from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
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
        form = self.get_form()
        if form.is_valid():
            messages.info(request, 'サインアップしました')
            return self.form_valid(form)
        else:
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
            messages.info(request, 'ログインしました。')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
