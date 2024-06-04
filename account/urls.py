from django.contrib.auth.models import User
from django.urls import path, reverse_lazy
from django.contrib.auth.views import (
    LoginView, LogoutView,
    PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView
)

from .views import (
    ProfileView, ProfileUpdateView, ProfileUpdateDoneView,
    SignupView, WelcomeView
)

app_name = 'account'

urlpatterns = [
    # path('', profile_view, name='profile'),
    # path('login/', login_view, name="login"),

    path('', ProfileView.as_view(), name='profile'),
    path('update/<int:pk>/', ProfileUpdateView.as_view(), name='update'),
    path('update/done/', ProfileUpdateDoneView.as_view(), name='updated'),

    path('signup', SignupView.as_view(), name='signup'),
    path('welcome', WelcomeView.as_view(), name='welcome'),


    # https://github.com/django/django/blob/stable/4.2.x/django/contrib/auth/views.py

    # login, logout
    # registration/login.html (or LOGIN_REDIRECT_URL = 'account:profile')
    path('login/', LoginView.as_view(
        next_page=reverse_lazy('account:profile')), name='login'),
    # registration/logged_out.html, replaced account:profile
    path('logout/', LogoutView.as_view(
        next_page=reverse_lazy('home:about')), name='logout'),

    # password change
    # registration/password_change_form.html
    path('password/change/', PasswordChangeView.as_view(
        success_url=reverse_lazy('account:changed')), name='change'),
    # registration/password_change_done.html
    path('password/change/done', PasswordChangeDoneView.as_view(), name='changed'),

    # password reset
    # registration/password_reset_form.html
    # registration/password_reset_email.html
    path('password/reset/', PasswordResetView.as_view(
        success_url=reverse_lazy('account:emailed')), name='reset'),
    # registration/password_reset_done.html
    path('password/reset/done/', PasswordResetDoneView.as_view(), name='emailed'),
    # registration/password_reset_confirm.html
    path('password/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('account:complete')), name='confirm'),
    # registration/password_reset_complete.html
    path('password/reset/complete/', PasswordResetCompleteView.as_view(), name='complete'),

]
