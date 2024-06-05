from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

from .views import (
    Login, Logout,
    Account,
    Signup,
    PasswordChange,
    PasswordSend,
    PasswordReset
)

app_name = 'account'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('<int:pk>/', Account.as_view(), name='profile'),
    path('signup', Signup.as_view(), name='signup'),
    path('password/change/', PasswordChange.as_view(), name='password_change'),
    path('password/send/', PasswordSend.as_view(), name='password_send'),
    path('password/reset/<uidb64>/<token>/', PasswordReset.as_view(), name='password_reset'),
]
