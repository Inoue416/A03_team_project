from django.urls import path
from profiles.views import CompanyProfileCreateView


urlpatterns = [
    path('company/', CompanyProfileCreateView.as_view(), name='company')
]