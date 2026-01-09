# ✅ Checklist de Deployment Gratuito

Use este checklist antes de fazer deploy da sua aplicação.

## 🔐 Segurança

- [ ] **SECRET_KEY**: Gerada e configurada em `.env`

  ```bash
  python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
  ```

- [ ] **DEBUG**: Definido como `False` em produção

  ```
  DEBUG=False
  ```

- [ ] **ALLOWED_HOSTS**: Configurado com seus domínios

  ```
  ALLOWED_HOSTS=seu-app.onrender.com,www.seu-app.onrender.com,seu-dominio.com.br
  ```

- [ ] **HTTPS**: Ativado (Render/Railway/PythonAnywhere fornecem certificado grátis)

---

## 📦 Dependências

- [ ] `requirements.txt` atualizado com todas as dependências
- [ ] Verificado: `pip install -r requirements.txt`
- [ ] Sem dependências faltando em produção

---

## 🗄️ Banco de Dados

- [ ] **Migração do banco**:

  ```bash
  python manage.py migrate
  ```

- [ ] **Superusuário criado** (para acesso ao admin):

  ```bash
  python manage.py createsuperuser
  ```

- [ ] **Dados iniciais** carregados (se necessário):
  ```bash
  python manage.py loaddata initial_data.json
  ```

---

## 🎨 Arquivos Estáticos

- [ ] **Coletados em produção**:

  ```bash
  python manage.py collectstatic --noinput
  ```

- [ ] **WhiteNoise configurado** no `settings.py`

- [ ] **STATIC_URL e STATIC_ROOT** configurados

---

## 🚀 Deployment

### Render.com

- [ ] Repositório GitHub conectado ao Render
- [ ] Build Command configurado:
  ```
  pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
  ```
- [ ] Start Command configurado:
  ```
  gunicorn core.wsgi:application --bind 0.0.0.0:$PORT
  ```
- [ ] Variáveis de ambiente adicionadas:
  - [ ] SECRET_KEY
  - [ ] DEBUG=False
  - [ ] ALLOWED_HOSTS
  - [ ] DATABASE_URL (gerado automaticamente)

### PythonAnywhere

- [ ] Código enviado para `/home/seu-usuario/gestao_queroser`
- [ ] WSGI file configurado
- [ ] Dependências instaladas: `pip install -r requirements.txt`
- [ ] Migrações executadas: `python manage.py migrate`
- [ ] App recarregado (Reload button)

### Railway.app

- [ ] Repositório GitHub conectado
- [ ] Variáveis de ambiente configuradas
- [ ] Deployment automático ativado

---

## 🧪 Testes Pré-Deploy

- [ ] Executar servidor localmente:

  ```bash
  python manage.py runserver
  ```

- [ ] Acessar `http://localhost:8000/admin/` com superusuário

- [ ] Testar todas as funcionalidades principais:

  - [ ] Cadastrar aluno
  - [ ] Criar turma
  - [ ] Registrar instrumento
  - [ ] Cadastrar doador
  - [ ] Registrar doação

- [ ] Coletar estáticos sem erros:

  ```bash
  python manage.py collectstatic --noinput
  ```

- [ ] Nenhum erro de migração:
  ```bash
  python manage.py migrate --check
  ```

---

## 📋 Pós-Deployment

- [ ] Aplicação rodando sem erros em produção
- [ ] Admin acessível em `https://seu-app.onrender.com/admin/`
- [ ] Emails funcionando (se configurado)
- [ ] Backup do banco de dados configurado (se disponível)
- [ ] Logs sendo monitorados

---

## 🆘 Troubleshooting

### Erro: "ModuleNotFoundError"

```bash
pip install -r requirements.txt
```

### Erro: "DisallowedHost"

- Atualize `ALLOWED_HOSTS` em `.env`
- Redeploy a aplicação

### Banco de dados vazio

```bash
python manage.py migrate
python manage.py createsuperuser
```

### Arquivo estático quebrado (CSS/JS)

```bash
python manage.py collectstatic --noinput --clear
```

### Erro: "ModuleNotFoundError: No module named 'dj_database_url'"

```bash
pip install dj-database-url
```

---

## 📞 Próximos Passos

1. ✅ Siga este checklist completamente
2. 📖 Leia [DEPLOYMENT_GRATUITO.md](DEPLOYMENT_GRATUITO.md) para instruções específicas
3. 🚀 Faça deploy em sua plataforma escolhida
4. 🔗 Configure domínio customizado (opcional)
5. 🎉 Celebre! Sua ONG agora tem um sistema online grátis!

---

**Data do deployment**: ******\_\_\_******
**Plataforma escolhida**: ******\_\_\_******
**URL da aplicação**: ******\_\_\_******
