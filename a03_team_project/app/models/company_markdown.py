from django.db import models
from companies import Companies

class CompanyMarkDown(models.Model):
    id = models.CharField(max_length=255, null=False, primary_key=True)
    company_id = models.ForeignKey(Companies, on_delete=models.CASCADE)
    data = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        db_name = 'company_markdown'
