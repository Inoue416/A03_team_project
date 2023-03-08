from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from app.models.markdown_post import MarkdownPost
from app.models.nice import Nice
from app.models.comment import Comment


# TODO: いいねとコメント数の集計
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"
    context_object_name  = "markdown_objects"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        markdown_objects = []
        markdown_data = MarkdownPost.objects.order_by('-created_at').all()
        for md_data in markdown_data:
            nice_num = Nice.objects.filter(markdown=md_data).count()
            comment_num = Comment.objects.filter(markdown=md_data).count()
            markdown_objects.append({
                'md_data': md_data,
                'nice_num': nice_num, 
                'comment_num': comment_num
            })
        context['markdown_objects'] = markdown_objects
        return context
    