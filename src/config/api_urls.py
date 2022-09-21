from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(title='Always data API', default_version='v0', description='Routes of Always data project'),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('auth/', include(('apps.users.urls.auth', 'auth'))),
    path('users/', include(('apps.users.urls.users_urls', 'users'))),

    path('swagger(<str:format>.json|.yaml)/', schema_view.without_ui(), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger'), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc'), name='schema-redoc'),
]
