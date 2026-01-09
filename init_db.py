#!/usr/bin/env python
"""
Script para inicializar o banco de dados com dados padrão
Execute: python init_db.py
"""
import os
import django
from pathlib import Path

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

def create_default_admin():
    """Cria usuário admin padrão se não existir"""
    if User.objects.filter(username='admin').exists():
        print("✓ Usuário admin já existe")
        return
    
    User.objects.create_superuser(
        username='admin',
        email='admin@queroser.org',
        password='Admin@123456'
    )
    print("✓ Usuário admin criado com sucesso!")
    print("\n📋 Credenciais padrão:")
    print("   Username: admin")
    print("   Password: Admin@123456")
    print("\n⚠️  IMPORTANTE: Mude a senha após o primeiro login!")

if __name__ == '__main__':
    create_default_admin()
