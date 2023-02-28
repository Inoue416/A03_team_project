"""
認証関係のフォーム
"""
from django.contrib.auth import get_user_model, authenticate, password_validation
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.utils.translation import gettext_lazy as _

from django import forms


class SignupForm(UserCreationForm):
    """サインアップ用のフォーム"""
    
    # extra fields
    choice = forms.ChoiceField(choices=(('生徒', '生徒'), ('企業', '企業')))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # wiget style settings
        self.fields['name'].widget.attrs.update({'class':'form-control', 'placeholder': "名前"})
        self.fields["email"].widget.attrs.update({'class':'form-control', 'placeholder': "メールアドレス"})
        self.fields["password1"].widget.attrs.update({'class': 'form-control', 'placeholder': "パスワード"})
        self.fields["password2"].widget.attrs.update({'class': 'form-control', 'placeholder': "確認用のパスワード"})
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('name', 'email', 'password1', 'password2')
    
    def save(self, commit=True):
        """Create and return User object. (引数のcommitでセーブするか選べる。)"""
           
        # セレクトボックス（生徒or企業）の処理 （Userオブジェクト作成前の前処理）
        is_student = False
        is_company = False
        if self.cleaned_data['choice'] == '生徒':
            is_student = True
        if self.cleaned_data['choice'] == '企業':
            is_company = True
        
        # userオブジェクトの作成
        user = get_user_model()(
            name=self.cleaned_data['name'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1'],
            is_student=is_student,
            is_company=is_company,
        )
        # commit引数によって、DBに保存するorしない
        if commit:
            user.save()
            
        return user

    
class LoginForm(forms.Form):
    """ログイン用のフォーム"""
    # fields
    email = forms.EmailField(label='メールアドレス')
    password = forms.CharField(
        label='パスワード',
        min_length=8,
        widget=forms.PasswordInput(),
        help_text=password_validation.password_validators_help_text_html(),
    )
    # error messages
    error_messages = {
        'invalid_login': "メールアドレスまたはパスワードに誤りがあります",
        'inactive': _("This account is inactive"),
    }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = kwargs.get('request')
        self.user_cash = None
        # wiget style settings
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        
    def clean_password(self):
        """パスワード単体のバリデーション"""
        password = self.cleaned_data['password']
        validate_password(password)
        
        return password
    
    def clean(self):
        """認証関係のバリデーション。"""
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email is not None and password:
            self.user_cache = authenticate(self.request, email=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    # params={"email": self.email_field.verbose_name}
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data
    
    def confirm_login_allowed(self, user):
        """ユーザがアクティブかチェック"""
        if not user.is_active:
            raise forms.ValidationError(self.error_messages["inactive"], code='inactive')

    def get_user_id(self):
        """キャッシュの確認と設定"""
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache
        