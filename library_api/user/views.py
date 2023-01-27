from rest_framework import viewsets
from user.serializer import UserSerializer
from user.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
