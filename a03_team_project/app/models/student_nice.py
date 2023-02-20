from django.db import models
from app.models.student_markdown import StudentMarkDown

class StudentNice(models.Model):
    markdown_id = models.ForeignKey(StudentMarkDown, null=False, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'student_nice'