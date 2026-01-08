from django.db import models
from datetime import date

class Doador(models.Model):
    TIPO_PESSOA = [
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica/Empresa'),
    ]
    
    nome = models.CharField(max_length=200, verbose_name="Nome / Razão Social")
    tipo = models.CharField(max_length=2, choices=TIPO_PESSOA, default='PF')
    cpf_cnpj = models.CharField(max_length=20, blank=True, null=True, verbose_name="CPF/CNPJ")
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    
    ativo = models.BooleanField(default=True, verbose_name="Doador Ativo?")
    data_cadastro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Doador / Parceiro"
        verbose_name_plural = "Doadores / Parceiros"

class Doacao(models.Model):
    FORMA_PAGAMENTO = [
        ('PIX', 'PIX'),
        ('DINHEIRO', 'Dinheiro'),
        ('CARTAO', 'Cartão'),
        ('BOLETO', 'Boleto'),
        ('OUTRO', 'Outros'),
    ]

    doador = models.ForeignKey(Doador, on_delete=models.SET_NULL, null=True, verbose_name="Quem doou?")
    data = models.DateField(default=date.today, verbose_name="Data da Doação")
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor (R$)")
    forma_pagamento = models.CharField(max_length=20, choices=FORMA_PAGAMENTO, default='PIX')
    
    # Campo opcional para vincular a doação a um projeto específico (Ex: "Compra de Violões")
    destino = models.CharField(max_length=100, blank=True, null=True, verbose_name="Destino (Opcional)", help_text="Ex: Projeto Música, Manutenção, Livre")

    def __str__(self):
        return f"R$ {self.valor} - {self.doador}"

    class Meta:
        verbose_name = "Entrada de Doação"
        verbose_name_plural = "Entradas de Doações"