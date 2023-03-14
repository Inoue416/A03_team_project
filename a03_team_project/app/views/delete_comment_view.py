from django.views import View
from app.models.comment import Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect

class DeleteCommentView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            Comment.objects.filter(id=kwargs.get('pk')).delete()
        except:
            return redirect('home')
        return redirect("markdown_detail", kwargs.get('markdown_id'))
    
    def post(self, *args, **kwargs):
        return redirect('home')
