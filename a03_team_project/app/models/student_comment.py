from django.db import models

class StudentComment(models.Model):
    id = models.AutoField(primary_key=True)
    markdown_id = models.CharField(max_length=255, null=False)
    user_id = models.CharField(max_length=255, null=False)
    comment = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'student_comment'