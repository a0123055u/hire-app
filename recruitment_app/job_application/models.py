import uuid

from django.db import models


# Create your models here.
class JobDetails(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(null=False, max_length=100, blank=False)
    description = models.TextField(null=False, blank=False)
    is_accepting_applicant = models.BooleanField(default=True)
    maximum_head_count = models.IntegerField(blank=False, null=False, default=1)

    def __str__(self):
        return self.title
# Test comment Gowtham
