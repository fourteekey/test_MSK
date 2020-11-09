from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# from api.views import index_view              # VUE or another JS frontend


schema_view = get_schema_view(
    openapi.Info(
        title="T900 WEB API",
        default_version='v1',
    ),
    url=settings.API_URL
)
urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # http://127.0.0.1:8000/
    # re_path('^.*$', index_view, name='index'),

    # API VIEWS
    # http://127.0.0.1:8000/api/v1/<router-viewsets>
    path('api/v1/', include('api.api')),

    # Django Admin
    # http://127.0.0.1:8000/api/admin/
    # path('api/admin/', admin.site.urls),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
