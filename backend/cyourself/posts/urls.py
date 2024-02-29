from django.urls import path

from .views import (
    post_create,
    post_delete,
    post_edit,
    post_detail,
    comments_create,
    like_post,
    news,
    storage,
    add_to_storage,
    delete_from_storage
)


app_name = 'posts'

urlpatterns = [
    path('storage/', storage, name='storage'),
    path('add_to_storage/<int:pk>/', add_to_storage, name='add_to_storage'),
    path('delete_from_storage/<int:pk>/', delete_from_storage, name='delete_from_storage'),
    path('news/', news, name='news'),
    path('create/', post_create, name='post_create'),
    path('delete/<int:pk>/', post_delete, name='post_delete'),
    path('edit/<int:pk>/', post_edit, name='post_edit'),
    path('detail/<int:pk>/', post_detail, name='post_detail'),
    path('comments_create/<int:pk>/', comments_create, name='comments_create'),
    path('like/<int:pk>/', like_post, name='like_create'),
]
