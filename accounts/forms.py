from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    email = forms.EmailField()

    # https://github.com/django/django/blob/stable/4.2.x/django/contrib/auth/forms.py#L157
    # https://github.com/django/django/blob/stable/4.2.x/django/contrib/auth/forms.py#L92
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email already exists.")
        else:
            return email

    class Meta:
        model = User
        fields = ['username', 'email']
