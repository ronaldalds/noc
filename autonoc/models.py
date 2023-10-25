from django.db import models

# Create your models here.
class Operacao(models.Model):
    nome = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = "Operações"
    
    def __str__(self) -> str:
        return self.nome

class Status(models.Model):
    nome = models.CharField(max_length=128)
    
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

class Estado(models.Model):
    nome = models.CharField(max_length=128)
    uf = models.CharField(max_length=2)
    operacao = models.ForeignKey(Operacao, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Estados"
    
    def __str__(self) -> str:
        return self.uf

class Servico(models.Model):
    nome = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = "Serviços"
    
    def __str__(self) -> str:
        return self.nome

class Empresa(models.Model):
    nome = models.CharField(max_length=128)
    cnpj = models.CharField(max_length=128)
    operacao = models.ForeignKey(Operacao, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Empresas"
    
    def __str__(self) -> str:
        return self.nome

class CanalVenda(models.Model):
    nome = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = "Canais de Vendas"
    
    def __str__(self) -> str:
        return self.nome

class Cliente(models.Model):
    razao_social = models.CharField(max_length=128)
    nome = models.CharField(max_length=128)
    cnpj = models.CharField(max_length=128)
    logradouro = models.CharField(max_length=128)
    bairro = models.CharField(max_length=128)
    cidade = models.CharField(max_length=128)
    estado = models.CharField(max_length=128)
    cep = models.CharField(max_length=128)
    telefone = models.CharField(max_length=128)
    email = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = "Clientes"
    
    def __str__(self) -> str:
        return self.razao_social

class Conexao(models.Model):
    operacao = models.ForeignKey(Operacao, on_delete=models.PROTECT)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    cod = models.IntegerField()
    canal_venda = models.ForeignKey(CanalVenda, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    logradouro = models.CharField(max_length=128)
    cidade = models.CharField(max_length=128)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    servico = models.ForeignKey(Servico, on_delete=models.PROTECT)
    banda = models.IntegerField()
    data_contrato = models.DateField()
    data_ativacao = models.DateField()
    data_vencimento = models.DateField()
    observacao = models.CharField(max_length=512)
    consultor = models.ForeignKey(Consultor, on_delete=models.PROTECT)

class FormaPagamento(models.Model):
    tipo = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = "Formas de Pagamento"
    
    def __str__(self) -> str:
        return self.tipo

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

class Financeiro(models.Model):
    conexao = models.ForeignKey(Conexao, on_delete=models.PROTECT)
    forma_de_pagamento = models.ForeignKey(FormaPagamento, on_delete=models.PROTECT)
    saldo_a_pagar = models.FloatField()
    data_debito = models.DateField()