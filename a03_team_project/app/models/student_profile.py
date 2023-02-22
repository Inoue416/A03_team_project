from django.db import models
from universities import Universities
from grade import Grade
from users import Users  # usersモデルの定義名によって変更

class StudentProfile(models.Model):
    # usersモデルの定義名によって変更
    id = models.AutoField(primary_key=True)
    student_id = models.OneToOneField(Users, on_delete=models.CASCADE)
    university_id = models.ForeignKey(Universities, on_delete=models.CASCADE)
    grade = models.OneToOneField(Grade, on_delete=models.PROTECT)
    icon = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'student_profile'