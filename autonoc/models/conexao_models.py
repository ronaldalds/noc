from django.db import models
from .empresa_models import Empresa
from .cliente_models import Cliente
from .endereco_models import Cidade, Operacao
from django.db.models.signals import pre_save
from django.dispatch import receiver

class StatusContrato(models.Model):
    nome = models.CharField(max_length=128, verbose_name="nome *")
    observacao = models.TextField(max_length=512)
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
    sigla = models.CharField(max_length=6)

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
    banda_contrato = models.IntegerField()
    data_contrato = models.DateField()
    data_ativacao = models.DateField()
    data_vencimento = models.DateField()
    observacao = models.TextField()
    consultor = models.ForeignKey(Consultor, on_delete=models.PROTECT)
    sinal = models.BooleanField(default=True)
    banda_reducao = models.IntegerField()
    cod_contrato = models.CharField(max_length=128)
    designacao = models.CharField(max_length=128, unique=True, null=True, blank=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Conexões"
    
    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)
        self.designacao = f"{self.cidade_instalacao.estado.uf}.{self.cidade_instalacao.cod_cidade}-{self.servico_contrato.sigla}-{self.cod_contrato}-{self.pk}"
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.cliente.cnpj} - {self.cliente.nome_fantasia} - {self.cod}"

@receiver(pre_save, sender=Conexao)
def status_contrato_post_save(sender, instance, **kwargs):
    if not instance._state.adding:
        try:
            # Obtém o objeto no banco de dados com os valores atuais
            old_instance = Conexao.objects.get(pk=instance.pk)
        except Conexao.DoesNotExist:
            old_instance = None

        if old_instance and (old_instance.sinal == True) and (instance.sinal == False):
            # O campo 'sinal' foi alterado
            print(f"\n\n\n\nO campo 'sinal' foi alterado de {old_instance.sinal} para {instance.sinal}. Executando comando... {instance.banda_reducao}\n\n\n\n")
