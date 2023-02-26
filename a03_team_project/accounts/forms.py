"""
認証関係のフォーム
"""
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.password_validation import validate_password
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
            
class LoginForm(forms.Form):
    """ログイン用のフォーム"""
    email = forms.EmailField(label='メールアドレス')
    password = forms.CharField(
        label='パスワード',
        min_length=8,
        widget=forms.PasswordInput(),
        help_text=password_validation.password_validators_help_text_html(),
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        
    def clean_password(self):
        password = self.cleaned_data['password']
        validate_password(password)
        return password
        