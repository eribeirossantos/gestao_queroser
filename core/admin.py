from django.contrib.admin import AdminSite
from django.db.models import Count, Avg, Sum
from django.utils.timezone import now
from datetime import timedelta
from academico.models import Aluno, Turma, Aula
from financeiro.models import Doador, Doacao
import json
from collections import defaultdict

class CustomAdminSite(AdminSite):
    """Admin customizado com dashboard"""
    
    def index(self, request, extra_context=None):
        """Sobrescreve a página inicial do admin para adicionar estatísticas"""
        
        # Estatísticas básicas
        stats = {
            'total_alunos': Aluno.objects.count(),
            'alunos_ativos': Aluno.objects.filter(ativo=True).count(),
            'alunos_inativos': Aluno.objects.filter(ativo=False).count(),
            'total_turmas': Turma.objects.count(),
            'total_doadores': Doador.objects.count(),
        }
        
        # Frequência média por turma
        frequencia_data = self._calcular_frequencia_turmas()
        
        # Arrecadação nos últimos 6 meses
        arrecadacao_data = self._calcular_arrecadacao_6_meses()
        
        # Adicionar ao contexto
        extra_context = extra_context or {}
        extra_context.update({
            'stats': stats,
            'frequencia': frequencia_data,
            'arrecadacao': arrecadacao_data,
        })
        
        return super().index(request, extra_context)
    
    def _calcular_frequencia_turmas(self):
        """Calcula a frequência média de cada turma"""
        turmas = Turma.objects.all()
        turmas_nomes = []
        percentuais = []
        
        for turma in turmas:
            aulas = Aula.objects.filter(turma=turma)
            if aulas.exists():
                total_alunos = turma.alunos.count()
                if total_alunos > 0:
                    # Calcular média de presença
                    total_presencas = sum(aula.alunos_presentes.count() for aula in aulas)
                    total_possivel = aulas.count() * total_alunos
                    percentual = (total_presencas / total_possivel * 100) if total_possivel > 0 else 0
                    
                    turmas_nomes.append(turma.nome[:20])  # Limitar tamanho do nome
                    percentuais.append(round(percentual, 1))
        
        return {
            'turmas': json.dumps(turmas_nomes),
            'percentuais': json.dumps(percentuais)
        }
    
    def _calcular_arrecadacao_6_meses(self):
        """Calcula a arrecadação dos últimos 6 meses"""
        hoje = now()
        seis_meses_atras = hoje - timedelta(days=180)
        
        # Buscar doações dos últimos 6 meses
        doacoes = Doacao.objects.filter(
            data__gte=seis_meses_atras
        ).values('data').annotate(total=Sum('valor'))
        
        # Agrupar por mês
        meses_valores = defaultdict(float)
        for doacao in doacoes:
            mes_ano = doacao['data'].strftime('%b/%y')
            meses_valores[mes_ano] += float(doacao['total'])
        
        # Garantir que temos 6 meses mesmo sem doações
        meses_lista = []
        valores_lista = []
        
        for i in range(5, -1, -1):
            data_mes = hoje - timedelta(days=30 * i)
            mes_ano = data_mes.strftime('%b/%y')
            meses_lista.append(mes_ano)
            valores_lista.append(round(meses_valores.get(mes_ano, 0), 2))
        
        return {
            'meses': json.dumps(meses_lista),
            'valores': json.dumps(valores_lista)
        }

# Substituir o site admin padrão
from django.contrib import admin
admin.site.__class__ = CustomAdminSite
