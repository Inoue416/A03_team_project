from django.db import models
from app.models.company_markdown import CompanyMarkDown

class CompanyNice(models.Model):
    markdown_id = models.ForeignKey(CompanyMarkDown, null=False, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'company_nice'