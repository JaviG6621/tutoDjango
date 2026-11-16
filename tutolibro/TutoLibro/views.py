from django.shortcuts import render
from django.http import HttpResponse

def mi_vista(request):
    return HttpResponse("Respuesta")

# Create your views here.
