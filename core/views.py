# Django
from rest_framework.generics import ListAPIView

# Models & Serializers
from core.models import Department, Designation

from core.serializers import DepartmentSerializer, DesignationSerializer


class DepartmentListAPIView(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    pagination_class = None


class DesignationListAPIView(ListAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    pagination_class = None
