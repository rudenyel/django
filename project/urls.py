from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors/', include('authors.urls', namespace='authors')),
    path('books/', include('books.urls', namespace='books')),
    path('', include('home.urls', namespace='home')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # noqa
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # noqa
