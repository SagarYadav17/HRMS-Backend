# Django
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

# Models & Serializers
from users.models import User, Profile

from users.serializers import UserSerializer, ProfileSerializer

# Customs
from core.utils import get_object_or_error
from users.utils import generate_password


class RegisterUserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# TODO: Check ListAPIView & RetrieveUpdateAPIView together
class ProfileAPIView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UpdateProfileAPIView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = "user_id"


class ForgetPasswordAPIView(APIView):
    def post(self, request, user_id):
        user = get_object_or_error(User, user_id=user_id)
        password = generate_password()
        user.set_password(password)
        user.save()
        return Response({"message": "Password has been reset successfully."})
