from django.db import models
from users import Users #  他同様Usersモデルによって変更あり

# 開発中に変更があるかも
class Markdown(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    # TODO
    # 直接マークダウンを入れるかmdファイルをサーバーに保存し、それをクライアントに返す式にするかで
    # Char(URL)かText(markdown)か変わってくる
    data = models.CharField(max_length=255, null=False)
    # TODO
    # 画像の挿入も検討したい
    # image =     
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        db_name = 'markdown'