from django.urls import path

from . import views

urlpatterns = [
    path('create_report', views.CreateReport.as_view()),
    path('get_or_update_report/<slug>', views.GetOrUpdateReport.as_view()),
    path('list_report', views.ListReport.as_view()),
]
