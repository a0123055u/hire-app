from django.test import TestCase

# Create your tests here.
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import CandidateProfile
from .api.serializers import CandidateSerializer
from job_application.models import JobDetails

# initialize the APIClient app
client = Client()
class GetAllTest(TestCase):
    """ Test module for GET all puppies API """
    #     first_name = models.CharField(null=False, blank=False, max_length=255)
    #     last_name = models.CharField(null=False, blank=False, max_length=255)
    #     email = models.EmailField(max_length=255)
    #     job_id = models.ForeignKey(JobDetails, on_delete=models.CASCADE)
    #     resume = models.BinaryField()
    #     stage = models.CharField(max_length=150, choices=STATUS_CHOICES, default='pending')
    # def setUp(self):
    #
    #     CandidateProfile.objects.all().delete()
    #     print(JobDetails.objects.filter(id='045dbe33-0ea9-47b1-9e49-2a91caf15327'))
    #     CandidateProfile.objects.create(
    #         first_name='Casper', email='Casper@mailinator.com', last_name='Ronie', job_id=JobDetails.objects.filter(id='f69d784f-1b1c-40b5-a8ca-e976fe316821'))
    #     CandidateProfile.objects.create(
    #         first_name='Muffin', age=1, last_name='Chuk', job_id=JobDetails.objects.filter(id='f69d784f-1b1c-40b5-a8ca-e976fe316821'))
    #     CandidateProfile.objects.create(
    #         first_name='Rambo', age=2, last_name='Gazaki', job_id=JobDetails.objects.filter(id='f69d784f-1b1c-40b5-a8ca-e976fe316821'))
    #     CandidateProfile.objects.create(
    #         first_name='Ricky', age=6, last_name='Nick', job_id=JobDetails.objects.filter(id='f69d784f-1b1c-40b5-a8ca-e976fe316821'))

    def test_get_all_candidate(self):
        # get API response
        response = client.get('/candidate/api/profile?format=json')
        # get data from db
        puppies = CandidateProfile.objects.all()
        serializer = CandidateSerializer(puppies, many=True)
        # print(self.assertEqual(response.data, serializer.data))
        print(response.status_code, response.data)
        print(self.assertEqual(response.status_code, status.HTTP_200_OK))


