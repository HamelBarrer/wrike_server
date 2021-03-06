from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from users.views import CustomToken

urlpatterns = [
    path('auth-token/', CustomToken.as_view()),
    path('api/v1/', include('users.urls')),
    path('api/v1/', include('profiles.urls')),
    path('api/v1/', include('reports.urls')),
    path('api/v1/', include('projects.urls')),
    path('admin/', admin.site.urls),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT,
)
