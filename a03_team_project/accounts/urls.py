from django.urls import path, include
from django.contrib.auth.views import LogoutView

from accounts.views import SignUpView, LoginView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='index.html'), name='logout'),
]
