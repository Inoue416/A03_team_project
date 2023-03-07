# """
# 認証関係のViewのテスト
# """
# from django.test import TestCase, Client
# from django.contrib.auth import get_user, get_user_model
# from django.urls import reverse

# # from auth.views import (
    
# # )

# SIGNUP_URL = reverse('accounts:signup')
# LOGIN_URL = reverse('accounts:login')

# class TestPublicAuthentication(TestCase):
#     """Authentication関係のテスト（パブリック）"""
    
#     def setUp(self):
#         self.client = Client()
#         self.name = 'Test Name'
#         self.email = 'user@exmaple.com'
#         self.password = 'UserPass@123'
    
#     def test_signup_page_url(self):
#         res = self.client.get('/accout/signup')
#         self.assertEqual(res.status_code, 200)
#         self.assertTemplateUsed(res, template_name='signup.html')
    
#     def test_signup_successful(self):
#         """サインアップ通常パターン"""
#         payload = {
#             'name': self.name,
#             'email': self.email,
#             'password1': self.password,
#             'password2': self.password,
#             'chocice': '生徒'
#         }
#         res = self.client.post(SIGNUP_URL, payload)
        
#         self.assertEqual(res.status_code, 200)
#         users = get_user_model().objects.all()
#         self.assertEqual(users.count(), 1)
        
#     def test_login_page_url(self):
#         payload = {
#             'email': self.email,
#             'password': self.password,
#         }
#         res = self.client.post(LOGIN_URL, payload)
        
# class TestPrivateAuthnetication(TestCase):
#     """Authentication関係のテスト（プライベート）"""
    
#     # TODO:パスワードの変更系のテストを作成
    
#     def setUp(self):
#         self.client = Client()
#         self.user = get_user_model().objects.create_user(
#             name='テスト太郎',
#             email='test@example.com',
#             password='test1234',
#             is_student=True,   
#         )
#         self.client.force_login(self.user)
        
#     def test_login_successful(self):
#         """ログイン通常パターン"""
#         payload = {
#             'email': self.user.email,
#             'password': self.user.password,
#         }
#         res = self.client.post(LOGIN_URL, payload)