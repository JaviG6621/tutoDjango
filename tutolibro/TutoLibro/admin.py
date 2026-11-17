from django.contrib import admin
from .models import Project, Persona, User

# Registramos tus modelos para que aparezcan en la web de administración
admin.site.register(Project)
admin.site.register(Persona)
admin.site.register(User)  # Si también quieres ver tu modelo de usuario personalizado
