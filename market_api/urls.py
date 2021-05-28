# django
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from market import views
from rest_framework import routers, permissions

# swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# router
router = routers.DefaultRouter()
router.register(r"products", views.ProductViewSet)

# url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include("rest_framework.urls", namespace="rest_framework")),
]

# api-docs
schema_url_patterns = [ path('', include(router.urls)), ]

schema_view = get_schema_view(
    openapi.Info(
        title="Django API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
    ),
    public=True, 
    permission_classes=(permissions.AllowAny,), 
    patterns=schema_url_patterns,

)


if settings.DEBUG:
    urlpatterns = [
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]