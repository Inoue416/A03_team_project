"""
Tests for auth forms. 
"""
from django.test import TestCase

from accounts.forms import (
    SignupForm,
)
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
