from django.db import models
from app.models.students import Students

class StudentMarkDown(models.Model):
    id = models.CharField(max_length=255, null=False, primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    data = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'student_markdown'
