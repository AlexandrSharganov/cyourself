from django.urls import path

from .views import personal_page, edit_profile, list_follow, create_follow, delete_follow


app_name = 'personal'

urlpatterns = [
    path('<int:pk>/', personal_page, name='personal'),
    path('<int:pk>/edit/', edit_profile, name='edit_profile'),
    path('follows/', list_follow, name='list_follow'),
    path('create_follow/<int:pk>/', create_follow, name='create_follow'),
    path('delete_follow/<int:pk>/', delete_follow, name='delete_follow'),
    
]
