from django.urls import path, include
from rest_framework import routers

from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from blog.views import UserViewSet, PostViewSet

# Routers
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)

# API DOCS CONFIGURATION

# BUG FIX:
# pip install --upgrade setuptools
# pip install --upgrade distribute

schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version='v1',
        description="Post Description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="iamsolijonovasadbek@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# new
urlpatterns = [
    path('', include(router.urls)),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
