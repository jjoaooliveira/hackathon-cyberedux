from django.db import models

# Create your models here.

class Denunciante(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=30)

class Endereco(models.Model):
    endereco = models.CharField(max_length=200)
    cep = models.CharField(max_length=8)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

class Instituicao(models.Model):
    nome = models.CharField(max_length=100)
    contato = models.CharField(max_length=50)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

class Colaborador(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)

class Instituicao_Contem_Categoria(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Chamado(models.Model):
    descricao = models.CharField(max_length=200)
    data_abertura = models.DateField()
    problema = models.CharField(max_length=200)
    situacao = models.CharField(max_length=200)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    denunciante = models.ForeignKey(Denunciante, on_delete=models.CASCADE)

class Colaborador_Chamado(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    chamado = models.ForeignKey(Chamado, on_delete=models.CASCADE)
