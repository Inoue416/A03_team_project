from django.views.generic import CreateView
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView
)
from django.contrib import messages

from accounts.forms import SignupForm, LoginForm

# NOTE:使えるかも
from django.contrib.auth import authenticate, login

# Create your views here.


class SignUpView(CreateView):
    """サインアップのビュー"""
    form_class = SignupForm
    success_url = '/'
    template_name = 'registration/signup.html'
    
    # NOTE:messageの表示機能を追加したいがためのオーバライド
    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        self.object = None
        form = self.get_form()
        if form.is_valid():
            messages.info(request, 'サインアップしました', extra_tags="primary")
            return self.form_valid(form)
        else:
            messages.error(request, 'サインアップできませんでした', extra_tags="danger")
            return self.form_invalid(form)
    

class LoginView(LoginView):
    """ログインのビュー"""
    authentication_form = LoginForm
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    
    # NOTE:messageの表示機能を追加したいがためのオーバライド
    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        
        form = self.get_form()
        if form.is_valid():
            messages.info(request, 'ログインしました。', extra_tags="primary")
            return self.form_valid(form)
        else:
            messages.error(request, 'ログインできませんでした', extra_tags="danger")
            return self.form_invalid(form)
    
class CustomLogoutView(LogoutView):
    
    # HACK: templateを表示して、リダイレクトするような仕組みになっており、リダイレクトした後に（メッセージミドルウェアの）メッセージを表示できなくなってしまう。
    # 　　メッセージを表示する対策としてtemplateにホームページのテンプレートを指定して、リダイレクトしないことによって、メッセージが表示されるような形にしている。
    template_name = 'index.html'
    
    def get(self, request, *args, **kwargs):
        messages.info(request, 'ログアウトしました', extra_tags="primary")
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

class CustomPasswordChangeView(PasswordChangeView):
    
    success_url = '/'
    
    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():
            messages.info(request, 'パスワードを変更しました', extra_tags="primary")
            return self.form_valid(form)
        else:
            messages.info(request, 'パスワードを変更できませんでした', extra_tags='danger')
            return self.form_invalid(form)
