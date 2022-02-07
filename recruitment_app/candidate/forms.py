from django.forms import ModelForm
from candidate.models import CandidateProfile


class CandidateForm(ModelForm):
    class Meta:
        model = CandidateProfile
        fields = '__all__'
