from django.urls import path
from tools.views import list_view, upload, botfarm, botfarm_favorites, botfarm_reviews

app_name = 'tools'

urlpatterns = [
    path('', list_view, name='list'),
    path('upload/', upload, name='upload'),
    path('botfarm/', botfarm, name='botfarm'),
    path('botfarm/favorites', botfarm_favorites, name='favorites'),
    path('botfarm/reviews', botfarm_reviews, name='reviews'),
]
