from django.urls import path
from core.views import DepartmentListAPIView, DesignationListAPIView

urlpatterns = [
    path("departments/", DepartmentListAPIView.as_view(), name="core_department"),
    path("designations/", DesignationListAPIView.as_view(), name="core_designation"),
]
