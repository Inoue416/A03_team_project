from django.db import models

class StudentComment(models.Model):
    id = models.CharField(max_length=255, null=False, primary_key=True, primary_key=True)
    user_id = models.CharField(max_length=255, null=False)
    comment = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        db_name = 'student_comment'