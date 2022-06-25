from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

# Models
from core.models import Department, Designation


class UserManager(BaseUserManager):
    def create_user(self, username, password, email):
        """Create and return a `User` with an email, username and password."""
        user = self.model(username=username)
        if email:
            user.email = self.normalize_email(email)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, password, email):
        """
        Create and return a `User` with superuser powers.
        Superuser powers means that this use is an admin that can do anything
        they want.
        """

        user = self.create_user(username, password, email)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=128, unique=True)
    email = models.EmailField(null=True, max_length=128, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    usergroup = models.CharField(max_length=100)
    joining_date = models.DateTimeField(default=timezone.localtime)

    USERNAME_FIELD = "username"

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=128)
    phone_number = models.PositiveBigIntegerField()
    address = models.TextField()
    designation = models.ForeignKey(Designation, on_delete=models.PROTECT)
    assigned_departments = models.ManyToManyField(Department)

    def __str__(self):
        return self.full_name
