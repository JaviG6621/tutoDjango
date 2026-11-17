from django.db import models
import uuid  # <-- Necesario para el UUIDField

class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/")  # Recomendado: especificar carpeta de subida
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Persona(models.Model):
    # ¡Ojo! Si defines una PK como UUID, normalmente querrás que se genere sola:
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # max_length=3 es muy poco para un nombre (ej. "Ana" cabe, pero "Alejandro" no). Lo subimos a 50.
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"