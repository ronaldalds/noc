from django.db import models
from .endereco_models import Cidade

class Cliente(models.Model):
    razao_social = models.CharField(max_length=128)
    nome = models.CharField(max_length=128)
    cnpj = models.CharField(max_length=128)
    logradouro = models.CharField(max_length=128)
    numero = models.CharField(max_length=128)
    bairro = models.CharField(max_length=128)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    cep = models.CharField(max_length=128)
    telefone = models.CharField(max_length=128)
    email = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = "Clientes"
    
    def __str__(self) -> str:
        return self.razao_social