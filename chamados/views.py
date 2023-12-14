import plotly.express as px
import plotly.offline as opy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db import connection
from datetime import date

from django.urls import reverse
from .models import Denunciante, Categoria, Chamado, Cidade 

# Create your views here.
def index(request):
    return render(request, "index.html")


def lista(request):
    chamados = Chamado.objects.all()
    return render(request, "lista.html", {"chamados": chamados})


def detail(request, chamado_id):
    chamado = get_object_or_404(Chamado, pk=chamado_id)
    
    return render(request, "detail.html", {"chamado": chamado})


def formsColaborador(request):
    return render(request, "forms_colaborador.html", {})

def formsUsuario(request):
    cidades = Cidade.objects.all()
    categorias = Categoria.objects.all()
    return render(request, "forms_usuario.html", {"cidades": cidades, "categorias": categorias})


def forms_post_usuario(request):
    data = date.today()
    novo_denunciante = Denunciante(
        nome=request.POST["nome"],
        email=request.POST["email"],
        cpf=request.POST["cpf"]
    )
    novo_denunciante.save()

    novo_chamado = Chamado(
        
    )
    return HttpResponseRedirect(reverse(index))

def forms_post_colaborador(request):
    data = date.today()
    novo_denunciante = Denunciante(
        nome=request.POST["nome"],
        email=request.POST["email"],
        cpf=request.POST["cpf"]
    )
    novo_denunciante.save()

    return HttpResponseRedirect(reverse(lista))


def relatorio(request):
    cursor = connection.cursor()
    cursor.execute('''
                   SELECT cc2.nome CIDADE, COUNT(*) TOTAL FROM chamados_chamado cc 
                    JOIN chamados_endereco ce ON ce.id = cc.endereco_id 
                    JOIN chamados_cidade cc2 on cc2.id = ce.cidade_id
                    GROUP BY CIDADE;
    ''')
    data = cursor.fetchall()

    x = [dados[0] for dados in data]
    y = [dados[1] for dados in data]

    #Criar um gráfico de linha com Plotly
    grafico_raw = px.bar(
        x=x,
        y=y,
        title='Denuncias/Cidade', 
        labels={'x': 'Cidades', 'y': 'Denuncias'},
        width=600,
        height=600
    )
    grafico = opy.plot(grafico_raw, output_type='div')
    
    return render(request, 'relatorio.html', {"grafico": grafico})

def login(request):
    return render(request, 'login.html')