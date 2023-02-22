from django.db import models
from users import Users

class Follow(models.Model):
    from_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    to_id = models.ForeignKey(Users, on_delete=models.CASCADE)

    class Meta:
        db_table = 'follow'