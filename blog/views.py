from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.serializers import UserSerializer


# Create your views here.
class UserAPIView(APIView):
    queryset = User.objects.all()

    def get_queryset(self):
        return User.objects.all()

    def get(self, request):
        users = self.get_queryset()
        serializer = UserSerializer(users, many=True, context={'request': request})
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
