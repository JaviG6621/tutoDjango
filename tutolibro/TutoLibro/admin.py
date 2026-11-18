from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Project, Persona, Perfil, Developer

# Registramos Project y Persona de forma estándar
admin.site.register(Project)
admin.site.register(Persona)
admin.site.register(Perfil)
admin.site.register(Developer)

# Registramos nuestro modelo de usuario personalizado usando el UserAdmin del libro
@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):
    # Aquí puedes personalizar cómo se ve el usuario en el admin más adelante si el libro te lo pide
    pass