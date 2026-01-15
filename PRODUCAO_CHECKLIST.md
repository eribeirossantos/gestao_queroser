# ✅ Checklist - Migração para Produção

Use este checklist para garantir que tudo está configurado corretamente antes de colocar em produção.

## 🔐 Segurança

- [ ] **SECRET_KEY**: Gerada nova e segura
  ```bash
  python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
  ```

- [ ] **DEBUG**: Definido como `False`
  ```
  DEBUG=False
  ```

- [ ] **ALLOWED_HOSTS**: Contém todos seus domínios
  ```
  ALLOWED_HOSTS=gestao-queroser.onrender.com,www.gestao-queroser.onrender.com
  ```

- [ ] **HTTPS**: Ativado (Render fornece certificado grátis)

- [ ] **Senha admin**: Alterada da senha padrão

---

## 🗄️ Banco de Dados

- [ ] **DATABASE_URL**: Copiada do Railway e configurada no Render
  - Teste a conexão localmente:
    ```bash
    python manage.py dbshell
    ```

- [ ] **Migrações**: Todas aplicadas
  ```bash
  python manage.py migrate --check
  ```

- [ ] **Dados iniciais**: Carregados (se houver)
  ```bash
  python manage.py loaddata initial_data.json
  ```

- [ ] **Superusuário**: Criado para acesso ao admin
  ```bash
  python manage.py createsuperuser
  ```

---

## 📦 Dependências

- [ ] **requirements.txt**: Atualizado com todas as dependências
  ```bash
  pip freeze > requirements.txt
  ```

- [ ] **Verificar instalação**:
  ```bash
  pip install -r requirements.txt
  ```

- [ ] **Sem erros ao importar**:
  ```bash
  python manage.py check
  ```

---

## 🎨 Arquivos Estáticos

- [ ] **Coletados localmente**:
  ```bash
  python manage.py collectstatic --noinput
  ```

- [ ] **WhiteNoise configurado**: Verificar em `settings.py`
  ```python
  STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
  ```

- [ ] **STATIC_URL e STATIC_ROOT**: Configurados corretamente

---

## 🚀 Render - Configuração

- [ ] **Build Command**:
  ```
  pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
  ```

- [ ] **Start Command**:
  ```
  gunicorn core.wsgi:application --bind 0.0.0.0:$PORT
  ```

- [ ] **Variáveis de Ambiente**: Todas configuradas
  - SECRET_KEY
  - DEBUG=False
  - ALLOWED_HOSTS
  - DATABASE_URL (do Railway)

---

## 🧪 Testes Pré-Deploy

- [ ] **Teste local**:
  ```bash
  python manage.py runserver
  ```

- [ ] **Admin acessível**: http://localhost:8000/admin/

- [ ] **Funcionalidades principais testadas**:
  - [ ] Fazer login
  - [ ] Cadastrar aluno
  - [ ] Criar turma
  - [ ] Registrar instrumento
  - [ ] Cadastrar doador
  - [ ] Registrar doação

- [ ] **Nenhum erro ao coletar estáticos**:
  ```bash
  python manage.py collectstatic --noinput
  ```

- [ ] **Nenhum erro ao rodar migrações**:
  ```bash
  python manage.py migrate
  ```

---

## 📤 Fazer Deploy

- [ ] **Código commitado e pusheado** para GitHub
  ```bash
  git add .
  git commit -m "Mensagem descritiva"
  git push origin main
  ```

- [ ] **No Render**: Clique em "Manual Deploy" > "Deploy Latest Commit"

- [ ] **Aguardar deploy** (normalmente 2-5 minutos)

---

## ✅ Pós-Deploy

- [ ] **Aplicação respondendo**: https://gestao-queroser.onrender.com/

- [ ] **Admin acessível**: https://gestao-queroser.onrender.com/admin/

- [ ] **Login funcionando** com usuário admin

- [ ] **Dados visíveis** e corretos

- [ ] **Sem erros nos logs** do Render

- [ ] **HTTPS ativado** (URL deve mostrar 🔒)

---

## 🔄 Backup Configurado

- [ ] **Railway backups ativados**: Verificar em https://railway.app

- [ ] **Plano de backup manual**: Documentado em PRODUCAO.md

- [ ] **Teste de restauração**: Procedimento documentado

---

## 📋 Documentação

- [ ] **README.md**: Atualizado com URL de produção

- [ ] **PRODUCAO.md**: Preenchido com instruções de manutenção

- [ ] **DEPLOYMENT_GRATUITO.md**: Ainda relevante para referência

- [ ] **.env.example**: Atualizado

---

## 🎉 Pronto para Produção!

Quando todos os itens acima estiverem marcados ✅:

```
✅ Sua aplicação está segura e pronta para produção!
```

---

**Data de Deploy**: _______________
**URL de Produção**: _______________
**Responsável**: _______________
**Backup testado em**: _______________
