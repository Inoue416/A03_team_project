from django.db import models

# Create your models here.
class Universities(models.Model):
    id = models.CharField(primary_key=True, max_length=255, unique=True, null=False)
    name = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'universities'