"""
API for Candidate
"""

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
from ..models import CandidateProfile
from .serializers import CandidateSerializer


class CandidateViewSet(generics.ListAPIView):
    model = CandidateProfile
    serializer_class = CandidateSerializer
    queryset = CandidateProfile.objects.all()
