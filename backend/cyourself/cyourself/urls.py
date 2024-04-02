from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from .views import start_page_redirect


urlpatterns = [
    path('', start_page_redirect),
    path('auth/', include('users.urls', namespace='users')),
    path('admin/', admin.site.urls),
    path('dashboard.', include('dashboard.urls', namespace='dashboard')),
    path('personal/', include('personal.urls', namespace='personal')),
    path('posts/', include('posts.urls', namespace='posts')),
    path("__debug__/", include("debug_toolbar.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )