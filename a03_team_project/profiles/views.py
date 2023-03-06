# from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.http import HttpResponse

from profiles.forms import CompanyForm

class CompanyProfileCreateView(CreateView):
    template_name = 'profile/company.html'
    form_class = CompanyForm
    success_url = '/'

    def form_valid(self, form):
        qryset = form.save(commit=False)
        qryset.company_id = self.request.user
        qryset.save()
