from django.db import models
from .conexao_models import Conexao, FormaPagamento
from django.db.models.signals import pre_save
from django.dispatch import receiver

MESES = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro',
}

# Create your models here.
class Faturamento(models.Model):
    conexao = models.ForeignKey(Conexao, on_delete=models.PROTECT)
    valor = models.FloatField()
    vencimento = models.DateField()
    valor_faturado = models.FloatField()
    valor_recebido = models.FloatField()
    saldo = models.FloatField()
    data_pagamento = models.DateField()
    nf = models.IntegerField()
    data_nf = models.DateField()
    data_envio_nf = models.DateField()
    mes_vencimento = models.CharField(max_length=64, null=True, blank=True)
    ano_vencimento = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Faturamentos"
    
    def __str__(self) -> str:
        return f"{self.conexao} - {self.mes_vencimento} de {self.ano_vencimento}"
        
class FinanceiroCliente(models.Model):
    conexao = models.ForeignKey(Conexao, on_delete=models.PROTECT)
    forma_de_pagamento = models.ForeignKey(FormaPagamento, on_delete=models.PROTECT)
    saldo_a_pagar = models.FloatField()
    data_debito = models.DateField()
    mes_debito = models.CharField(max_length=64, null=True, blank=True)
    ano_debito = models.IntegerField(null=True, blank=True)

@receiver(pre_save, sender=Faturamento)
def extrair_mes_e_ano(sender, instance, **kwargs):
    if instance.vencimento:
        instance.mes_vencimento = MESES.get(instance.vencimento.month)
        instance.ano_vencimento = instance.vencimento.year

@receiver(pre_save, sender=Faturamento)
def extrair_mes_e_ano(sender, instance, **kwargs):
    if instance.data_debito:
        instance.mes_debito = MESES.get(instance.data_debito.month)
        instance.ano_debito = instance.data_debito.year