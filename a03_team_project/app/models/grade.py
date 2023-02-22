from django.db import models

class Grade(models.Model):
    id = models.AutoField(primary_key=True)
    grade = models.CharField(max_length=5, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'grade'