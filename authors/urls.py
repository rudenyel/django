from django.urls import path
from authors.views import (
    list_view,
    detail_view,
)

app_name = 'authors'

urlpatterns = [
    path('', list_view, name="list"),
    path('<slug:slug>', detail_view, name="detail"),
]
