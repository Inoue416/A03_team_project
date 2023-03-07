from django.db import models
from app.models.markdown_post import MarkdownPost
from app.models.user import User

class Comment(models.Model):
    markdown = models.ForeignKey(MarkdownPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "comment"