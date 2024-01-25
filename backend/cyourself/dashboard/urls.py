from django.urls import path, include

from .views import dash

app_name = 'dashboard'

urlpatterns = [
    path('', dash, name='dash'),
    # path('accounts/', include('django.contrib.auth.urls')),
]
