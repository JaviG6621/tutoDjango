from django.shortcuts import render, HttpResponse
from django.http import HttpResponse

def mi_vista(request):
    return HttpResponse("Respuesta")

def mi_vista(request):
    return render(request, 'mi_plantilla.html', {'nombre': 'usuario'})

def home(request):
    return render(request, "application/home.html")

def about(request):
    return render(request, "application/about.html")

def contact(request):
    return render(request, "application/contact.html")

# Create your views here.
