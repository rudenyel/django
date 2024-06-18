from django.urls import path
from reviews.views import (
    create_view,
)

app_name = 'reviews'

urlpatterns = [
    path('<slug:slug>/create', create_view, name="create"),
]
