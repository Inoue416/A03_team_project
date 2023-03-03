from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView


from accounts.forms import SignupForm, LoginForm

# NOTE:使えるかも
from django.contrib.auth import authenticate, login

# Create your views here.


class SignUpView(CreateView):
    """サインアップのビュー"""
    form_class = SignupForm
    success_url = '/'
    template_name = 'registration/signup.html'

class LoginView(LoginView):
    """ログインのビュー"""
    authentication_form = LoginForm
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    
# NOTE:template_nameだけなので、urls.pyで指定していいかも
# class LogoutView(LogoutView):
#     """ログアウトのビュー"""
#     template_name = 'registration/login.html'

class PsswordChangeView():
    """パスワード変更のビュー"""