from django.shortcuts import render
from rest_framework.views import APIView
from .models import Scan
from .serializers import UserSerializer, ScanSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

class ScanViewSet(viewsets.ModelViewSet):
    serializer_class = ScanSerializer
    # permission_classes=[permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,]

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Scan.objects.filter(user = self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,]
    queryset = User.objects.all()
