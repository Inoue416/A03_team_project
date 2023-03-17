"""a03_team_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app.views.index_view import IndexView
from app.views.markdown_detail_view import MarkdownDetailView
from app.views.comment_view import CommentView
from app.views.nice_view import NiceView
from app.views.delete_comment_view import DeleteCommentView
from app.views.formpage_view import formpage


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('', IndexView.as_view(), name='home'),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('markdown_detail/<int:id>', MarkdownDetailView.as_view(), name="markdown_detail"),
    path('comment/<int:markdown_id>', CommentView.as_view(), name="comment"),
    path('api/nice', NiceView.as_view(), name="nice"),
    path('<int:pk>/delete_comment/<int:markdown_id>', DeleteCommentView.as_view(), name="delete_comment"),
    path('profiles/', include('profiles.urls')),
    path("formpage/", formpage, name="formpage")
]
