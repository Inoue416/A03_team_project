from django.db import models
from app.models.users import Users

class Follow(models.Model):
    follower = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='following')

    class Meta:
        db_table = 'follow'