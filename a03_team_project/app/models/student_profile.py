from django.db import models
from students import Students
from universities import Universities
from skills import Skills


class StudentProfile(models.Model):
    student_id = models.OneToOneField(Students, on_delete=models.PROTECT)
    university_id = models.ForeignKey(Universities, on_delete=models.DO_NOTHING)
    grade = models.CharField(max_length=5, null=False)
    good_skill = models.ForeignKey(Skills, on_delete=models.DO_NOTHING, null=True)
    icon = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        db_name = 'student_profile'