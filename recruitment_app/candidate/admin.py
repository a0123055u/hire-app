from django.contrib import admin
from candidate.models import CandidateJobStatus, CandidateDetailedProfile, Visa, Skill
# Register your models here.
admin.site.register(CandidateJobStatus)
admin.site.register(CandidateDetailedProfile)
admin.site.register(Visa)
admin.site.register(Skill)