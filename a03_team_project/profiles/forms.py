from django import forms

from app.models import CompanyProfile

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

        def save(self, request, **kwargs):

            company_id = request.user.id

            company = CompanyProfile(
                company_id = company_id,
                outline = self.cleaned_data['outline'],
                businness_contents = self.cleaned_data['businness_contents'],
                image = self.cleaned_data['image'],
                homepage = self.cleaned_data['homepage'],
            )

            company.save()

            return company