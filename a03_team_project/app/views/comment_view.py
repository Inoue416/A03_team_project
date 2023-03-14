from django.views.generic import FormView
from app.models.comment import Comment
from app.forms.comment_form import CommentForm
from django.urls import reverse_lazy

class CommentView(FormView):
    template_name = "comment_form.html"
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy("markdown_detail", kwargs={"id": self.kwargs.get('markdown_id')})

    def form_valid(self, form):
        form.save(self.request.user.id)
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['markdown_id'] = self.kwargs.get('markdown_id')
        return context