from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Operacao)
class OperacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ['nome']

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'razao_social',
        'nome',
        'cnpj',
        'logradouro',
        'numero',
        'bairro',
        'cidade'
    )
    search_fields = ['nome', 'razao_social']

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'operacao', 'nome', 'uf')
    list_filter = ('operacao',)
    search_fields = ['nome']

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sigla', 'estado')
    list_filter = ('estado',)
    search_fields = ['nome']

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'razao_social',
        'nome',
        'cnpj',
        'logradouro',
        'numero',
        'bairro',
        'cidade',
        'cep',
        'telefone',
        'email',
    )
    list_filter = ('cidade',)
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
        'logradouro_instalacao',
        'cidade_instalacao',
        'servico_contrato',
        'banda_contrato',
        'data_contrato',
        'data_ativacao',
        'data_vencimento',
        'observacao',
        'consultor',
        'sinal',
        'banda_reducao',
    )
    list_filter = ('cidade_instalacao', 'operacao', 'status', 'sinal')  # Adicionado 'operacao' e 'status' como campos filtráveis
    search_fields = ['cliente__nome', 'cliente__cnpj']

@admin.register(StatusContrato)
class StatusContratoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'observacao')
    search_fields = ['nome']

@admin.register(Consultor)
class ConsultorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'telefone', 'ativo')
    list_filter = ('ativo',)
    search_fields = ['nome']

@admin.register(ServicoContrato)
class ServicoContratoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ['nome']

@admin.register(CanalVenda)
class CanalVendaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ['nome']

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
        'mes_vencimento',
        'ano_vencimento',
        'vencimento',
        'valor_faturado',
        'valor_recebido',
        'saldo',
        'data_pagamento',
        'nf',
        'data_nf',
        'data_envio_nf',
    )
    list_filter = ('mes_vencimento', 'ano_vencimento')
    search_fields = ['conexao']

@admin.register(FinanceiroCliente)
class FinanceiroClienteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'conexao',
        'forma_de_pagamento',
        'saldo_a_pagar',
        'mes_debito',
        'ano_debito',
        'data_debito',
    )
    list_filter = ('mes_debito', 'ano_debito')
    search_fields = ['conexao']

@admin.register(Estacao)
class EstacaoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'logradouro',
        'numero',
        'bairro',
        'cidade',
    )
    list_filter = ('cidade',)
    search_fields = ['nome', 'cidade']

@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'modelo',
        'ip',
    )
    search_fields = ['nome', 'modelo']

@admin.register(Vlan)
class VlanAdmin(admin.ModelAdmin):
    list_display = (
        'numero_vlan',
        'nome',
    )
    search_fields = ['nome', 'numero_vlan']

@admin.register(Circuito)
class CircuitoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'conexao',
        'ponta_a',
        'ponta_b',
        'id_sensor_prtg',
        'designacao',
        'estacao',
        'rack',
        'fila',
        'porta',
        'equipamento_acesso',
        'ip_circuito',
        'submask',
        'id_vlan',
        'dgo_cto',
        'porta_dgo_cto',
        'equipamento_ultima_milha',
    )
    list_filter = ('estacao', 'id_vlan')
    search_fields = ['conexao', 'designacao']