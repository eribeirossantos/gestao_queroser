from django.contrib import admin
from .models import Instrumento, Emprestimo

@admin.register(Instrumento)
class InstrumentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo_interno', 'status', 'estado')
    list_filter = ('status', 'estado')
    search_fields = ('nome', 'codigo_interno', 'numero_serie')

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('instrumento', 'aluno', 'data_saida', 'data_prevista', 'devolvido')
    list_filter = ('data_saida', 'data_prevista')
    search_fields = ('instrumento__nome', 'aluno__nome') # Busca pelo nome do instrumento OU do aluno

    # Cria uma coluna calculada para mostrar se já devolveu
    def devolvido(self, obj):
        return obj.data_devolucao is not None
    devolvido.boolean = True # Transforma em ícone de ✅ ou ❌
    devolvido.short_description = "Devolvido?"