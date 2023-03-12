from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from app.models.markdown_post import MarkdownPost
from app.models.nice import Nice
from app.models.comment import Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
        DIV_NUM = 10
        paginator = Paginator(markdown_objects, DIV_NUM)
        page = self.request.GET.get('page')
        page_objects = None
        try:
            page_objects = paginator.page(page)
        except PageNotAnInteger:
            page_objects = paginator.page(1)
        except EmptyPage:
            page_objects = paginator.page(paginator.num_pages)

        context['page_objects'] = page_objects
        return context
    