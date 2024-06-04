# https://ccbv.co.uk/projects/Django/4.2/
# https://docs.djangoproject.com/en/4.2/topics/class-based-views/
# https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/
# https://github.com/django/django/blob/stable/4.2.x/django/views/generic/edit.py

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .forms import SignUpForm


class ProfileView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('account:login')
    template_name = 'account/profile.html'


class SignupView(CreateView, PasswordResetView):
    form_class = SignUpForm  # UserCreationForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('account:profile')
    success_message = "Your profile was created successfully"


class WelcomeView(TemplateView):
    template_name = 'account/welcome.html'


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
