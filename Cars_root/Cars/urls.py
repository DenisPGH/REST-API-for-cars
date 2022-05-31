from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.schemas import get_schema_view as gsv


schema_view = get_schema_view(
   openapi.Info(
      title="API Cars_root",
      default_version='v1',
      description="API-cars-view-scheme. You can check all methods(request and response)"
                  ", if they work properly.",
   ),
   public=True,
   permission_classes=(
                       permissions.IsAuthenticated,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Cars.users_app.urls'),name='users'),
    path('info/',include('Cars.cars_rest.urls'),name='restpart'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('my-schema/',gsv(title='API-cars',description="API-cars schema swagger"),name='denis schema')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

