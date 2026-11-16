from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.view.generic import TemplateView, DetailView, ListView
from .models import Usuario
import datetime

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = "Usuario"
        return context

class IndexVie(DetailView):
    model = Usuario
    template_name = "index.html"
    slug_field = 'username'
    context_object_name = 'usuario'

class IndexVi(ListView):
    model = Usuario
    template_name = "index.html"
    context_object_name = "usuarios"
    queryset = Usuario.object.filter(age__lt = 18)

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

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>La hora es %s</body></html>" %now
    return HttpResponse(html)

# Create your views here.
