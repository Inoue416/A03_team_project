from django.db import models

class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'department'