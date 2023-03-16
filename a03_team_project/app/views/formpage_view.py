from django.shortcuts import render, redirect
from app.models.markdown_post import MarkdownPost
from app.models.user import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def formpage(request):

    if request.POST:
        try:
            user = User.objects.get(id=request.user.id)
            title = request.POST.get("title")
            mark_date = request.POST.get("markDate")
            MarkdownPost.objects.create(user=user, title=title, data=mark_date)
            messages.success(request, "投稿完了")
            return render(request, "app/formpage.html")
        except:
            messages.error(request, "入力値にエラーがあります")
            return render(request, "app/formpage.html")
        
    return render(request, "app/formpage.html")