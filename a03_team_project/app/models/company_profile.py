from distutils.command.upload import upload
from django.db import models
from app.models.user import User  # 他同様


class CompanyProfile(models.Model):
    company_id = models.OneToOneField(User, on_delete=models.CASCADE)
    outline = models.TextField(null=False, default='作成中')
    businness_contents = models.TextField(null=False, default='作成中')
    # 画像までのパスを格納予定
    image = models.ImageField(null=True, upload_to="company")
    homepage = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'company_profile'