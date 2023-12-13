from django.db import models

# Create your models here.

class Denunciante(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)

class Cidade(models.Model):
    cidade = models.CharField(max_length=100)

class Categoria(models.Model):
    nome = models.CharField(max_length=30)

class Endereco(models.Model):
    endereco = models.CharField(max_length=200)
    cep = models.CharField(max_length=8)
    cidade_id = models.ForeignKey(Cidade, on_delete=models.CASCADE)

class Instituicao(models.Model):
    nome = models.CharField(max_length=100)
    contato = models.CharField(max_length=50)
    endereco_id = models.ForeignKey(Endereco, on_delete=models.CASCADE)

class Colaborador(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)
    instituicao_id = models.ForeignKey(Instituicao, on_delete=models.CASCADE)

class Instituicao_Contem_Cateria(models.Model):
    instituicao_id = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Chamado(models.Model):
    descricao = models.CharField(max_length=200)
    data_abertura = models.DateTimeField('data_abertura')
    problema = models.CharField(max_length=200)
    situacao = models.CharField(max_length=200)
    endereco_id = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    colaborador_id = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    denunciante_id = models.ForeignKey(Denunciante, on_delete=models.CASCADE)

class Colaborador_Chamado(models.Model):
    colaborador_id = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    chamado_id = models.ForeignKey(Chamado, on_delete=models.CASCADE)
    
