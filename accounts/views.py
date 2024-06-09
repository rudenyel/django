# https://ccbv.co.uk/projects/Django/4.2/
# https://github.com/django/django/blob/stable/4.2.x/django/contrib/auth/views.py
# https://github.com/django/django/blob/stable/4.2.x/django/views/generic/edit.py

from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import (
    LoginView, LogoutView,
    PasswordChangeView,
    PasswordResetView,
    PasswordResetConfirmView,
)

from .forms import SignupForm
from .models import Profile


class Login(LoginView):
    template_name = 'accounts/login.html'
    success_message = "You have successfully logged in!"

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse_lazy('home:about')


class Logout(LogoutView):
    success_message = "You have successfully logged out!"

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse_lazy('home:about')


class Signup(CreateView):
    form_class = SignupForm
    template_name = 'accounts/signup.html'
    success_message = "Your account was created successfully!"

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse_lazy('account:login')


class Account(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ["first_name", "last_name", "phone", "address"]
    template_name = 'accounts/profile.html'
    success_message = "Your profile has been successfully updated!"

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse_lazy('account:profile', kwargs={'pk': self.object.pk})


class PasswordChange (LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_message = "Your password has been successfully changed."

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse_lazy('account:profile', kwargs={'pk': self.request.user.profile.id})


class PasswordSend (PasswordResetView):
    template_name = 'accounts/password_send.html'
    email_template_name = 'accounts/password_send_email.html'
    success_message = "We've emailed you instructions for setting your password."

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse_lazy('home:about')


class PasswordReset (PasswordResetConfirmView):
    template_name = 'accounts/password_reset.html'
    success_message = "Your password has been reset. You can log in now."

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse_lazy('account:login')

# @login_required
# def profile_view(request):
#     template_name = 'account/profile.html'
#     return render(request, template_name=template_name)


# def login_view(request):
#     template_name = 'account/forms/login_view.html'
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             user = authenticate(request,
#                                 username=data['username'],
#                                 password=data['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Authenticated successfully')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()
#     context = {'form': form}
#     return render(request, template_name=template_name, context=context)
