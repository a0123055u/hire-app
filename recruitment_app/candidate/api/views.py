"""
API for Candidate
"""

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
from ..models import CandidateProfile
from .serializers import CandidateSerializer
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
import logging

logger = logging.getLogger(__name__)

class CandidateViewSet(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    model = CandidateProfile
    serializer_class = CandidateSerializer

    def get_queryset(self):
        queryset =CandidateProfile.objects.filter(~Q(stage__in=['rejected_by_candidate', 'rejected_by_company']))
        id = self.request.query_params.get('id', None)
        if id:
            queryset = queryset.filter(id=id)
        return queryset


class CandidateAPIUpdate(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CandidateProfile.objects.filter(~Q(stage__in=['rejected_by_candidate', 'rejected_by_company']))
    serializer_class = CandidateSerializer

    def update(self, request, *args, **kwargs):
        # The required object is obtained from django glossary
        # https://docs.djangoproject.com/en/3.1/glossary/
        try:
            instance = self.get_object()
            logger.info(f'Candidate filtered to update {instance}')
            stage = str(request.data.get("stage")) if request.data.get("stage", None) else None
            dict_status = dict(STATUS_CHOICES)
            actual_status = stage if stage in list(dict_status.keys()) else None
            serializer = CandidateSerializer(instance, many=False)
            if not stage:
                return Response({'message': 'stage cannot be empty or null', 'error': True, 'result': ''}, status=status.HTTP_400_BAD_REQUEST)
            if not actual_status:
                return Response({'message': 'stage not found!!', 'error': True, 'result': ''}, status=status.HTTP_400_BAD_REQUEST)
            if instance.stage == 'hired' or 'rejected' in instance.stage:
                return Response({'message': 'Cannot Change the status of hired / rejected person ', 'error': True, 'result': ''}, status=status.HTTP_400_BAD_REQUEST)
            actual_status_index = list(dict_status.keys()).index(stage)
            old_status_index = list(dict_status.keys()).index(instance.stage)
            is_new_stage_set = instance.stage != actual_status
            is_progressive_change = actual_status_index > old_status_index and not actual_status_index - old_status_index > 1
            ignore_order_in_status_change = ['rejected_by_candidate', 'on_hold', 'rejected_by_company']
            # cannot set same status for update, must be valid status , must  progress one step at a time and must not be in rejected status list
            if instance.stage == 'advanced_interviewing' and actual_status == 'offered':
                instance.stage = actual_status
                instance.save()
            elif instance.stage != actual_status and actual_status and is_progressive_change:
                instance.stage = actual_status
                instance.save()
                logger.info(f'Candidate object {instance} updated with stage {stage} successfully !!')
            # Can set rejected from any status and no need to check progressive for on_hold, cannot set same status and is not rejected
            elif (stage in ignore_order_in_status_change or instance.stage == "on_hold") and is_new_stage_set:
                instance.stage = actual_status
                instance.save()
                logger.info(f'Candidate object {instance} updated with stage {stage} successfully !!')
            else:
                return Response({'message': 'fail due to wrong status change', 'error': True, 'result': ''}, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return Response({'message': f'{ex}', 'error': True, 'result': ''}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

from ..models import STATUS_CHOICES
import json
from django.http import JsonResponse
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_status(request):
    result = dict()
    result = json.loads(json.dumps(dict(list(STATUS_CHOICES))))
    return JsonResponse(result)
