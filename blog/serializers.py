from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.relations import HyperlinkedIdentityField


# new
class UserSerializer(serializers.HyperlinkedModelSerializer):
    user_detail_url = HyperlinkedIdentityField(
        view_name='user-detail',
        lookup_field='id'
    )

    class Meta:
        model = User
        fields = '__all__'
