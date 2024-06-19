from django.urls import path
from favorites.views import list_view, toggle_view, ajax_toggle_view

app_name = 'favorites'

urlpatterns = [
    path('', list_view, name='list'),
    path('<slug:slug>', toggle_view, name="toggle"),
    path('<slug:slug>/ajax', ajax_toggle_view, name="ajax_toggle"),
]



