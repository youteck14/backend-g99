from django.db import models
#contrib > contributions
#auth_user se encuentra en la aplicacion de auth
#AbstractBaseUser > me permite total control sobre la tabla 'auth_user'
#AbstractUser > me permite control solamente en la columnas de nombre, apellido, correo y password de la tabla 'auth_user'
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .authManage import UsuarioManager
# Create your models here.

class PlatoModel(models.Model):
    id = models.AutoField(primary_key=True, null= False, unique=True)
    nombre = models.CharField(max_length=50, null= False)
    precio  = models.FloatField(null=False)
    disponibilidad = models.BooleanField(default=True)
    #auto_now_add > datetime y sirve para indicar que se guarde la hora y fecha actual del servidor cuando se cree un nuevo registro
    fechaCreacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'platos'
        #ordenar por el precio descendiente
        ordering = ['-precio']

class UsuarioModel(AbstractBaseUser, PermissionsMixin):
    #PermissionMixin > me sirve para poder modificar los permisos que tendra este usuario al momento de crearse por los comandos (python manage.py createsuperuser)
    id = models.AutoField(primary_key=True, unique= True)
    nombre = models.CharField(max_length=50, null= False)
    apellido = models.CharField(max_length=50, null=False)
    correo = models.EmailField(max_length=50, unique=True, null=False)
    password = models.TextField(null=False)
    tipoUsuario = models.CharField(max_length=40, choices=[('ADMIN', 'ADMIN'), ('USER', 'USER')],
    db_column='tipo_usuario')

    #utilizamos los siguiente atributos si queremos seguir trabajando con el panel administrativo
    is_staff = models.BooleanField(default=False)
    # is_active > para saber si sigue activo trabajando en la empresa
    is_active = models.BooleanField(default= True)

    createAt = models.DateTimeField(auto_now_add = True,
    db_column='created_at')

    objects = UsuarioManager()

    #sera el campo que pedira el panel administrativo para autorizar al usuario, tiene que ser una columna que sea 'unique'
    USERNAME_FIELD = 'correo'

    #las columnas o campos requeridos al momento de crear el usuario por la terminal, osea seran los datos solicitados, no tiene que ir el USERNAME_FIELD puesto que este ya esta implicitamente colocado
    #Tampoco va la contraseña porque sea ya es por defecto
    REQUIRED_FIELDS = ['nombre', 'apellido', 'tipoUsuario']

    class Meta:
        db_table = 'usuarios'
