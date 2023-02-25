from django.db import models
from app.models.user import User #  他同様Userモデルによって変更あり

# 開発中に変更があるかも
class MarkdownPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # TODO
    # 直接マークダウンを入れるかmdファイルをサーバーに保存し、それをクライアントに返す式にするかで
    # Char(URL)かText(markdown)か変わってくる
    title = models.CharField(max_length=255, null=False)
    data = models.TextField(null=False)
    # TODO
    # 画像の挿入も検討したい
    # image =     
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'markdown_post'