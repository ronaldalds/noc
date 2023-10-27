from django.db import models
from .empresa_models import Empresa
from .cliente_models import Cliente
from .endereco_models import Cidade, Operacao

class StatusContrato(models.Model):
    nome = models.CharField(max_length=128)
    banda = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = "Status"
    
    def __str__(self) -> str:
        return self.nome

class Consultor(models.Model):
    nome = models.CharField(max_length=128)
    telefone = models.CharField(max_length=128)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Consultores"
    
    def __str__(self) -> str:
        return self.nome

class ServicoContrato(models.Model):
    nome = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = "Serviços do Contrato"
    
    def __str__(self) -> str:
        return self.nome

class CanalVenda(models.Model):
    nome = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = "Canais de Vendas"
    
    def __str__(self) -> str:
        return self.nome

class FormaPagamento(models.Model):
    tipo = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = "Formas de Pagamento"
    
    def __str__(self) -> str:
        return self.tipo

class Conexao(models.Model):
    operacao = models.ForeignKey(Operacao, on_delete=models.PROTECT)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    cod = models.IntegerField()
    canal_venda = models.ForeignKey(CanalVenda, on_delete=models.PROTECT)
    status = models.ForeignKey(StatusContrato, on_delete=models.PROTECT)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    logradouro_instalacao = models.CharField(max_length=128)
    cidade_instalacao = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    servico_contrato = models.ForeignKey(ServicoContrato, on_delete=models.PROTECT)
    banda = models.IntegerField()
    data_contrato = models.DateField()
    data_ativacao = models.DateField()
    data_vencimento = models.DateField()
    observacao = models.TextField()
    consultor = models.ForeignKey(Consultor, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Conexões"

    def __str__(self) -> str:
        return f"{self.cliente.cnpj} - {self.cliente.razao_social}"