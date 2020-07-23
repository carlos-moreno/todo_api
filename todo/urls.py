from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from todo.account.views import UserViewSet
from todo.core.views import TodoViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('todos', TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('get_token/', TokenObtainPairView.as_view(), name='get_token'),
    path('refresh_token/', TokenRefreshView.as_view(), name='refresh_token'),
]
