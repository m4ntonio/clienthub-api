# 🚀 API CRUD com FastAPI + MongoDB

Projeto de API REST para cadastro de clientes com interface web simples.

![Python](https://img.shields.io/badge/python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.135-green)
![MongoDB](https://img.shields.io/badge/MongoDB-database-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

## 🧠 Tecnologias

- FastAPI
- MongoDB
- Pydantic
- Uvicorn
- HTML + JavaScript (frontend)

## 📦 Funcionalidades

- Criar cliente
- Listar clientes
- Buscar por ID
- Atualizar cliente
- Deletar cliente

## 🚀 Como rodar

### 1. Clonar o projeto

```bash
git clone https://github.com/seuusuario/seuprojeto.git
cd seuprojeto
```
### 2. Criar ambiente virtual
```
python -m venv venv

Ativar:

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```
### 3. Instalar dependências
```
pip install -r requirements.txt
```

### 4. Rodar a API
```
uvicorn main:app --reload
```

### 5. Acessar
```
Swagger: http://127.0.0.1:8000/docs
Frontend: abrir index.html
```

### 🗄️ Banco de dados

MongoDB rodando localmente:
```
mongodb://localhost:27017
```
```
📁 Estrutura
.
├── main.py
├── models.py
├── routes.py
├── database.py
├── index.html
├── requirements.txt
└── README.md
```

### ⚠️ Observações
- CORS habilitado para desenvolvimento
- Não usar allow_origins=["*"] em produção


### 📌 Próximos passos
- Autenticação (JWT)
- Deploy
- Docker
- Frontend com React