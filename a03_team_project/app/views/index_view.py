from django.views.generic import ListView
from app.models.markdown_post import MarkdownPost



class IndexView(ListView):
    template_name = "index.html"
    model = MarkdownPost
    ordering = ["-created_at"]
    context_object_name  = "markdown_objects"
    