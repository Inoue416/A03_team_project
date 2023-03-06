from django.urls import path

urlpatterns = [
    path('company/', createCompanyProfileView.as_view(), name='company')
]