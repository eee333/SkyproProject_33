from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from rest_framework import serializers


from core.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        # exclude = ["password"]


class UserCrateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def validate(self, attr: dict):
        password: str = attr.get("password")
        password_repeat: str = attr.pop("password_repeat", None)
        if password != password_repeat:
            raise ValidationError("password adn password_repeat are not equal")
        return attr

    def create(self, validated_data):
        user = super().create(validated_data)

        user.set_password(user.password)
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def save(self):
        if password := self.validated_data.get('password'):
            self.validated_data['password'] = make_password(password)
        return super().save()


class UserUpdatePassSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def save(self):
        if password := self.validated_data.get('password'):
            self.validated_data['password'] = make_password(password)
        return super().save()