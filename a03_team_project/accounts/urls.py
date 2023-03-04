from django.urls import path, re_path

from accounts.views import SignUpView, LoginView, CustomLogoutView, CustomPasswordChangeView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    # HACK:しっかりした正規表現に書き換えて
    re_path(r'[login/]+', LoginView.as_view(), name='login'),
    # path('login/', LoginView.as_view(), name='login'),
]
