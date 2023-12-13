from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import Denunciante

# Create your views here.
def index(request):
    return render(request, "index.html")


def lista(request):
    denunciantes = Denunciante.objects.all()
    return render(request, "lista.html", {"denunciantes": denunciantes})


def detail(request, denunciante_id):
    denunciante = get_object_or_404(Denunciante, pk=denunciante_id)

    return render(request, "detail.html", {"denunciante": denunciante})


def forms(request):
    return render(request, "forms.html", {})


def forms_post(request):
    novo_denunciante = Denunciante(nome=request.POST["nome"], email=request.POST["email"], cpf=request.POST["cpf"])
    novo_denunciante.save()

    return HttpResponseRedirect(reverse(lista))