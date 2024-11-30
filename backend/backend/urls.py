from django.contrib import admin
from django.urls import path, include
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg.openapi import Info

view = get_schema_view(
    Info("RND Soft API", "v1"), public=True, permission_classes=[AllowAny]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/docs', view.with_ui('swagger')),
]
