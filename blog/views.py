from rest_framework.permissions import IsAuthenticated

from blog.models import Post
from django.contrib.auth.models import User
from rest_framework import viewsets
from blog.serializers import UserSerializer, PostSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
