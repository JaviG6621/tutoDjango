import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nombre"] = "Usuario"
        return context


def home(request):
    return render(request, "application/home.html")


def about(request):
    return render(request, "application/about.html")


def contact(request):
    return render(request, "application/contact.html")


def current_datetime(request):
    now = datetime.datetime.now()
    html = f"<html><body>La hora es {now}</body></html>"
    return HttpResponse(html)

# Create your views here.
