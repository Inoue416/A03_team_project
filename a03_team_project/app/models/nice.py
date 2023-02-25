from django.db import models
from app.models.user import User  # 他同様
from app.models.markdown_post import MarkdownPost

class Nice(models.Model):
    # id = models.AutoField(primary_key=True)
    markdown = models.ForeignKey(MarkdownPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'nice'
