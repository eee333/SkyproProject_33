from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers


from core.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        # exclude = ["password"]


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
            raise ValidationError(f"password adn password_repeat are not equal:{password_repeat}")
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
    class Meta:
        model = User
        fields = '__all__'

    def save(self):
        if password := self.validated_data.get('password'):
            self.validated_data['password'] = make_password(password)
        return super().save()
