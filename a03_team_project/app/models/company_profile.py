from django.db import models
from app.models.companies import Companies


class CompanyProfile(models.Model):
    company_id = models.OneToOneField(Companies, on_delete=models.PROTECT)
    outline = models.TextField(null=False, default='作成中')
    businness_contents = models.TextField(null=False, default='作成中')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'company_profile'