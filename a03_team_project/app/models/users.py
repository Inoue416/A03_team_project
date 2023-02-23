from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255, null=False)
    is_student = models.BooleanField(null=True)
    is_company = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'users'