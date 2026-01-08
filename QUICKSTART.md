# 🚀 INÍCIO RÁPIDO - LINKS E COMANDOS

## Leia Nesta Ordem

1. **AGORA** → [PROFISSIONAL_STATUS.txt](PROFISSIONAL_STATUS.txt)
2. **ANTES DE PUSH** → [GITHUB_SETUP_CHECKLIST.md](GITHUB_SETUP_CHECKLIST.md)
3. **PARA COLABORADORES** → [README.md](README.md)
4. **PARA CONTRIBUIR** → [CONTRIBUTING.md](CONTRIBUTING.md)
5. **PARA PRODUÇÃO** → [DEPLOYMENT.md](DEPLOYMENT.md)

---

## 🔑 Comando Mais Importante

Gere uma **NOVA SECRET_KEY** antes de fazer push:

```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Cole no `.env`:

```
SECRET_KEY=<chave-gerada-aqui>
```

---

## 🚀 Setup Rápido Local

### Opção 1: Manual

```powershell
git clone https://github.com/seu-usuario/gestao_queroser.git
cd gestao_queroser
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
# Edite .env com suas credenciais
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Opção 2: Automático (Windows)

```powershell
python setup.py
```

### Opção 3: Docker

```powershell
docker-compose up -d
# Acesse: http://localhost:8000/admin/
```

---

## 📤 Fazer Push para GitHub

```powershell
# 1. Criar repositório em github.com/new (copie a URL)

# 2. Fazer commit
git init
git add .
git commit -m "Initial commit: Professional setup with documentation"

# 3. Fazer push
git branch -M main
git remote add origin https://github.com/seu-usuario/gestao_queroser.git
git push -u origin main
```

---

## 📊 Estrutura do Projeto

```
Código                          Documentação
├── academico/                  ├── README.md ⭐
├── financeiro/                 ├── CONTRIBUTING.md
├── patrimonio/                 ├── DEPLOYMENT.md
└── core/                       ├── GITHUB_SETUP_CHECKLIST.md ⭐
                                ├── CHANGELOG_SETUP.md
Configuração                    ├── PROJETO_OVERVIEW.txt
├── requirements.txt            ├── RESUMO_PROFISSIONALIZACAO.md
├── pyproject.toml              └── PROFISSIONAL_STATUS.txt
├── .env (local)
├── .env.example ⭐            Docker & DevOps
├── .gitignore                  ├── Dockerfile
└── setup.py                    ├── docker-compose.yml
                                └── .github/workflows/
Qualidade
├── .editorconfig               Legal
└── LICENSE                     └── LICENSE (MIT)
```

---

## ✅ Checklist Pré-GitHub

- [ ] Leu PROFISSIONAL_STATUS.txt
- [ ] Gerou nova SECRET_KEY
- [ ] Atualizou .env
- [ ] Executou `python manage.py migrate`
- [ ] Testou localmente (`python manage.py runserver`)
- [ ] Verificou .env NÃO está commitado
- [ ] Criou repositório no GitHub
- [ ] Fez commit e push
- [ ] Configurou branch protection
- [ ] Habilitou GitHub Actions

---

## 💡 Comandos Úteis

```powershell
# Verificar status do Git
git status

# Ver commits
git log --oneline

# Verificar se .env está no .gitignore
git check-ignore .env

# Listar branching
git branch -a

# Ver configuração remota
git remote -v

# Atualizar do GitHub
git pull

# Forçar push (CUIDADO!)
git push -f origin main

# Resetar último commit (CUIDADO!)
git reset --soft HEAD~1
```

---

## 🐳 Comandos Docker

```powershell
# Iniciar
docker-compose up -d

# Ver logs
docker-compose logs -f

# Executar comando
docker-compose exec web python manage.py migrate

# Parar
docker-compose stop

# Desligar
docker-compose down

# Limpar tudo
docker-compose down -v
```

---

## 📱 Links Importantes

- 📚 [Django Docs](https://docs.djangoproject.com/)
- 🐙 [GitHub](https://github.com/)
- 🐳 [Docker](https://www.docker.com/)
- 🔐 [Python-Dotenv](https://github.com/theskumar/python-dotenv)
- 🚀 [Gunicorn](https://gunicorn.org/)

---

## 🎯 Próximas Melhorias (Futura)

- [ ] Adicionar testes unitários
- [ ] Configurar Sentry
- [ ] Adicionar logging
- [ ] Configurar email
- [ ] Adicionar API REST
- [ ] Frontend moderno
- [ ] Cache com Redis
- [ ] CI/CD mais robusto

---

## ❓ Dúvidas?

1. Leia a [documentação relevante](README.md)
2. Verifique [DEPLOYMENT.md](DEPLOYMENT.md)
3. Abra uma issue no GitHub
4. Consulte [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 🎉 Status

✅ **Tudo pronto para GitHub!**

Bom sorte com seu projeto! 🚀

---

**Instituto Quero Ser - Sistema de Gestão para ONGs Educacionais**

_Desenvolvido com ❤️ para educação e transformação social_
