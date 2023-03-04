from django.urls import path

from accounts.views import SignUpView, LoginView, CustomLogoutView, CustomPasswordChangeView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
]
