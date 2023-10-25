from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Operacao)
class OperacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ['nome']

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ['nome']

@admin.register(Consultor)
class ConsultorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'telefone', 'ativo')
    list_filter = ('ativo',)
    search_fields = ['nome']

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'operacao', 'nome', 'uf')
    list_filter = ('operacao',)
    search_fields = ['nome']

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ['nome']

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('id', 'operacao', 'nome', 'cnpj')
    list_filter = ('operacao',)
    search_fields = ['nome']

@admin.register(CanalVenda)
class CanalVendaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ['nome']

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'razao_social',
        'nome',
        'cnpj',
        'logradouro',
        'bairro',
        'cidade',
        'estado',
        'cep',
        'telefone',
        'email',
    )
    list_filter = ('estado', 'cidade')
    search_fields = ['razao_social']

@admin.register(Conexao)
class ConexaoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'operacao',
        'empresa',
        'cod',
        'canal_venda',
        'status',
        'cliente',
        'logradouro',
        'cidade',
        'estado',
        'servico',
        'banda',
        'data_contrato',
        'data_ativacao',
        'data_vencimento',
        'observacao',
        'consultor',
    )
    list_filter = ('estado', 'cidade')
    search_fields = ['empresa']

@admin.register(FormaPagamento)
class FormaPagamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo')
    search_fields = ['tipo']

@admin.register(Faturamento)
class FaturamentoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'conexao',
        'valor',
        'vencimento',
        'valor_faturado',
        'valor_recebido',
        'saldo',
        'data_pagamento',
        'nf',
        'data_nf',
        'data_envio_nf',
    )
    search_fields = ['conexao']

@admin.register(Financeiro)
class FinanceiroAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'conexao',
        'forma_de_pagamento',
        'saldo_a_pagar',
        'data_debito',
    )
    search_fields = ['conexao']