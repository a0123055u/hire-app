"""
serializer for Candidate
"""

from rest_framework import generics
from rest_framework import serializers
from ..models import CandidateJobStatus


class CandidateSerializer(serializers.ModelSerializer):
    job_title = serializers.SerializerMethodField()
    class Meta:
        model = CandidateJobStatus
        fields = '__all__'

    def get_job_title(self, obj):
        if obj and obj.job_id:
            return str(obj.job_id)
