from django.urls import path, include
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView

from accounts.views import SignUpView, LoginView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='index.html'), name='logout'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change_done/', PasswordChangeDoneView.as_view(), name='password_change_done')
]
