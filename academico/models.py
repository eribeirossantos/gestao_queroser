from django.db import models
from datetime import date

class Aluno(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome Completo")
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")
    cpf_responsavel = models.CharField(max_length=14, blank=True, null=True, verbose_name="CPF do Responsável")
    telefone = models.CharField(max_length=20, verbose_name="Telefone/WhatsApp")
    endereco = models.TextField(blank=True, null=True, verbose_name="Endereço")
    
    # Foto do aluno
    foto = models.ImageField(upload_to='alunos/fotos/', blank=True, null=True, verbose_name="Foto")
    
    # Campos importantes para ONGs
    escola_publica = models.BooleanField(default=True, verbose_name="Estuda em Escola Pública?")
    observacoes = models.TextField(blank=True, null=True, verbose_name="Observações (Saúde/Social)")
    
    data_cadastro = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"

class Turma(models.Model):
    DIAS_SEMANA = [
        ('SEG', 'Segunda-feira'),
        ('TER', 'Terça-feira'),
        ('QUA', 'Quarta-feira'),
        ('QUI', 'Quinta-feira'),
        ('SEX', 'Sexta-feira'),
        ('SAB', 'Sábado'),
    ]

    nome = models.CharField(max_length=100, verbose_name="Nome da Turma (Ex: Violão Iniciante)")
    professor = models.CharField(max_length=100, verbose_name="Nome do Professor/Voluntário")
    dia_semana = models.CharField(max_length=3, choices=DIAS_SEMANA, verbose_name="Dia da Semana")
    horario = models.TimeField(verbose_name="Horário")
    
    # Relacionamento com alunos
    alunos = models.ManyToManyField(Aluno, blank=True, related_name="turmas", verbose_name="Alunos Matriculados")

    def __str__(self):
        return f"{self.nome} - {self.get_dia_semana_display()} às {self.horario}"

    class Meta:
        verbose_name = "Turma/Oficina"
        verbose_name_plural = "Turmas/Oficinas"

class Aula(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, verbose_name="Turma")
    data = models.DateField(default=date.today, verbose_name="Data da Aula")
    conteudo = models.TextField(blank=True, null=True, verbose_name="Conteúdo Ministrado")
    
    # Chamada: quem estava presente
    alunos_presentes = models.ManyToManyField(Aluno, blank=True, verbose_name="Alunos Presentes")

    def __str__(self):
        return f"{self.turma} - {self.data.strftime('%d/%m/%Y')}"

    class Meta:
        verbose_name = "Diário de Aula / Chamada"
        verbose_name_plural = "Diários de Aula / Chamadas"
        ordering = ['-data']