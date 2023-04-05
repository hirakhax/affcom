from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(
        self,
        username,
        email=None,
        password=None,
        **kwargs,
    ):
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("User must have a password")

        email = self.normalize_email(email=email)
        user = self.model(username=username, email=email, **kwargs)
        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None):
        return self.create_user(
            username=username,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True,
        )


class User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "username"

    objects = UserManager()

    def __str__(self):
        return str(self.username)
