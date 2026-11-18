from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import uuid

languages = (
	('python', 'PYTHON'),
	('c', 'C'),
	('java', 'JAVA'),
	('php', 'PHP')
)

# 1. Creamos el gestor personalizado para el email
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El campo Email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


# 2. Tu modelo User actualizado usando el gestor anterior
class User(AbstractUser):
    username = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Sin username ni password aquí

    # ¡ESTA LÍNEA ES LA CLAVE QUE FALTABA!
    objects = CustomUserManager()

class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Persona(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete = models.PROTECT)
    website = models.URLField(max_length = 200, blank = True)
    photo = models.ImageField(upload_to = 'users/pictures', blank = True, null = True)
    date_modified = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.user.username

class Developer(models.Model):
	nick = models.CharField(max_length = 16)
	first_name = models.CharField(max_length = 255)
	last_name = models.CharField(max_length = 255)
	email = models.EmailField()
	programming_language = models.CharField(max_length = 32, choices = languages)