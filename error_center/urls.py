from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from .account.views import UserViewSet
from .core.views import AgentViewSet, EventViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
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
    path('api/v1/', include(router.urls))
]
