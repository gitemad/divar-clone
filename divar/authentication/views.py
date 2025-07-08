from rest_framework.generics import CreateAPIView
from .models import User
from .serializers import UserCreateSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def post(self, request, *args, **kwargs):
        # TODO: either fix except block or override create method of user manager
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')
        try:
            User.objects.create_user(
                phone_number,
                password,
            )
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)