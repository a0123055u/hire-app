from django.test import TestCase

# Create your tests here.
import json
import pytest
# from rest_framework import status
from django.test import TestCase, Client
# from django.urls import reverse
from .models import CandidateProfile
from django.contrib.auth.models import User
from .api.serializers import CandidateSerializer
# import recruitment_app.job_application.models
import job_application.models

# from ..job_application.models import JobDetails


# initialize the APIClient app
client = Client()


# @pytest.fixture(scope="session")
# def fixture_1():
#     # candidate = CandidateProfile.objects.all()
#     print(f"Fixture 1")
#     return 1
#
# def test_example1(fixture_1):
#     num = fixture_1
#     print("test 1")
#     assert num == 1
#
# def test_example2(fixture_1):
#     print("test 2")
#     num = fixture_1
#     assert num == 1
#
# @pytest.fixture
# def yield_fixture():
#     print('Start Test Phase')
#     yield 6
#     print("End of yield")
#
# def test_final(yield_fixture):
#     print('run test_final')
#     assert yield_fixture == 6
#
#
# @pytest.mark.django_db
# def test_create_user():
#     User.objects.create_user('test', 'test@mailinator.com', 'test')
#     assert User.objects.count() == 1

def change_status(local_stage):
    response = client.put('/candidate/api/profile/update/1', data={"stage": local_stage},
                          content_type="application/json")
    cp = CandidateProfile.objects.filter().values_list('stage', flat=True)[0]
    print(f'local_stage - {local_stage}, cp -{cp}, response.status_code - {response.status_code}, local_stage == cp {local_stage == cp and response.status_code == 200}')
    # assert local_stage == cp and response.status_code == 200 if not negative and not error else local_stage != cp and response.status_code != 200
    assert local_stage == cp and response.status_code == 200


def change_status_fail(local_stage):
    response = client.put('/candidate/api/profile/update/1', data={"stage": local_stage},
                          content_type="application/json")
    cp = CandidateProfile.objects.filter().values_list('stage', flat=True)[0]
    response_data = response.json()

    print(f'local_stage (fail checking) - {local_stage}, cp -{cp}, response_data {response_data} ,respponse code {response.status_code}, local_stage != cp and {local_stage != cp and response.status_code != 200}')
    # assert local_stage == cp and response.status_code == 200 if not negative and not error else local_stage != cp and response.status_code != 200
    assert local_stage != cp and response.status_code != 200


@pytest.fixture
def set_up_models():
    print(f'Executing fixtures set_up_models')
    job_application.models.JobDetails.objects.create(title='test job', description='test job',
                                                     is_accepting_applicant=True, maximum_head_count=5)
    job = job_application.models.JobDetails.objects.filter()[0]
    # default stage taken when object is created "pending"
    CandidateProfile.objects.create(
        first_name='Casper', email='Casper@mailinator.com', last_name='Ronie', job_id=job)


@pytest.fixture
def set_model_4_users():
    print(f'Running fixture set_model_4_users')
    job_application.models.JobDetails.objects.create(title='test job', description='test job',
                                                     is_accepting_applicant=True, maximum_head_count=5)
    job = job_application.models.JobDetails.objects.filter()[0]
    CandidateProfile.objects.create(
        first_name='Casper', email='Casper@mailinator.com', last_name='Ronie', job_id=job)
    CandidateProfile.objects.create(
        first_name='Muffin', email='Muffin@mailinator.com', last_name='Chuk', job_id=job)
    CandidateProfile.objects.create(
        first_name='Rambo', email='Rambo@mailinator.com', last_name='Gazaki', job_id=job)
    CandidateProfile.objects.create(
        first_name='Ricky', email='Ricky@mailinator.com', last_name='Nick', job_id=job)


@pytest.mark.django_db
def test_candidate_creation_w_job_app(set_model_4_users):
    response = client.get('/candidate/api/profile?format=json')
    print(f'response data {response.data}')
    assert CandidateProfile.objects.count() == 4 and job_application.models.JobDetails.objects.count() == 1
    candidates_net = CandidateProfile.objects.filter()
    serializer = CandidateSerializer(candidates_net, many=True)
    serializer_data = serializer.data
    print(f'serializer_data count {len(serializer_data)}, candidates_net {len(candidates_net)}')
    assert len(response.data) == len(serializer_data)


@pytest.mark.django_db
def test_status_change_flow_recruitment(set_up_models):
    # https://docs.djangoproject.com/en/4.1/topics/testing/tools/

    # Decision matrix
    # {'pending': 'PENDING', 'reviewing': 'REVIEWING', 'shortlisted': 'SHORTLISTED', 'interviewing': 'INTERVIEWING', 'advanced_interviewing': 'ADVANCED INTERVIEWING', 'rejected_by_company': 'REJECTED BY COMPANY', 'offered': 'OFFERED', 'hired': 'HIRED', 'rejected_by_candidate': 'REJECTED BY CANDIDATE', 'on_hold': 'ON HOLD'}
    # End status of applicant "rejected_by_company", "rejected_by_candidate", "hired"
    # Special case "on_hold" can be changed from any valid status to this, vise versa

    local_stage = 'reviewing'
    change_status(local_stage)

    local_stage = 'shortlisted'
    change_status(local_stage)

    local_stage = 'interviewing'
    change_status(local_stage)

    local_stage = 'advanced_interviewing'
    change_status(local_stage)

    local_stage = 'offered'
    change_status(local_stage)

    local_stage = 'hired'
    change_status(local_stage)


@pytest.mark.django_db
def test_on_hold_f_valid(set_up_models):
    local_stage = 'reviewing'
    change_status(local_stage)

    local_stage = 'on_hold'
    change_status(local_stage)

    local_stage = 'shortlisted'
    change_status(local_stage)

    local_stage = 'on_hold'
    change_status(local_stage)

    local_stage = 'interviewing'
    change_status(local_stage)

    local_stage = 'on_hold'
    change_status(local_stage)

    local_stage = 'advanced_interviewing'
    change_status(local_stage)

    local_stage = 'on_hold'
    change_status(local_stage)

    local_stage = 'offered'
    change_status(local_stage)

    local_stage = 'on_hold'
    change_status(local_stage)

    local_stage = 'hired'
    change_status(local_stage)

    local_stage = 'on_hold'
    change_status_fail(local_stage)

    local_stage = 'on_hold'
    change_status_fail(local_stage)

    local_stage = 'rejected_by_candidate'
    change_status_fail(local_stage)

    local_stage = 'rejected_by_company'
    change_status_fail(local_stage)

