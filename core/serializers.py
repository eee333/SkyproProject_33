from rest_framework import serializers
from core.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ["password"]


class UserCrateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
