from django.contrib import admin
from django import forms
from django.utils.html import format_html
from .models import Aluno, Turma, Aula
from .widgets import CameraWidget, CAMERA_JS

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Usar o widget de câmera para o campo de foto
        self.fields['foto'].widget = CameraWidget()

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    form = AlunoForm
    list_display = ('nome', 'telefone', 'foto_thumbnail', 'ativo')
    search_fields = ('nome', 'cpf_responsavel')
    list_filter = ('ativo', 'escola_publica')
    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('nome', 'data_nascimento', 'foto')
        }),
        ('Contato', {
            'fields': ('telefone', 'cpf_responsavel', 'endereco')
        }),
        ('Situação', {
            'fields': ('escola_publica', 'ativo', 'observacoes')
        }),
    )
    
    def foto_thumbnail(self, obj):
        """Mostrar miniatura da foto na lista"""
        if obj.foto:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius: 4px;" />',
                obj.foto.url
            )
        return '-'
    foto_thumbnail.short_description = 'Foto'
    
    def change_form(self, request, object_id=None, form_url='', extra_context=None):
        """Adicionar JavaScript do widget de câmera"""
        if extra_context is None:
            extra_context = {}
        extra_context['extra_js'] = [CAMERA_JS]
        return super().change_form(request, object_id, form_url, extra_context)
    
    class Media:
        js = ('admin/js/admin_camera.js',)

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