import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .serializers import DeveloperSerializer
from .models import Developer
from rest_framework import generics
from rest_framework.response import Response


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

class DeveloperList(generics.ListCreateApiView):
    serializer_class = DeveloperSerializer
    queryset = Developer.objects.all()

class DeveloperDetail(generics.UpdateDestroyApiView):
    serializer_class = DeveloperSerializer
    def retrieve(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        object = Developer.objects.get(pk=kwargs['pk'])
        serializer = DeveloperSerializer(object)
        return Response(serializer.data)

# Create your views here.
