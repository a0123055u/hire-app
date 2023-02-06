import datetime

from django.db import models
from django.urls import reverse
from job_application.models import JobDetails
from django_extensions.db.models import TimeStampedModel
from phonenumber_field.phonenumber import PhoneNumber
from django_countries.fields import CountryField
from django.utils.text import gettext_lazy as _
from django.core.validators import RegexValidator
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

SEX_CHOICES=(('male', 'MALE'),
             ('female', 'FEMALE'),
             ('not_disclosed', 'NA'))

class Skill(TimeStampedModel):
    name = models.CharField(max_length=50)
    is_valid = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Visa(TimeStampedModel):
    name = models.CharField(max_length=100, null=False, blank=False)
    validity_in_years = models.IntegerField(default=0)
    validity_in_months = models.IntegerField(default=0)
    is_valid = models.BooleanField(default=False)
    country = CountryField(default='IN')
    def __str__(self):
        return f'[{self.country.code}] - {self.name}'
class CandidateDetailedProfile(TimeStampedModel):
    first_name = models.CharField(null=False, blank=False, max_length=255)
    last_name = models.CharField(null=False, blank=False, max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(null=False, blank=False, max_length=255, default="111111")
    sex = models.CharField(max_length=190, choices=SEX_CHOICES, default='not_disclosed')
    address = models.TextField(null=False, blank=False, default="") #support multiline
    postal_code = models.CharField(max_length=6, validators=[RegexValidator('^[0-9]{6}$', _('Invalid postal code'))], default="600000")
    current_residency_country = CountryField(default='US')
    nationality = CountryField(default='IN')
    resume_file = models.FileField(upload_to='candidate/resumes')
    skills = models.ManyToManyField(Skill, default="1")
    total_years_of_experience = models.IntegerField(default=0)
    total_relevant_years_of_experience = models.IntegerField(default=0)
    current_salary_monthly = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    current_bonus_yearly = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    expected_salary_monthly = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    notice_period_in_months = models.IntegerField(default=1)
    require_visa_to_work = models.BooleanField(default=True)
    current_visa = models.ForeignKey(Visa, on_delete=models.CASCADE, default=1)
    current_visa_validity = models.DateField(default=datetime.date.today)
    reference_one_at_work = models.TextField(null=True, blank=True, default="")
    reference_two_at_work = models.TextField(null=True, blank=True, default="")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'[{self.current_residency_country}]-[{self.id}]{self.first_name}-[{self.email}]'
class CandidateJobStatus(TimeStampedModel):
    #TO DO - GOWTHAM ADD RELATION OF CandidateDetailedProfile AS fk
    candidate = models.ForeignKey(CandidateDetailedProfile, on_delete=models.CASCADE, default=18)
    job_id = models.ForeignKey(JobDetails, on_delete=models.CASCADE)
    resume = models.BinaryField()
    stage = models.CharField(max_length=190, choices=STATUS_CHOICES, default='pending')

    def get_absolute_url(self):
        return reverse('candidate_list')

    def __str__(self):
        return f'[{self.candidate.current_residency_country}]-[{self.id}]-{self.candidate.first_name}-[{self.candidate.email}]--{self.stage}'



