from django.views.generic import TemplateView
from app.models.markdown_post import MarkdownPost
from app.models.comment import Comment
from django.contrib.auth.mixins import LoginRequiredMixin
import json
from app.models.nice import Nice
from app.models.user import User

# TODO LoginRequiredMixinを継承する
class MarkdownDetailView(TemplateView):
    template_name = "markdown_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # マークダウンデータの取得
        data = MarkdownPost.objects.get(pk=self.kwargs.get('id'))
        context['markdown_object'] = data
        context['markdown_data'] = json.dumps({"data": data.data}, indent=2, ensure_ascii=False)
        # コメントとコメントの総数を取得
        context['comment_objects'] = Comment.objects.filter(markdown=data).all()
        context['comment_num'] = Comment.objects.filter(markdown=data).count()
        # いいねの総数取得
        context['nice_num'] = Nice.objects.filter(markdown=MarkdownPost.objects.get(pk=self.kwargs.get('id'))).count()
        # いいねしているかを取得
        is_nice = Nice.objects.filter(
            markdown=MarkdownPost.objects.get(pk=self.kwargs.get('id')),
            user=User.objects.get(id=self.request.user.id)
        ).first()
        if is_nice == None:
            is_nice = False
        else:
            is_nice = True
        context['is_nice'] = is_nice
        return context