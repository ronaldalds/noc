from django.contrib import admin
from reversion.admin import VersionAdmin
from import_export.admin import ImportExportMixin
from ..models import *

@admin.register(Estacao)
class EstacaoAdmin(ImportExportMixin, VersionAdmin):
    list_display = (
        'id',
        'nome',
        'logradouro',
        'numero',
        'bairro',
        'cidade',
    )
    list_display_links = list_display
    list_filter = ('cidade',)
    search_fields = ['nome', 'cidade']

@admin.register(Equipamento)
class EquipamentoAdmin(ImportExportMixin, VersionAdmin):
    list_display = (
        'id',
        'nome',
        'modelo',
        'ip',
        'estacao',
        'rack',
        'fila',
    )
    list_display_links = list_display
    list_filter = ('estacao',)
    search_fields = ['nome', 'modelo']

@admin.register(Vlan)
class VlanAdmin(ImportExportMixin, VersionAdmin):
    list_display = (
        'numero_vlan',
        'nome',
    )
    list_display_links = list_display
    search_fields = ['nome', 'numero_vlan']

@admin.register(Circuito)
class CircuitoAdmin(ImportExportMixin, VersionAdmin):
    list_display = (
        'id',
        'conexao',
        'ponta_a',
        'interface_ponta_a',
        'ponta_b',
        'interface_ponta_b',
        'id_sensor_prtg',
        'ip_circuito',
        'submask',
        'id_vlan',
        'get_conexao_designacao',
    )
    list_display_links = list_display
    search_fields = [
        'conexao__cliente__nome_fantasia',
        'conexao__cliente__cnpj',
        'conexao__cod',
        ]
    
    readonly_fields = [
        'get_conexao_designacao',
    ]

    def get_conexao_designacao(self, obj):
        return obj.conexao.designacao
    
    get_conexao_designacao.short_description = 'Designacao'