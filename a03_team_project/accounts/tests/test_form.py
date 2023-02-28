"""
Tests for auth forms. 
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

from accounts.forms import (
    SignupForm,
    LoginForm,
)

# TODO:パスワード変更のForm作成

test_data = {
    'name': 'Test Name',
    'email': 'test@example.com',
    'password': 'TestUser!23',
    'choice': '生徒'
}

class TestSingupForm(TestCase):
    """サインアップのフォームのテスト"""
    
    def test_signup_with_vailid_value(self):
        """通常の入力のサインアップのバリデーション"""
        form = SignupForm(data={
            'name': test_data['name'],
            'email': test_data['email'],
            'password1': test_data['password'],
            'password2': test_data['password'],
            'choice': test_data['choice']
        })
        
        self.assertTrue(form.is_valid())
        
    def test_signup_with_invalid_email(self):
        """Invalidなメールアドレスに対するバリデーションのテスト"""
        invalid_email = 'invalid'
        form = SignupForm(data={
            'name': test_data['name'],
            'email': invalid_email,
            'password1': test_data['password'],
            'password2': test_data['password'],
            'choice': '生徒',
        })
        
        self.assertFalse(form.is_valid())
    
    def test_signup_with_invalid_password(self):
        """Invalidなパスワードに対するバリデーションのテスト"""
        invalid_password = 'password'
        form = SignupForm(data={
            'name': test_data['name'],
            'email': test_data['email'],
            'password1': invalid_password,
            'password2': invalid_password,
            'choice': '生徒',
        })
        
        self.assertFalse(form.is_valid())
        
    def test_signup_with_different_passwords(self):
        """パスワードと確認用のパスワードが違う場合のテスト"""
        password2 = 'different'
        form = SignupForm(data={
            'name': test_data['name'],
            'email': test_data['email'],
            'password1': test_data['password'],
            'password2': password2,
            'choice': '生徒',
        })
        
        self.assertFalse(form.is_valid())
    
    

class TestLoginForm(TestCase):
    """ログインのフォームのテスト"""
    
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            name=test_data['name'],
            email=test_data['email'],
            password=test_data['password'],
            is_student=True,
        )
    
    def test_valid_value(self):
        """通常の入力のログインに対するバリデーションのテスト"""
        form = LoginForm(data={
            'email': self.user.email,
            'password': test_data['password'],
        })
        
        self.assertTrue(form.is_valid())
    
    def test_log_in_with_wrong_email(self):
        """Invalidなメールアドレスでのログインに対するバリデーションのテスト"""
        invalid_email = 'invalid'
        
        
        form = LoginForm(data={
            'email':invalid_email,
            'password': test_data['password']
        })
        
        self.assertFalse(form.is_valid())
    
    def test_log_in_with_Invalid_password(self):
        """Invalidパスワードでのログインに対するバリデーションのテスト"""
        invalid_password = 'password'
        
        form = LoginForm(data={
            'email':test_data['email'],
            'password': invalid_password
        })
        
        self.assertFalse(form.is_valid())

# class PasswordChangeFrom()