# Configuração de Desenvolvimento

Este arquivo contém instruções para configurar o ambiente de desenvolvimento local.

## Pré-requisitos

- Python 3.8 ou superior
- PostgreSQL 10 ou superior
- Git

## Setup Inicial

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/gestao_queroser.git
cd gestao_queroser
```

### 2. Criar ambiente virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente

```bash
# Copiar arquivo de exemplo
cp .env.example .env

# Editar .env com suas configurações
```

### 5. Criar database PostgreSQL

```bash
# Entrar no PostgreSQL
psql -U postgres

# Criar database
CREATE DATABASE queroser_db;
CREATE USER queroser_user WITH PASSWORD 'sua_senha';
ALTER ROLE queroser_user SET client_encoding TO 'utf8';
ALTER ROLE queroser_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE queroser_user SET default_transaction_deferrable TO on;
GRANT ALL PRIVILEGES ON DATABASE queroser_db TO queroser_user;
\q
```

### 6. Executar migrações

```bash
python manage.py migrate
```

### 7. Criar superusuário

```bash
python manage.py createsuperuser
```

### 8. Executar servidor de desenvolvimento

```bash
python manage.py runserver
```

Acesse: http://127.0.0.1:8000/admin/

## Comandos Úteis

```bash
# Criar nova migração após alterações no models.py
python manage.py makemigrations

# Ver migrações pendentes
python manage.py showmigrations

# Executar testes
python manage.py test

# Coletar arquivos estáticos
python manage.py collectstatic
```

## Estrutura de Branches

- `main` - Produção
- `develop` - Desenvolvimento
- `feature/*` - Novas funcionalidades
- `fix/*` - Correções de bugs

## Padrões de Código

- PEP 8 para Python
- Nomes em português para modelos de negócio, em inglês para configurações
- Sempre incluir `verbose_name` e `verbose_name_plural` em modelos

## Issues e PRs

1. Sempre criar uma issue antes de um PR
2. Referenciar a issue no título do PR
3. Adicionar descrição clara das mudanças
4. Rodar testes antes de submeter

---

Dúvidas? Abra uma issue no repositório!
