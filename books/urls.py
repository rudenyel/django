from django.urls import path
from books.views import (
    list_view,
    detail_view
)

app_name = 'books'

urlpatterns = [
    path('', list_view, name='list'),
    path('<slug:slug>', detail_view, name="detail"),
]
