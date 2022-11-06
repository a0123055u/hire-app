from django.db import models
from django.urls import reverse
from job_application.models import JobDetails
# Create your models here.

STATUS_CHOICES = (('pending', 'PENDING'),
                  ('reviewing', 'REVIEWING'),
                  ('shortlisted', 'SHORTLISTED'),
                  ('interviewing', 'INTERVIEWING'),
                  ('advanced_interviewing','ADVANCED INTERVIEWING'),
                  ('rejected_by_company', 'REJECTED BY COMPANY'),
                  ('offered', 'OFFERED'),
                  ('hired', 'HIRED'),
                  ('rejected_by_candidate', 'REJECTED BY CANDIDATE'),
                  ('on_hold', 'ON HOLD')
                  )

class CandidateProfile(models.Model):
    first_name = models.CharField(null=False, blank=False, max_length=255)
    last_name = models.CharField(null=False, blank=False, max_length=255)
    email = models.EmailField(max_length=255)
    job_id = models.ForeignKey(JobDetails, on_delete=models.CASCADE)
    resume = models.BinaryField()
    stage = models.CharField(max_length=150, choices=STATUS_CHOICES, default='pending')

    def get_absolute_url(self):
        return reverse('candidate_list')

    def __str__(self):
        return self.email + " (" + str(self.job_id) + ") "+self.first_name + " " + self.last_name
