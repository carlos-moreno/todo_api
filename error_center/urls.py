from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_swagger.views import get_swagger_view

from .core.views import AgentViewSet, EventViewSet

router = routers.DefaultRouter()
router.register('agents', AgentViewSet)
router.register('events', EventViewSet)

schema_url_patterns = [
    url('api/v1/', include(router.urls)),
]
schema_view = get_swagger_view(title='Error Center API', urlconf='error_center.urls',
                               patterns=schema_url_patterns, )

urlpatterns = [
    path('', schema_view),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('get_token', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
