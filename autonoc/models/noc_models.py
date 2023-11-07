from django.db import models
from .endereco_models import Cidade
from .conexao_models import Conexao
from django.core.exceptions import ValidationError
    
class Estacao(models.Model):
    nome = models.CharField(max_length=128)
    logradouro = models.CharField(max_length=128)
    numero = models.CharField(max_length=128)
    bairro = models.CharField(max_length=128)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Estações"
    
    def __str__(self) -> str:
        return self.nome

class Equipamento(models.Model):
    nome = models.CharField(max_length=128)
    modelo = models.CharField(max_length=128)
    ip = models.CharField(max_length=128)
    estacao = models.ForeignKey(Estacao, on_delete=models.PROTECT)
    rack = models.CharField(max_length=128, blank=True, null=True)
    fila = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Equipamentos"
    
    def __str__(self) -> str:
        return f"{self.nome} - {self.modelo}"

class Vlan(models.Model):
    numero_vlan = models.IntegerField(help_text="valor entre 1 á 4094")
    nome = models.CharField(max_length=128, unique=True, help_text="nome deve ser único")

    class Meta:
        verbose_name_plural = "VLANs"
    
    def __str__(self) -> str:
        return self.numero_vlan
    
    def clean(self):
        if self.numero_vlan < 1 or self.numero_vlan > 4094:
            raise ValidationError("O valor da VLAN deve estar entre 1 e 4094.")

class Circuito(models.Model):
    conexao = models.ForeignKey(Conexao, on_delete=models.PROTECT)
    ponta_a = models.ForeignKey(Equipamento, on_delete=models.PROTECT, related_name='circuito_ponta_a')
    interface_ponta_a = models.CharField(max_length=128)
    ponta_b = models.ForeignKey(Equipamento, on_delete=models.PROTECT, related_name='circuito_ponta_b')
    interface_ponta_b = models.CharField(max_length=128)
    id_sensor_prtg = models.IntegerField()
    designacao = models.CharField(max_length=128, unique=True)
    ip_circuito = models.CharField(max_length=128)
    submask = models.IntegerField(help_text="valor entre 0 á 32")
    id_vlan = models.ForeignKey(Vlan, on_delete=models.PROTECT)
    # estacao = models.ForeignKey(Estacao, on_delete=models.PROTECT)
    # rack = models.CharField(max_length=128)
    # fila = models.CharField(max_length=128)
    # porta = models.CharField(max_length=128)
    # equipamento_acesso = models.ForeignKey(Equipamento, on_delete=models.PROTECT, related_name='circuito_acesso')
    # dgo_cto = models.CharField(max_length=128)
    # porta_dgo_cto = models.IntegerField()
    # equipamento_ultima_milha = models.ForeignKey(Equipamento, on_delete=models.PROTECT, related_name='circuito_ultima_milha')

    class Meta:
        verbose_name_plural = "Circuitos"
    
    def clean(self):
        if self.submask < 0 or self.submask > 32:
            raise ValidationError("O valor da SUBMASK deve estar entre 0 e 32.")
    
    def __str__(self) -> str:
        return self.designacao
