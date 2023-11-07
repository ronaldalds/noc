from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import *

# Register your models here.
@admin.register(Operacao)
class OperacaoAdmin(VersionAdmin):
    list_display = ('id', 'nome')
    search_fields = ['nome']

@admin.register(Empresa)
class EmpresaAdmin(VersionAdmin):
    list_display = (
        'id',
        'razao_social',
        'nome_fantasia',
        'nome',
        'cnpj',
        'logradouro',
        'numero',
        'bairro',
        'cidade'
    )
    search_fields = ['nome', 'razao_social']

@admin.register(Estado)
class EstadoAdmin(VersionAdmin):
    list_display = ('id', 'operacao', 'nome', 'uf')
    list_filter = ('operacao',)
    search_fields = ['nome']

@admin.register(Cidade)
class CidadeAdmin(VersionAdmin):
    list_display = ('id', 'nome', 'sigla', 'estado')
    list_filter = ('estado',)
    search_fields = ['nome']

@admin.register(Cliente)
class ClienteAdmin(VersionAdmin):
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
class ConexaoAdmin(VersionAdmin):
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
    list_filter = ('cidade_instalacao', 'operacao', 'status', 'sinal')
    search_fields = ['cliente__nome', 'cliente__cnpj']

@admin.register(StatusContrato)
class StatusContratoAdmin(VersionAdmin):
    list_display = ('id', 'nome', 'observacao')
    search_fields = ['nome']

@admin.register(Consultor)
class ConsultorAdmin(VersionAdmin):
    list_display = ('id', 'nome', 'telefone', 'ativo')
    list_filter = ('ativo',)
    search_fields = ['nome']

@admin.register(ServicoContrato)
class ServicoContratoAdmin(VersionAdmin):
    list_display = ('id', 'nome')
    search_fields = ['nome']

@admin.register(CanalVenda)
class CanalVendaAdmin(VersionAdmin):
    list_display = ('id', 'nome')
    search_fields = ['nome']

@admin.register(FormaPagamento)
class FormaPagamentoAdmin(VersionAdmin):
    list_display = ('id', 'tipo')
    search_fields = ['tipo']

@admin.register(Faturamento)
class FaturamentoAdmin(VersionAdmin):
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
class FinanceiroClienteAdmin(VersionAdmin):
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
class EstacaoAdmin(VersionAdmin):
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
class EquipamentoAdmin(VersionAdmin):
    list_display = (
        'id',
        'nome',
        'modelo',
        'ip',
        'estacao',
        'rack',
        'fila',
    )
    list_filter = ('estacao',)
    search_fields = ['nome', 'modelo']

@admin.register(Vlan)
class VlanAdmin(VersionAdmin):
    list_display = (
        'numero_vlan',
        'nome',
    )
    search_fields = ['nome', 'numero_vlan']

@admin.register(Circuito)
class CircuitoAdmin(VersionAdmin):
    list_display = (
        'id',
        'conexao',
        'ponta_a',
        'interface_ponta_a',
        'ponta_b',
        'interface_ponta_b',
        'id_sensor_prtg',
        'designacao',
        'ip_circuito',
        'submask',
        'id_vlan',
        # 'estacao',
        # 'rack',
        # 'fila',
        # 'porta',
        # 'equipamento_acesso',
        # 'dgo_cto',
        # 'porta_dgo_cto',
        # 'equipamento_ultima_milha',
    )
    # list_filter = ('id_vlan',)
    search_fields = ['conexao', 'designacao']