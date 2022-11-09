"""
serializer for Candidate
"""

from rest_framework import generics
from rest_framework import serializers
from ..models import CandidateProfile


class CandidateSerializer(serializers.ModelSerializer):
    job_title = serializers.SerializerMethodField()
    class Meta:
        model = CandidateProfile
        fields = ('id', 'first_name', 'last_name', 'email', 'job_id', 'job_title',  'resume', 'stage')

    def get_job_title(self, obj):
        if obj and obj.job_id:
            return str(obj.job_id)
