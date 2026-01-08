# 🚀 Guia de Deployment para Produção

## Hospedagem Recomendada

### Opção 1: Heroku (Simples)

### Opção 2: Railway (Moderno)

### Opção 3: DigitalOcean (Completo)

### Opção 4: AWS (Enterprise)

---

## Railway (Recomendado para começar)

### 1. Criar conta

- Visite [railway.app](https://railway.app)
- Faça login com GitHub

### 2. Criar novo projeto

```bash
npm i -g @railway/cli
railway login
railway init
```

### 3. Conectar banco de dados PostgreSQL

- Dashboard → Plugins → Add PostgreSQL
- Railway vinculará automaticamente as variáveis de ambiente

### 4. Deploy

```bash
railway up
```

---

## DigitalOcean App Platform (Recomendado para aplicações maiores)

### 1. Preparar projeto

```bash
# Criar arquivo Procfile
echo "web: gunicorn core.wsgi:application" > Procfile
```

### 2. Conectar GitHub

- DigitalOcean App Platform
- Connect GitHub Repository
- Selecionar branch `main`

### 3. Configurar variáveis de ambiente

```
DEBUG=False
SECRET_KEY=<gerar nova chave>
DB_NAME=queroser_prod
DB_USER=queroser
DB_PASSWORD=<gerar senha forte>
DB_HOST=<database-host>
DB_PORT=5432
ALLOWED_HOSTS=seu-dominio.com,www.seu-dominio.com
```

### 4. Deploy automático

- Cada push para `main` fará deploy automático

---

## VPS (DigitalOcean, Linode, Vultr)

### 1. Preparar servidor

```bash
# Atualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar dependências
sudo apt install -y python3-pip python3-venv postgresql postgresql-contrib nginx

# Criar usuário Django
sudo useradd -m djangouser
sudo su - djangouser
```

### 2. Clonar projeto

```bash
git clone https://github.com/seu-usuario/gestao_queroser.git
cd gestao_queroser
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configurar banco de dados

```bash
sudo -u postgres psql

CREATE DATABASE queroser_prod;
CREATE USER queroser_prod WITH PASSWORD 'senha_super_segura';
ALTER ROLE queroser_prod SET client_encoding TO 'utf8';
ALTER ROLE queroser_prod SET default_transaction_isolation TO 'read committed';
ALTER ROLE queroser_prod SET default_transaction_deferrable TO on;
GRANT ALL PRIVILEGES ON DATABASE queroser_prod TO queroser_prod;
\q
```

### 4. Configurar .env em produção

```bash
nano .env
```

```
DEBUG=False
SECRET_KEY=<gerar nova chave segura>
DB_NAME=queroser_prod
DB_USER=queroser_prod
DB_PASSWORD=senha_super_segura
DB_HOST=localhost
DB_PORT=5432
ALLOWED_HOSTS=seu-dominio.com,www.seu-dominio.com
```

### 5. Migrações e estáticos

```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

### 6. Configurar Gunicorn

```bash
# Criar socket
mkdir -p ~/run/gunicorn

# Criar arquivo de serviço systemd
sudo nano /etc/systemd/system/gunicorn_queroser.service
```

```ini
[Unit]
Description=Gunicorn service for Quero Ser
After=network.target

[Service]
Type=notify
User=djangouser
WorkingDirectory=/home/djangouser/gestao_queroser
ExecStart=/home/djangouser/gestao_queroser/venv/bin/gunicorn \
          --workers 3 \
          --bind unix:/home/djangouser/run/gunicorn/socket \
          core.wsgi:application

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl start gunicorn_queroser
sudo systemctl enable gunicorn_queroser
```

### 7. Configurar Nginx

```bash
sudo nano /etc/nginx/sites-available/queroser
```

```nginx
upstream gunicorn_queroser {
    server unix:/home/djangouser/run/gunicorn/socket fail_timeout=0;
}

server {
    listen 80;
    server_name seu-dominio.com www.seu-dominio.com;

    client_max_body_size 20M;

    location /static/ {
        alias /home/djangouser/gestao_queroser/staticfiles/;
    }

    location /media/ {
        alias /home/djangouser/gestao_queroser/media/;
    }

    location / {
        proxy_pass http://gunicorn_queroser;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

```bash
sudo ln -s /etc/nginx/sites-available/queroser /etc/nginx/sites-enabled/
sudo systemctl restart nginx
```

### 8. SSL/HTTPS (Let's Encrypt)

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d seu-dominio.com -d www.seu-dominio.com
```

---

## Monitoramento em Produção

### Logs

```bash
# Gunicorn
sudo journalctl -u gunicorn_queroser -f

# Nginx
sudo tail -f /var/log/nginx/error.log
```

### Backup automático do banco

```bash
# Criar script de backup
mkdir -p ~/backups

# Arquivo: backup.sh
#!/bin/bash
BACKUP_DIR="/home/djangouser/backups"
DB_NAME="queroser_prod"
DB_USER="queroser_prod"

pg_dump $DB_NAME > $BACKUP_DIR/backup-$(date +%Y%m%d-%H%M%S).sql

# Agendar com cron
crontab -e
# 0 2 * * * /home/djangouser/backup.sh
```

---

## Checklist de Deploy

- [ ] SECRET_KEY alterada e segura
- [ ] DEBUG = False
- [ ] ALLOWED_HOSTS configurado
- [ ] HTTPS/SSL ativado
- [ ] Banco de dados em produção
- [ ] Estáticos coletados
- [ ] Backups configurados
- [ ] Logs monitorados
- [ ] Email configurado
- [ ] Sentry/logging remoto configurado (opcional)

---

## Troubleshooting

### 500 Internal Server Error

```bash
# Verificar logs
python manage.py runserver --settings=core.settings
python manage.py check --deploy
```

### Permissões

```bash
sudo chown -R djangouser:djangouser /home/djangouser/gestao_queroser
```

### Banco de dados não conecta

```bash
python manage.py dbshell
# Se conectar, o problema está na aplicação
```

---

**Precisa de ajuda? Abra uma issue no repositório!**
