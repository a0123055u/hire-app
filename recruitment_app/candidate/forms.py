from django.forms import ModelForm
from candidate.models import CandidateProfile
from django import forms

class CandidateForm(ModelForm):
    class Meta:
        model = CandidateProfile
        fields = '__all__'


# class CandidateUpdateForm(ModelForm):
#     first_name = forms.CharField(label= 'First Name')
#     last_name = forms.CharField(label='Last Name')
#
#     STATUS_CHOICES = (('pending', 'PENDING'),
#                       ('reviewing', 'REVIEWING'),
#                       ('shortlisted', 'SHORTLISTED'),
#                       ('interviewing', 'INTERVIEWING'),
#                       ('advanced_interviewing', 'ADVANCED INTERVIEWING'),
#                       ('rejected', 'REJECTED'),
#                       ('offered', 'OFFERED'),
#                       ('hired', 'HIRED'),)
#     stage = forms.ChoiceField(choices=STATUS_CHOICES)
#
#     # def clean_stage(self):
#     #     import pdb
#     #     pdb.set_trace()
#     #     if not self.is_valid():
#     #         raise forms.ValidationError('The Status is not updated due to Permission or Order of Change')
#     class Meta:
#         model = CandidateProfile
#         fields = ['first_name', 'last_name', 'stage']
