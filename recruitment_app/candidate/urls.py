from django.contrib import admin
from django.urls import path, include, re_path
# from .views import add_candidate, CandidateListView, CandidateUpdateView
from .api.views import CandidateViewSet, CandidateAPIUpdate, profile_status
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    # path('recruitment/', add_candidate, name="candidate_add"),
    # path('list/', CandidateListView.as_view(), name='candidate_list'),
    # path('list/<pk>/update/', CandidateUpdateView.as_view(), name='candidate_update'),
    re_path(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/profile', CandidateViewSet.as_view(), name='api_candidate_profile'),
    path('api/profile/update/<int:pk>', CandidateAPIUpdate.as_view(), name='api_candidate_update'),
    path('api/profile/status', profile_status, name='api_candidate_status'),
    # path('',) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]