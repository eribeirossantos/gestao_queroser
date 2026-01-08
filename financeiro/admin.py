from django.contrib import admin
from django.db.models import Sum # Importante para somar
from django.contrib import messages # Importante para mostrar a mensagem
from .models import Doador, Doacao

@admin.register(Doador)
class DoadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'telefone', 'ativo')
    search_fields = ('nome', 'cpf_cnpj')
    list_filter = ('ativo', 'tipo')

@admin.register(Doacao)
class DoacaoAdmin(admin.ModelAdmin):
    list_display = ('data', 'doador', 'valor', 'forma_pagamento', 'destino')
    list_filter = ('data', 'forma_pagamento', 'destino')
    date_hierarchy = 'data'
    search_fields = ('doador__nome',)

    # --- O TRUQUE DO SOMATÓRIO AQUI ---
    def changelist_view(self, request, extra_context=None):
        # Primeiro, executamos a lógica padrão do Django
        response = super().changelist_view(request, extra_context)

        # Tentamos pegar os dados filtrados (queryset) da resposta
        try:
            # A variável 'cl' (ChangeList) contém os filtros atuais
            qs = response.context_data['cl'].queryset
            # Calculamos a soma do campo 'valor'
            soma = qs.aggregate(Sum('valor'))['valor__sum']
            
            # Se tiver soma, mostramos uma mensagem no topo da tela
            if soma:
                messages.info(request, f"💰 TOTAL VISUALIZADO: R$ {soma:,.2f}")
        except (AttributeError, KeyError):
            # Se der erro (ex: não é uma tela de lista), passa reto
            pass

        return response