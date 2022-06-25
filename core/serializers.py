# Django
from rest_framework.serializers import ModelSerializer

# Models
from core.models import Department, Designation


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class DesignationSerializer(ModelSerializer):
    class Meta:
        model = Designation
        fields = "__all__"
