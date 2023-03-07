from dataclasses import fields
from this import s
from django import forms
from betterforms.multiform import MultiModelForm

from app.models import CompanyProfile, StudentProfile, Universities, Grade

class CompanyForm(forms.ModelForm):

    class Meta:
        model = CompanyProfile
        fields = ['outline', 'businness_contents', 'image', 'homepage']

        labels = {
            'outline': '会社概要',
            'businness_contents': '業務内容',
            'image': 'アイコン',
            'homepage': 'ホームページのURL',
        }

        def __init__(self, user, *args, **kwargs):
            self.login_user = user
            super().__init__(*args, **kwargs)

        def save(self, **kwargs):

            company = CompanyProfile(
                    outline = self.cleaned_data['outline'],
                    businness_contents = self.cleaned_data['businness_contents'],
                    image = self.cleaned_data['image'],
                    homepage = self.cleaned_data['homepage'],
                )

            company.save()  


            return company

# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = StudentProfile
#         fields = ['icon']

#         labels = {
#             'icon': 'プロフィール画像'
#         }

        # def save(self, commit=True):
        #     student = super(StudentForm, self).save(commit=commit)

        #     if commit:
        #         student.save()

        #     return student

# class UniversityForm(forms.ModelForm):
#     class Meta:
#         model = Universities
#         fields = ['name']

#         labels = {
#             'name': '大学'
#         }

# class GradeForm(forms.ModelForm):
#     class Meta:
#         model = Grade
#         fields = ['grade']

#         labels = {
#             'grade': '学年'
#         }

# class StudentMultiForm(MultiModelForm):

#     class Meta:
#         form_classes = {
#             'StudentProfile': StudentForm,
#             'Universities': UniversityForm,
#             'Grade': GradeForm,
#         }

#         def __init__(self, user, *args, **kwargs):
#             self.login_user = user
#             super().__init__(*args, **kwargs)

#         def save(self, **kwargs):
#             student = StudentProfile(
#                 university = self.cleaned_data['name'],
#                 grade = self.cleaned_data['grade'],
#                 icon = self.cleaned_data['icon']
#             ),

#             student.save()

#             return student