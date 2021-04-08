from django.urls import path

from . import views

urlpatterns = [
    path('project/<slug>', views.GetOrUpdateProject.as_view()),
    path('projects', views.ListProject.as_view()),
    path('create-project', views.CreateProject.as_view()),
]
