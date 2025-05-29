from django.db import models
from endereco.models import EnderecoM

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    cnh = models.CharField(max_length=20, unique=True)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    data_nascimento = models.DateField()
    endereco = models.ForeignKey(EnderecoM, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nome']

    def __str__(self):
        return self.nome
