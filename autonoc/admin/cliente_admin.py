from django.contrib import admin
from reversion.admin import VersionAdmin
from ..models import *


@admin.register(Cliente)
class ClienteAdmin(VersionAdmin):
    list_display = (
        'id',
        'nome_fantasia',
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
    list_display_links = list_display
    search_fields = ['nome_fantasia']
