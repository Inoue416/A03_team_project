"""
User モデルのテスト
"""

from django.test import TestCase
from django.contrib.auth import get_user_model

class UserTest(TestCase):
    """User モデルのテスト"""
    
    # 成功パターン（２つ）
    
    def test_create_user_with_successful(self):
        """ユーザ作成の成功パターン（通常時）"""
        name = 'テスト太郎'
        email = 'test@example.com'
        password = 'test1234'
        
        user = get_user_model().objects.create_user(
            name=name,
            email=email,
            password=password,
            is_student=True,
        )
        
        self.assertEqual(user.name, name)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        
    def test_create_superuser(self):
        """スーパーユーザ作成のテスト"""
        user = get_user_model().objects.create_superuser(
            'テスト太郎',
            'test1234',
        )
        self.assertTrue(user.is_superuser)
    
    # 失敗パターン（５つ）
    
    def test_without_email_raise_error(self):
        """emailが入力されてない場合のテスト"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('テスト太郎', '', 'test1234')
    
    def test_without_password_raise_error(self):
        """パスワードが入力されていない場合のテスト"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('テスト太郎', 'test@example.com', '')
     
    def test_email_normalized(self):
        """不規則なEmailの場合に普通のフォーマットにしているかのテスト"""
        
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]
        
        email_counta = 1
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(f'テスト太郎{email_counta}', email, 'test1234', is_student=True)
            self.assertEqual(user.email, expected)
            email_counta += 1
        
    
    # HACK：関数名：roleがしっくりこない。（下の２つのテスト）
    
    def test_without_role_raise_error(self):
        """生徒でも、企業でもない場合のテスト"""
        # HACK:エラーは自作するべきかも。とりあえずのValueError
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('テスト太郎', 'test@example.com', 'test1234', is_student=False, is_company=False)
            
    def test_with_doble_role_raise_error(self):
        """生徒と会社、どっちものロールになっている場合のテスト"""
        # HACK:自作エラーを使うべきかも、とりあえずのValueError
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('テスト太郎', 'test@example.com', 'test1234', is_student=True, is_company=True)
            
    
    