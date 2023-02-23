from django.db import models
from app.models.users import Users
from app.models.universities import Universities
from app.models.grade import Grade


class StudentProfile(models.Model):
    # usersモデルの定義名によって変更
    student_id = models.OneToOneField(Users, on_delete=models.CASCADE)
    university_id = models.OneToOneField(Universities, on_delete=models.CASCADE)
    grade = models.OneToOneField(Grade, on_delete=models.PROTECT)
    icon = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'student_profile'