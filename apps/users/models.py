
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):
    def _create_user(self, username, email, name,last_name, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            name = name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, name,last_name, password=None, **extra_fields):
        return self._create_user(username, email, name,last_name, password, False, False, **extra_fields)

    def create_superuser(self, username, email, name,last_name, password=None, **extra_fields):
        return self._create_user(username, email, name,last_name, password, True, True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField('User Id', unique = True, primary_key=True)
    dni = models.CharField('users DNI',max_length = 9,null=True, blank=True,unique=True)
    username = models.CharField(max_length = 50, unique = True)
    email = models.EmailField('Correo Electrónico',max_length = 255,)
    name = models.CharField('Nombres', max_length = 30, blank = True, null = True)
    last_name = models.CharField('Apellidos', max_length = 50, blank = True, null = True)
    imagePfp = models.ImageField('Imagen de perfil', upload_to='static/usersPfp/', null=True, blank = True)
    fechaNac = models.CharField("Fecha de nacimiento", max_length=30,null=True, blank=True)
    direccion = models.CharField("Fecha de nacimiento", max_length=30,null=True, blank=True)
    descripcion = models.CharField("Bio/Descripcion", max_length=255,null=True, blank=True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_mod = models.BooleanField(default = False)
  
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','name','last_name','rol']

    def __str__(self):
        return f'{self.name} {self.last_name}'
