# 🚀 Guia de Deployment Gratuito

Este guia mostra como fazer deploy do Sistema de Gestão Quero Ser com **custo zero ou mínimo**.

## 📋 Opções de Hospedagem Gratuita

### 1. **Render** (Recomendado) ⭐

- **Tier gratuito**: Até 1 dynos
- **Banco de dados**: PostgreSQL gratuito (até 1GB)
- **Tempo de resposta**: Pode dormir após 15 minutos de inatividade (tier gratuito)
- **Custo**: R$0 - R$15 se quiser Pro

#### Passos:

1. **Crie conta no Render**: https://render.com

2. **Conecte seu repositório GitHub**:

   - Faça login
   - Clique em "New +"
   - Selecione "Web Service"
   - Conecte seu repositório GitHub

3. **Configure o serviço**:

   ```
   Name: gestao-queroser
   Environment: Python 3
   Build Command: pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
   Start Command: gunicorn core.wsgi:application --bind 0.0.0.0:$PORT
   ```

4. **Configure variáveis de ambiente**:

   - Abra "Environment"
   - Adicione:
     ```
     SECRET_KEY=<gere uma nova chave>
     DEBUG=False
     ALLOWED_HOSTS=<seu-app>.onrender.com,www.<seu-app>.onrender.com
     DATABASE_URL=<fornecido automaticamente pelo Render>
     ```

5. **Deploy automático**:
   - Toda vez que você fazer push no GitHub, o Render fará deploy automaticamente

**Gerar SECRET_KEY**:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

### 2. **PythonAnywhere** (Muito Fácil)

- **Tier gratuito**: Domínio `.pythonanywhere.com`
- **Banco de dados**: SQLite incluído
- **CPU/Memória**: Suficiente para ONGs
- **Custo**: R$0 - R$50/mês para domínio customizado

#### Passos:

1. **Crie conta**: https://www.pythonanywhere.com/

2. **Faça upload do código**:

   - Use o console web ou Git
   - Clone seu repositório

3. **Configure um Web App**:

   - "Add a new web app"
   - Manual configuration > Python 3.11
   - Source code: `/home/seu-usuario/gestao_queroser`

4. **Configure WSGI**:

   - Edit `/var/www/seu_usuario_pythonanywhere_com_wsgi.py`
   - Adicione:

   ```python
   import os
   import sys

   path = '/home/seu-usuario/gestao_queroser'
   if path not in sys.path:
       sys.path.append(path)

   os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'

   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```

5. **Instale dependências**:

   - Console: `pip install -r requirements.txt`
   - Rode migrações: `python manage.py migrate`

6. **Reinicie o app**:
   - Na dashboard, clique em "Reload"

---

### 3. **Railway** (Crédito Gratuito)

- **Tier gratuito**: $5/mês em créditos
- **Banco de dados**: Suporta PostgreSQL
- **Facilidade**: Muito simples

#### Passos:

1. **Crie conta**: https://railway.app/

2. **Conecte GitHub**:

   - Novo projeto > GitHub repo

3. **Configure variáveis**:

   ```
   SECRET_KEY=<gere uma nova chave>
   DEBUG=False
   ALLOWED_HOSTS=<seu-app>.railway.app
   DATABASE_URL=<fornecido automaticamente>
   ```

4. **Deploy automático**:
   - Railway detecta Django automaticamente

---

## 🛠️ Preparação do Projeto

### Antes de fazer deploy, execute:

```bash
# Crie arquivo .env com variáveis de produção
cp .env.example .env

# Edite .env com valores de produção
# DEBUG=False
# SECRET_KEY=<sua chave gerada>

# Teste localmente
python manage.py runserver

# Colete arquivos estáticos
python manage.py collectstatic --noinput

# Execute migrações
python manage.py migrate
```

---

## 💡 Dicas de Custo Zero

✅ **Use SQLite** (padrão) - sem custos, sem serviço externo
✅ **Use tier gratuito** - Render, PythonAnywhere ou Railway
✅ **Comprima estáticos** - WhiteNoise já está configurado
✅ **Otimize imagens** - Reduza tamanho de uploads
✅ **Cleanup regular** - Remova dados antigos periodicamente

---

## 🚨 Troubleshooting

### Erro: "ModuleNotFoundError: No module named 'X'"

```bash
pip install -r requirements.txt
```

### Erro: "DisallowedHost"

- Adicione seu domínio em `ALLOWED_HOSTS` no `.env`
- Redeploy a aplicação

### Banco de dados vazio

```bash
python manage.py migrate
python manage.py createsuperuser
```

### Arquivo estático não encontrado

```bash
python manage.py collectstatic --noinput
```

---

## 📱 Domínio Customizado (Opcional)

Para usar seu próprio domínio (ex: gestao.minhaong.com.br):

### Render

- Vá em "Custom Domains"
- Adicione seu domínio
- Configure DNS records conforme instruções

### PythonAnywhere

- Upgrade para Pro (R$50/mês)
- Aponte DNS para PythonAnywhere

### Railway

- Aponte DNS para Railway

---

## 🔐 Segurança em Produção

✅ `DEBUG=False` - Nunca exponha erros
✅ `SECRET_KEY` - Mude para uma chave segura
✅ `ALLOWED_HOSTS` - Liste apenas seus domínios
✅ HTTPS - Render/Railway/PythonAnywhere fornecem grátis
✅ Backups - Configure em sua hospedagem

---

## 📞 Suporte

Dúvidas? Abra uma issue no repositório:
https://github.com/seu-usuario/gestao_queroser/issues
