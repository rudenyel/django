from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls', namespace='account')),
    path('authors/', include('authors.urls', namespace='authors')),
    path('books/', include('books.urls', namespace='books')),
    path('favorites/', include('favorites.urls', namespace='favorites')),
    path('reviews/', include('reviews.urls', namespace='reviews')),
    path('tools/', include('tools.urls', namespace='tools')),
    path('', include('home.urls', namespace='home')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # noqa
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # noqa
    urlpatterns += path("__debug__/", include("debug_toolbar.urls")),
