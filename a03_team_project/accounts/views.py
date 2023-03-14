from django.views.generic import CreateView
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView
)
from django.contrib import messages

from accounts.forms import SignupForm, LoginForm

from django.http import HttpResponseRedirect
from django.contrib.auth import logout as auth_logout

from django.urls import reverse_lazy

# Create your views here.


class SignUpView(CreateView):
    """サインアップのビュー"""
    form_class = SignupForm
    success_url = reverse_lazy('login')
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
    
    def get(self, request, *args, **kwargs):
        auth_logout(request)
        messages.info(request, 'ログアウトしました', extra_tags="primary")
        return HttpResponseRedirect('/')    

class CustomPasswordChangeView(PasswordChangeView):
    
    success_url = reverse_lazy('home')
    
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
