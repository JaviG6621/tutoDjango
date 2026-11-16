from django.shortcuts import render
from django.http import HttpResponse

def mi_vista(request):
    return HttpResponse("Respuesta")

def mi_vista(request):
    return render(request, 'mi_plantilla.html', {'nombre': 'usuario'})

# Create your views here.
