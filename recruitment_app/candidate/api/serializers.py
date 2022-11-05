"""
serializer for Candidate
"""

from rest_framework import generics
from rest_framework import serializers
from ..models import CandidateProfile


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateProfile
        fields = '__all__'


