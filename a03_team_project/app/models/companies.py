from django.db import models

# Create your models here.
class Companies(models.Model):
    id = models.CharField(max_length=255, null=False, primary_key=True)
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'companies'