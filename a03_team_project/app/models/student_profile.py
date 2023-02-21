from django.db import models
from app.models.students import Students
from app.models.universities import Universities
from app.models.skills import Skills


class StudentProfile(models.Model):
    student_id = models.OneToOneField(Students, on_delete=models.PROTECT)
    university_id = models.ForeignKey(Universities, on_delete=models.DO_NOTHING)
    grade = models.CharField(max_length=5, null=False)
    good_skill = models.ForeignKey(Skills, on_delete=models.DO_NOTHING, null=True)
    icon = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'student_profile'