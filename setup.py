#!/usr/bin/env python
"""
Script de inicialização rápida do projeto

Uso: python setup.py
"""

import os
import sys
import subprocess
from pathlib import Path

def run_command(command, description):
    """Executa um comando e mostra status"""
    print(f"\n{'='*60}")
    print(f"📦 {description}")
    print(f"{'='*60}")
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"✅ {description} - OK")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - ERRO")
        print(f"Erro: {e}")
        return False

def main():
    print("\n")
    print(" " * 20 + "🎵 SETUP - Instituto Quero Ser 🎵")
    print(" " * 15 + "Sistema de Gestão para ONGs Educacionais")
    
    # Verificar se .env existe
    if not Path('.env').exists():
        print("\n⚠️  Arquivo .env não encontrado!")
        print("   Copie .env.example para .env e configure suas variáveis.")
        
        if input("\n   Deseja copiar .env.example para .env agora? (s/n): ").lower() == 's':
            import shutil
            shutil.copy('.env.example', '.env')
            print("   ✅ Arquivo .env criado. Configure-o antes de continuar!")
        else:
            print("   ❌ Configure o arquivo .env e tente novamente.")
            sys.exit(1)
    
    # Executar migrações
    if not run_command(
        "python manage.py migrate",
        "Executando migrações do banco de dados"
    ):
        print("\n❌ Erro ao executar migrações!")
        sys.exit(1)
    
    # Coletar estáticos
    if not run_command(
        "python manage.py collectstatic --noinput",
        "Coletando arquivos estáticos"
    ):
        print("\n⚠️  Erro ao coletar estáticos (não crítico)")
    
    # Criar superusuário
    print(f"\n{'='*60}")
    print("👤 Criar Superusuário")
    print(f"{'='*60}")
    if input("Deseja criar um superusuário agora? (s/n): ").lower() == 's':
        subprocess.run("python manage.py createsuperuser", shell=True)
    
    print("\n")
    print(" " * 20 + "✅ Setup Completo!")
    print("\n   Para iniciar o servidor de desenvolvimento:")
    print("   $ python manage.py runserver")
    print("\n   Acesse: http://127.0.0.1:8000/admin/")
    print("\n")

if __name__ == '__main__':
    main()
