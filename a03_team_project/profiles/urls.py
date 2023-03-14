from django.urls import path
from profiles.views import CompanyProfileCreateView#, StudentProfileCreateView


urlpatterns = [
    path('company/', CompanyProfileCreateView.as_view(), name='company'),
    # path('student/', StudentProfileCreateView.as_view(), name='student'),
]