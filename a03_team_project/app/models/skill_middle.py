from django.db import models
from users import Users
from skills import Skills

class SkillMiddle(models.Model):
    # idはUsersテーブルのキーをフォーリンキーとして用いる
    id = models.ForeignKey(Users, on_delete=models.CASCADE)
    skill_id = models.ForeignKey(Skills, on_delete=models.CASCADE)

    class Meta:
        db_table = 'skill_middle'