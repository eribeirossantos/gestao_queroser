from django.db import models
# NÃO importamos o Aluno aqui em cima para evitar erro circular

class Instrumento(models.Model):
    ESTADO_CHOICES = [
        ('NOVO', 'Novo'),
        ('BOM', 'Bom Estado'),
        ('REGULAR', 'Regular (Marcas de uso)'),
        ('DANIFICADO', 'Danificado (Precisa reparo)'),
        ('SUCATA', 'Sucata/Inutilizável'),
    ]

    STATUS_CHOICES = [
        ('DISPONIVEL', 'Disponível'),
        ('EMPRESTADO', 'Emprestado'),
        ('MANUTENCAO', 'Em Manutenção'),
    ]

    nome = models.CharField(max_length=100, verbose_name="Nome (Ex: Violão Tagima)")
    numero_serie = models.CharField(max_length=50, blank=True, null=True, verbose_name="Nº de Série")
    codigo_interno = models.CharField(max_length=20, unique=True, verbose_name="Cód. Etiqueta (Patrimônio)")
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='BOM', verbose_name="Estado de Conservação")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DISPONIVEL')
    
    data_aquisicao = models.DateField(blank=True, null=True, verbose_name="Data de Aquisição")
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Valor (R$)")

    def __str__(self):
        return f"{self.nome} ({self.codigo_interno})"

    class Meta:
        verbose_name = "Instrumento"
        verbose_name_plural = "Instrumentos"

class Emprestimo(models.Model):
    instrumento = models.ForeignKey(Instrumento, on_delete=models.CASCADE)
    
    # AQUI ESTÁ A CORREÇÃO: Usamos uma string para referenciar o modelo do outro app
    aluno = models.ForeignKey('academico.Aluno', on_delete=models.CASCADE)
    
    data_saida = models.DateField(auto_now_add=True, verbose_name="Data de Retirada")
    data_prevista = models.DateField(verbose_name="Previsão de Devolução")
    data_devolucao = models.DateField(blank=True, null=True, verbose_name="Devolvido em")
    observacoes = models.TextField(blank=True, null=True, verbose_name="Obs. na retirada (Ex: já estava arranhado)")

    def __str__(self):
        # O Django resolve a string 'academico.Aluno' automaticamente aqui
        return f"{self.instrumento} -> {self.aluno}"

    class Meta:
        verbose_name = "Empréstimo de Instrumento"
        verbose_name_plural = "Controle de Empréstimos"