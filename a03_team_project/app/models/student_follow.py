from django.db import models
from app.models.students import Students

class StudentFollow(models.Model):
    student_id = models.ForeignKey(Students, null=False, on_delete=models.CASCADE)
    other_id = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'student_follow'