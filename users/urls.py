from django.urls import path

from . import views

urlpatterns = [
    path('users', views.CreateUser.as_view()),
    path('list_user', views.ListUser.as_view()),
    path('get_or_update_user/<pk>', views.GetOrUpdateUser.as_view()),
]
