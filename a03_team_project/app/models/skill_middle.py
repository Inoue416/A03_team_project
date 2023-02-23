from django.db import models
from app.models.users import Users
from app.models.skills import Skills

class SkillMiddle(models.Model):
    # idはUsersテーブルのキーをフォーリンキーとして用いる
    id = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True)
    skill_id = models.ManyToManyField(Skills, related_name='have_skills')

    class Meta:
        db_table = 'skill_middle'