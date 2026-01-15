# 🔐 Guia de Produção - Sistema Quero Ser

Este documento descreve como manter o sistema em produção de forma segura e confiável.

## 📊 Ambiente de Produção

**Plataforma**: Render (Hospedagem)
**Banco de Dados**: Railway PostgreSQL
**URL**: https://gestao-queroser.onrender.com

---

## 🔐 Variáveis de Ambiente - Produção

No painel do **Render**, configure estas variáveis de ambiente:

```
SECRET_KEY=<sua-chave-segura>
DEBUG=False
ALLOWED_HOSTS=gestao-queroser.onrender.com,www.gestao-queroser.onrender.com
DATABASE_URL=postgresql://user:password@host:port/dbname
ENVIRONMENT=production
```

### Como obter DATABASE_URL do Railway:

1. Acesse: https://railway.app
2. Vá ao seu projeto PostgreSQL
3. Clique em "Connect"
4. Copie a **Database URL (Environment Variable)**
5. Cole no Render como `DATABASE_URL`

---

## 🚀 Fazer Deploy em Produção

### Opção 1: Deploy Automático (Recomendado)

Toda vez que você fizer `git push` para `main`:
1. GitHub recebe o push
2. Render detecta a mudança automaticamente
3. Deploy acontece em 2-5 minutos
4. Banco de dados PostgreSQL é usado

```bash
# No seu computador local
git add .
git commit -m "Sua mensagem"
git push origin main
```

### Opção 2: Deploy Manual

No painel do Render:
1. Clique no seu serviço `gestao-queroser`
2. Clique em "Manual Deploy"
3. Selecione "Deploy Latest Commit"

---

## 💾 Backup e Recuperação

### Backup Automático (Railway)

Railway oferece backups automáticos! Para acessar:

1. Acesse: https://railway.app
2. Vá ao seu projeto PostgreSQL
3. Na aba "Data"
4. Procure por "Backups"

### Backup Manual - Exportar Dados

Para fazer backup manualmente do banco:

```bash
# Conectar ao banco PostgreSQL
PGPASSWORD="sua_senha" pg_dump -h host -U user -d database > backup.sql

# Ou via Django (exporta para JSON)
python manage.py dumpdata > backup_completo.json
```

### Restaurar Backup

Se precisar restaurar dados:

```bash
# Via SQL
PGPASSWORD="sua_senha" psql -h host -U user -d database < backup.sql

# Via Django JSON
python manage.py loaddata backup_completo.json
```

---

## 🔍 Monitorar Aplicação em Produção

### Acessar Logs do Render

1. Vá ao painel do Render
2. Selecione seu serviço `gestao-queroser`
3. Clique em "Logs"
4. Procure por erros ou avisos

### Problemas Comuns

#### Erro: "DisallowedHost"
- **Causa**: ALLOWED_HOSTS não contém o domínio
- **Solução**: Atualize `ALLOWED_HOSTS` nas variáveis do Render

#### Erro: "Connection refused" (Banco)
- **Causa**: DATABASE_URL incorreta
- **Solução**: Verifique se a DATABASE_URL está correta no Render

#### Erro: "No such table"
- **Causa**: Migrações não rodaram
- **Solução**: No Render, logs devem mostrar se `python manage.py migrate` falhou

---

## 📱 Manutenção Regular

### Weekly (Semanal)
- [ ] Verificar logs do Render
- [ ] Verificar se há atualizações de segurança do Django

### Monthly (Mensal)
- [ ] Fazer backup manual dos dados
- [ ] Revisar performance da aplicação
- [ ] Atualizar dependências: `pip list --outdated`

### Quarterly (Trimestral)
- [ ] Fazer update de segurança completo
- [ ] Testar procedimento de restauração de backup
- [ ] Revisar ALLOWED_HOSTS e segurança

---

## 🛡️ Checklist de Segurança em Produção

- [ ] `DEBUG=False` (nunca `True` em produção)
- [ ] `SECRET_KEY` é única e segura
- [ ] `ALLOWED_HOSTS` contém apenas seus domínios
- [ ] HTTPS ativado (Railway fornece grátis)
- [ ] Backups funcionando
- [ ] Logs sendo monitorados
- [ ] DATABASE_URL não é público (usar variáveis de ambiente)

---

## 🚨 Procedimento de Emergência

Se precisar fazer rollback (voltar para versão anterior):

```bash
# Ver histórico de commits
git log --oneline

# Voltar para commit anterior
git revert <commit-hash>
git push origin main

# O Render fará deploy da versão anterior automaticamente
```

---

## 📞 Suporte

- Documentação Django: https://docs.djangoproject.com
- Documentação Render: https://render.com/docs
- Documentação Railway: https://docs.railway.app
- Issues do projeto: https://github.com/eribeirossantos/gestao_queroser/issues

---

**Última atualização**: 14 de janeiro de 2026
**Status**: Produção ✅
