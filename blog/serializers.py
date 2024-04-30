from django.contrib.auth.models import User
from rest_framework import serializers

from blog.models import Post


# new
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff', 'is_active', 'is_superuser']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created', 'updated', 'is_published']