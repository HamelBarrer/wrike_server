from django.urls import path

from . import views

urlpatterns = [
    path('profile/<slug>', views.GetPerfil.as_view()),
]
