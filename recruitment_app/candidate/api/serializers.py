"""
serializer for Candidate
"""

from rest_framework import generics
from rest_framework import serializers
from ..models import CandidateJobStatus, Skill, Visa



class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class VisaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visa
        fields = '__all__'

class CandidateSerializer(serializers.ModelSerializer):
    job_title = serializers.SerializerMethodField()
    skills = SkillSerializer(read_only=True, many=True)
    visas = VisaSerializer(read_only=True, many=True)
    candidate_details = serializers.SerializerMethodField()
    class Meta:
        model = CandidateJobStatus
        fields = ('id', 'job_id', 'candidate', 'job_title',  'resume', 'stage', 'skills', 'visas', 'candidate_details')

    def get_job_title(self, obj):
        if obj and obj.job_id:
            return str(obj.job_id)

    def get_candidate_details(self, obj):
        if obj and obj.candidate:
            candidate_dict = dict()
            candidate_dict['first_name'] = obj.candidate.first_name
            candidate_dict['last_name'] = obj.candidate.last_name
            candidate_dict['email'] = obj.candidate.email
            return candidate_dict
        return None

