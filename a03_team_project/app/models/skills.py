from django.db import models


class Skills(models.Model):
    id = models.AutoField(primary_key=True)
    skill = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        db_name = 'skills'