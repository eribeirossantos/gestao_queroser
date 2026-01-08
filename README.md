# 🎵 Sistema de Gestão - Instituto Quero Ser

Um sistema web completo de gestão para ONGs que oferecem oficinas educacionais e musicais. Desenvolvido com Django para gerenciar alunos, turmas, patrimônio, financeiro e doações.

## ✨ Funcionalidades

### 📚 Módulo Acadêmico

- Cadastro completo de alunos (dados pessoais, responsáveis, informações sociais)
- Gerenciamento de turmas/oficinas (dias, horários, professores)
- Controle de presença e frequência em aulas
- Vinculação de alunos a turmas

### 💰 Módulo Financeiro

- Cadastro de doadores (pessoas físicas e jurídicas)
- Registro de doações com múltiplas formas de pagamento (PIX, dinheiro, cartão, boleto)
- Rastreamento de destino das doações (projetos específicos)
- Painel com visualização de totais

### 🎸 Módulo de Patrimônio

- Inventário completo de instrumentos musicais
- Controle de estado de conservação dos bens
- Sistema de empréstimos a alunos
- Rastreamento de devoluções

## 🛠️ Requisitos

- Python 3.8+
- PostgreSQL 10+
- pip ou pipenv

## 🚀 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/gestao_queroser.git
cd gestao_queroser
```

### 2. Crie um ambiente virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o arquivo .env

```bash
# Copie o arquivo de exemplo
cp .env.example .env

# Edite o arquivo .env com suas configurações
# Importante: Mude a SECRET_KEY!
```

### 5. Crie o banco de dados PostgreSQL

```bash
# Usando psql
createdb queroser_db
```

### 6. Execute as migrações

```bash
python manage.py migrate
```

### 7. Crie um superusuário

```bash
python manage.py createsuperuser
```

### 8. Inicie o servidor de desenvolvimento

```bash
python manage.py runserver
```

Acesse: http://127.0.0.1:8000/admin/

## 📁 Estrutura do Projeto

```
gestao_queroser/
├── academico/              # Módulo de gestão acadêmica
│   ├── models.py           # Aluno, Turma, Aula
│   ├── admin.py            # Interface administrativa
│   └── ...
├── financeiro/             # Módulo financeiro
│   ├── models.py           # Doador, Doação
│   ├── admin.py            # Interface administrativa
│   └── ...
├── patrimonio/             # Módulo de patrimônio
│   ├── models.py           # Instrumento, Empréstimo
│   ├── admin.py            # Interface administrativa
│   └── ...
├── core/                   # Configurações do projeto
│   ├── settings.py         # Configurações Django
│   ├── urls.py             # URLs principais
│   └── wsgi.py             # WSGI para produção
├── manage.py               # CLI do Django
├── requirements.txt        # Dependências Python
├── .env.example           # Modelo de variáveis de ambiente
├── .gitignore             # Arquivos ignorados pelo Git
└── README.md              # Este arquivo
```

## 🔧 Configuração para Produção

### Segurança

1. **Mude a SECRET_KEY**:

   ```python
   # Gere uma nova chave
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

2. **Configure o DEBUG**:

   ```
   DEBUG=False
   ```

3. **Configure ALLOWED_HOSTS**:

   ```
   ALLOWED_HOSTS=seu-dominio.com,www.seu-dominio.com
   ```

4. **Use HTTPS** e configure CSRF

### Deployment com Gunicorn

```bash
gunicorn core.wsgi:application --bind 0.0.0.0:8000
```

## 📊 Modelos de Dados

### Acadêmico

- **Aluno**: Nome, data de nascimento, CPF responsável, telefone, endereço, escola pública/privada, observações
- **Turma**: Nome, professor, dia da semana, horário, alunos matriculados
- **Aula**: Turma, data, conteúdo, alunos presentes

### Financeiro

- **Doador**: Nome, tipo (PF/PJ), CPF/CNPJ, email, telefone, ativo
- **Doação**: Doador, data, valor, forma de pagamento, destino

### Patrimônio

- **Instrumento**: Nome, série, código interno, estado, status, data de aquisição, valor
- **Empréstimo**: Instrumento, aluno, datas (saída/previsão/devolução), observações

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 💬 Suporte

Para dúvidas ou problemas, abra uma [issue](https://github.com/seu-usuario/gestao_queroser/issues) no repositório.

## 👥 Autores

- Instituto Quero Ser

---

**Desenvolvido com ❤️ para educação e transformação social**
