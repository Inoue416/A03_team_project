from django.db import models
from companies import Companies

class StudentFollow(models.Model):
    company_id = models.ForeignKey(Companies, null=False, on_delete=models.CASCADE)
    other_id = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        db_name = 'student_follow'