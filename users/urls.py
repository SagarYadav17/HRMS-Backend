from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import RegisterUserView, ProfileAPIView, UpdateProfileAPIView, ForgetPasswordAPIView

urlpatterns = [
    path("auth/register/", RegisterUserView.as_view(), name="auth_register"),
    path("auth/login/", TokenObtainPairView.as_view(), name="auth_login"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="auth_refresh"),
    path("auth/profile/", ProfileAPIView.as_view(), name="auth_profile"),
    path("auth/profile/<int:user_id>/", UpdateProfileAPIView.as_view(), name="auth_profile_update"),
    path("auth/forget-password/<int:user_id>/", ForgetPasswordAPIView.as_view(), name="auth_forget_password"),
]
