from django.urls import path

from .views import personal_page, edit_profile


app_name = 'personal'

urlpatterns = [
    path('<int:pk>/', personal_page, name='personal'),
    path('<int:pk>/edit/', edit_profile, name='edit_profile'),
]
