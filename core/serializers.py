from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers


from core.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        read_only_fields = ("id",)
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
        )


class UserCrateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password_repeat = serializers.CharField(write_only=True)

    class Meta:
        model = User
        read_only_fields = ("id",)
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "password_repeat",
        )

    def validate(self, attrs: dict):
        password: str = attrs.get("password")
        password_repeat: str = attrs.pop("password_repeat", None)
        if password != password_repeat:
            raise ValidationError("password and password_repeat are not equal")
        return attrs

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
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = User
        read_only_fields = ("id",)
        fields = (
            "old_password",
            "new_password",
        )

    def validate(self, attrs: dict):
        old_password: str = attrs.get("old_password")
        user: User = self.instance
        if not user.check_password(old_password):
            raise ValidationError("old_password is incorrect")
        return attrs

    def update(self, instance: User, validated_data):
        instance.set_password(validated_data["new_password"])
        instance.save(update_fields=["password"])
        return instance


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs: dict):
        username: str = attrs.get("username")
        password: str = attrs.get("password")
        user = authenticate(username=username, password=password)
        if not user:
            raise ValidationError("username or password is incorrect")
        attrs["user"] = user
        return attrs


