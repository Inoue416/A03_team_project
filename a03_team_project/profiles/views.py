from django.shortcuts import redirect
from ssl import get_server_certificate
from django.views.generic.edit import CreateView
from app.models import Universities, Grade, StudentProfile, User

from profiles.forms import CompanyForm#, StudentMultiForm
# from extra_views import InlineFormSetFactory, CreateWithInlinesView

class CompanyProfileCreateView(CreateView):
    template_name = 'profile/company.html'
    form_class = CompanyForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        print('is company?')
        print(self.request.user.is_company)
        if form.is_valid() and self.request.user.is_company:
            qryset = form.save(commit=False)
            qryset.company_id = self.request.user.id
            qryset.save()
            return self.form_valid(form)

        else:
            return self.form_invalid(form)

# class UniversityForm(InlineFormSetFactory):
#     model = Universities
#     fields = ['name']

# class GradeForm(InlineFormSetFactory):
#     model = Grade
#     fields = ['grade']

# class StudentProfileCreateView(CreateWithInlinesView):
#     model = StudentProfile
#     fields = ['icon']
#     context_object_name = 'student'
#     inlines = [UniversityForm, GradeForm]
#     template_name = 'profile/student.hyml'
#     success_url = '/'


# class StudentProfileCreateView(CreateView):
#     template_name = 'profile/student.html'
#     form_class = StudentMultiForm
#     success_url = '/'

#     def form_valid(self, form):
#         qryset = form.save(commit=False)
#         qryset.student = self.request.user
#         qryset.save()

#         return self.form_valid(form)

#     def form_invalid(self, form):
#         return self.form_invalid(form)
