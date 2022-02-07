from django.contrib import admin
from django.urls import path, include
from .views import add_candidate, CandidateListView, CandidateUpdateView
urlpatterns = [
    path('recruitment/', add_candidate, name="candidate_add"),
    path('list/', CandidateListView.as_view(), name='candidate_list'),
    path('list/<pk>/update/', CandidateUpdateView.as_view(), name='candidate_update'),
]