from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from user.serializer import UserSerializer

class CreateUserView(CreateAPIView):
    model = get_user_model()
    serializer_class = UserSerializer