from django.db import models
from app.models.users import Users
from app.models.skills import Skills

class SkillMiddle(models.Model):
    # idはUsersテーブルのキーをフォーリンキーとして用いる
    #id = models.BigAutoField()
    student = models.ForeignKey(Users, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skills, on_delete=models.CASCADE)

    class Meta:
        db_table = 'skill_middle'