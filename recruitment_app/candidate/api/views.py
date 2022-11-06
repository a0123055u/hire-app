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

class CandidateViewSet(generics.ListAPIView):
    model = CandidateProfile
    serializer_class = CandidateSerializer
    queryset = CandidateProfile.objects.filter(~Q(stage__in=['rejected', 'rejected_by_candidate', 'rejected_by_company']))
