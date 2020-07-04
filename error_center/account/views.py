from django.contrib.auth.models import Group
from rest_framework import viewsets

from .models import User
from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """Make doc here"""
    queryset = User.objects.all().order_by('date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """Make doc here"""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
