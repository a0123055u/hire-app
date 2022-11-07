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
from ..models import STATUS_CHOICES
class CandidateViewSet(generics.ListAPIView):
    model = CandidateProfile
    serializer_class = CandidateSerializer
    queryset = CandidateProfile.objects.filter(~Q(stage__in=['rejected', 'rejected_by_candidate', 'rejected_by_company']))


class CandidateAPIUpdate(generics.UpdateAPIView):
    queryset = CandidateProfile.objects.all()
    serializer_class = CandidateSerializer

    def update(self, request, *args, **kwargs):
        # The required object is obtained from django glossary
        # https://docs.djangoproject.com/en/3.1/glossary/
        instance = self.get_object()
        stage = str(request.data.get("stage"))
        dict_status = dict(STATUS_CHOICES)
        actual_status = dict_status.get(stage, None)
        serializer = CandidateSerializer(instance, many=False)
        if instance.stage != actual_status and actual_status:
            instance.stage = actual_status
            instance.save()
        else:
            return Response({'message':'fail due to wrong status','error':True,'code':400,'result':''})
        return Response(serializer.data)
