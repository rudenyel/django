from django.urls import path
from home.views import (
    about
)

app_name = 'home'

urlpatterns = [
    path('', about, name="about"),
]
