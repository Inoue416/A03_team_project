"""
Tests for auth forms. 
"""
from django.test import TestCase

from accounts.forms import (
    SignupForm,
    LoginForm,
)

# TODO:パスワード変更のForm作成

defaults_data = {
    'email': 'test@example.com',
    'password': 'Tuser!23',
}

class TestSingupForm(TestCase):
    """サインアップのフォームのテスト"""
    
    def test_signup_with_vailid_value(self):
        """通常の入力のサインアップのバリデーション"""
        email= defaults_data['email']
        password = defaults_data['password']
        form = SignupForm(data={
            'email': email,
            'password1': password,
            'password2': password,
        })
        
        self.assertTrue(form.is_valid())
        
    def test_signup_with_invalid_email(self):
        """Invalidなメールアドレスに対するバリデーションのテスト"""
        email = 'invalid'
        password = defaults_data['password']
        form = SignupForm(data={
            'email': email,
            'password1': password,
            'password2': password,
        })
        
        self.assertFalse(form.is_valid())
    
    def test_signup_with_invalid_password(self):
        """Invalidなパスワードに対するバリデーションのテスト"""
        email = defaults_data['email']
        password = 'password'
        form = SignupForm(data={
            'email': email,
            'password1': password,
            'password2': password,
        })
        
        self.assertFalse(form.is_valid())
        
    def test_signup_with_different_passwords(self):
        """パスワードと確認用のパスワードが違う場合のテスト"""
        email = defaults_data['email']
        password1 = defaults_data['password']
        password2 = 'different'
        form = SignupForm(data={
            'email': email,
            'password1': password1,
            'password2': password2
        })
        
        self.assertFalse(form.is_valid())
    
    

class TestLoginForm(TestCase):
    """ログインのフォームのテスト"""
    
    def test_valid_value(self):
        """通常の入力のログインに対するバリデーションのテスト"""
        email = defaults_data['email']
        password = defaults_data['password']
        
        form = LoginForm(data={
            'email':email,
            'password': password
        })
        
        self.assertTrue(form.is_valid())
    
    def test_log_in_with_wrong_email(self):
        """Invalidなメールアドレスでのログインに対するバリデーションのテスト"""
        email = 'invalid'
        password = defaults_data['password']
        
        form = LoginForm(data={
            'email':email,
            'password': password
        })
        
        self.assertFalse(form.is_valid())
    
    def test_log_in_with_Invalid_password(self):
        """Invalidパスワードでのログインに対するバリデーションのテスト"""
        email = defaults_data['email']
        password = 'password'
        
        form = LoginForm(data={
            'email':email,
            'password': password
        })
        
        self.assertFalse(form.is_valid())
    