from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from core.models import User
from core.serializers import UserSerializer, UserCrateSerializer, \
    UserUpdateSerializer, UserUpdatePassSerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCrateSerializer


class UserLoginView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserCrateSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserUpdatePassView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdatePassSerializer


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
