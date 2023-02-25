from django.db import models
from app.models.user import User
from app.models.skills import Skills

class SkillMiddle(models.Model):
    # idはUserテーブルのキーをフォーリンキーとして用いる
    #id = models.BigAutoField()
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skills, on_delete=models.CASCADE)

    class Meta:
        db_table = 'skill_middle'