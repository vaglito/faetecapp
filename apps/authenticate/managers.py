from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    """
    * Administrador de modelo de usuario personalizado donde el correo electrónico son los identificadores únicos
    para la autenticación en lugar de nombres de usuario.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Cree y guarde un usuario con el correo electrónico y la contraseña proporcionados.
        """
        if not email:
            raise ValueError(_("El correo debe estar configurado"))
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        """
        Cree y guarde un Superusuario con el email y la contraseña.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("El Superusuario debe tener is_staff=True"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("El Superusuario debe tener is_superuser=True"))
        return self.create_user(email, password, **extra_fields)
        