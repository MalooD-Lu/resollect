from django.urls import path
from .views import get_users, get_user_by_id, create_user, update_user, delete_user

urlpatterns = [
    path('api/users/', get_users, name='user-list'),
    path('api/users/<int:user_id>/', get_user_by_id, name='user-detail'),
    path('api/users/create/', create_user, name='user-create'),
    path('api/users/<int:user_id>/update/', update_user, name='user-update'),
    path('api/users/<int:user_id>/delete/', delete_user, name='user-delete'),
]
