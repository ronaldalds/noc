from django.contrib import admin
from reversion.admin import VersionAdmin
from import_export.admin import ImportExportMixin
from ..models import *

@admin.register(Faturamento)
class FaturamentoAdmin(ImportExportMixin, VersionAdmin):
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
    list_display_links = list_display
    list_filter = ('mes_vencimento', 'ano_vencimento')
    search_fields = ['conexao']

@admin.register(FinanceiroCliente)
class FinanceiroClienteAdmin(ImportExportMixin, VersionAdmin):
    list_display = (
        'id',
        'conexao',
        'forma_de_pagamento',
        'saldo_a_pagar',
        'mes_debito',
        'ano_debito',
        'data_debito',
    )
    list_display_links = list_display
    list_filter = ('mes_debito', 'ano_debito')
    search_fields = ['conexao']