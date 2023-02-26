"""
認証関係のフォーム
"""
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm

from django import forms

class SignupForm(UserCreationForm):
    """サインアップ用のフォーム"""
    
    email = forms.EmailField(required=True, label='メールアドレス')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({'class':'form-control', 'placeholder': "Email"})
        self.fields["password1"].widget.attrs.update({'class': 'form-control', 'placeholder': "パスワード"})
        self.fields["password2"].widget.attrs.update({'class': 'form-control', 'placeholder': "確認用のパスワード"})
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('email', 'password1', 'password2')
            
