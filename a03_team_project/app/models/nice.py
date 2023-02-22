from django.db import models
from users import Users  # 他同様
from markdown_post import MarkdownPost

class Nice(models.Model):
    # id = models.AutoField(primary_key=True)
    markdown_id = models.ForeignKey(MarkdownPost, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    class Meta:
        db_name = 'nice'
