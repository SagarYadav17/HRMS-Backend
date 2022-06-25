# Django
from rest_framework.serializers import ModelSerializer

# Models & Serializers
from users.models import User, Profile

from core.serializers import DepartmentSerializer, DesignationSerializer

# Customs
from users.utils import generate_password


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ("password",)

    def create(self, validated_data):
        password = generate_password()
        validated_data["password"] = password
        return super().create(validated_data)


class ProfileSerializer(ModelSerializer):
    user = UserSerializer("user")
    department = DepartmentSerializer("department")
    designation = DesignationSerializer("designation")

    class Meta:
        model = Profile
        fields = "__all__"
