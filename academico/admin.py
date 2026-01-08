from django.contrib import admin
from .models import Aluno, Turma, Aula

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'ativo') # O que aparece na lista
    search_fields = ('nome', 'cpf_responsavel')   # Barra de busca
    list_filter = ('ativo', 'escola_publica')     # Filtros laterais

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'professor', 'dia_semana', 'horario', 'contagem_alunos')
    list_filter = ('dia_semana', 'professor')
    
    # Cria uma interface visual fácil para adicionar alunos
    filter_horizontal = ('alunos',) 

    # Uma função extra para mostrar na lista quantos alunos tem na sala
    def contagem_alunos(self, obj):
        return obj.alunos.count()
    contagem_alunos.short_description = "Qtd. Alunos"

@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ('turma', 'data', 'qtd_presentes')
    list_filter = ('turma', 'data')
    date_hierarchy = 'data' # Cria uma navegação por datas no topo muito útil
    filter_horizontal = ('alunos_presentes',) # Interface de dois quadros para selecionar alunos
    
    def qtd_presentes(self, obj):
        return obj.alunos_presentes.count()
    qtd_presentes.short_description = "Qtd. Presentes"