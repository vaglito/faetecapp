from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

from .managers import UserManager

# Create your models here.

def folder_image(instance, filename):
    return "avatars/{0}/{1}".format(
        instance.email,
        filename
    )

class User(AbstractBaseUser, PermissionsMixin):
    """
    Definicion del modelo User
    """
    name = models.CharField("Nombres", max_length=100)
    last_name = models.CharField("Apellidos", max_length=100)
    email = models.EmailField("Email", unique=True)
    avatar = models.ImageField(upload_to=folder_image, blank=True)
    phone = models.IntegerField("Numero")
    is_active = models.BooleanField("¿Activo?", default=True)
    is_staff = models.BooleanField("Staff", default=False)
    is_superuser = models.BooleanField("Super User", default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        'name',
        'last_name',
        'phone'
    ]

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Usuarios'
    
    def __str__(self):
        return self.email

