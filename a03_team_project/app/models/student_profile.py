from django.db import models
from app.models.user import User
from app.models.universities import Universities
from app.models.grade import Grade


class StudentProfile(models.Model):
    # usersモデルの定義名によって変更
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    university = models.OneToOneField(Universities, on_delete=models.CASCADE)
    grade = models.OneToOneField(Grade, on_delete=models.PROTECT)
    icon = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'student_profile'