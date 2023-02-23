from django.db import models
from app.models.users import Users

class Follow(models.Model):
    from_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='follower')
    to_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='following')

    class Meta:
        db_table = 'follow'