# API do Projeto "À Mão" 🚀

Bem-vindo(a) à API do projeto **"À Mão"**!  
Esta é a aplicação back-end que dá vida à nossa plataforma de assinatura de kits de manualidades.  
A API gerencia usuários, assinaturas, catálogos de produtos, tutoriais e todo o sistema por trás da experiência criativa e consciente que oferecemos.

![Status do Projeto](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

---

## 🛠️ Tecnologias Utilizadas

- **Django**: Framework web principal para o back-end.  
- **Django REST Framework**: Para a construção da API RESTful.  
- **Simple JWT**: Autenticação segura baseada em JSON Web Tokens.  
- **PostgreSQL**: Banco de dados relacional principal (produção).  
- **SQLite**: Banco de dados leve para desenvolvimento rápido.  
- **Python Decouple**: Gerenciamento de variáveis de ambiente.

---

## ✅ Pré-requisitos

Antes de começar, certifique-se de ter os seguintes softwares instalados:

- **Git**: Para clonar o repositório.
- **Python 3.8 ou superior** – [Baixar Python](https://www.python.org/downloads/)
- **PostgreSQL (opcional)** – [Baixar PostgreSQL](https://www.postgresql.org/download/)
- **Cliente de API recomendado**: Postman ou Insomnia

---

## ⚙️ Configuração do Ambiente (Passos Iniciais)

Estes passos são comuns para ambas as opções de instalação:

### 1. Clone o Repositório

Abra seu terminal e clone o projeto do GitHub para sua máquina:

```bash
git clone <URL_DO_SEU_REPOSITORIO_GITHUB>
```

### 2. Navegue Para a Pasta do Projeto

```bash
cd ahmao
```

### 3. Crie e Ative o Ambiente Virtual

Isso isola as dependências do projeto para evitar conflitos:

```bash
# Cria o ambiente virtual
python -m venv venv

# Ativa o ambiente virtual
# No Windows:
venv\Scripts\activate

# No macOS/Linux:
source venv/bin/activate
```

### 4. Instale as Dependências

Este comando lê o arquivo requirements.txt e instala todas as bibliotecas Python necessárias:

```bash
pip install -r requirements.txt
```
ℹ️ O psycopg2-binary (driver do PostgreSQL) será instalado mesmo que você use SQLite. Isso é normal e não causará problemas.

---

## 💾 Opções de Instalação do Banco de Dados
Escolha uma das duas opções abaixo para configurar seu banco de dados:

### 🔹 Opção 1: Instalação Completa (com PostgreSQL)
#### 1. Crie um Banco de Dados Vazio
- Acesse o pgAdmin (ou outra ferramenta).
- Crie um banco chamado ahmao_db.
- Certifique-se de ter um usuário e senha válidos.
#### 2. Configure o Arquivo .env
- Na raiz do projeto, você encontrará um arquivo chamado .env.example.
- Copie este arquivo e renomeie a cópia para .env.
- Abra o novo arquivo e preencha com suas informações locais:
```bash
# .env
SECRET_KEY='gere_e_cole_uma_nova_chave_secreta_aqui'
DEBUG=True
DB_NAME=ahmao_db
DB_USER=seu_usuario_postgres
DB_PASSWORD=sua_senha_do_postgres
DB_HOST=localhost
DB_PORT=5432
```

### 🔹 Opção 2: Instalação Rápida (com SQLite)

#### 1. Modifique o `settings.py`

Abra o arquivo `ahmao/app/settings.py`.  
Encontre a seção `DATABASES` e altere da seguinte forma:

```python
# Comente a configuração PostgreSQL
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_HOST'),
#         'PORT': config('DB_PORT', cast=int),
#     }
# }

# Ative a configuração SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
``` 
#### 2. Configure o Arquivo .env (Simplificado)

Mesmo com SQLite, você ainda precisa criar o arquivo .env a partir do .env.example.
Mas só a SECRET_KEY precisa ser preenchida:

```bash
# .env
SECRET_KEY='gere_e_cole_uma_nova_chave_secreta_aqui'
DEBUG=True
```
As variáveis DB_... serão ignoradas.

---

## ✅ Passos Finais (Comuns a Ambas as Opções)

Após configurar seu banco de dados com a Opção 1 ou 2, finalize a instalação:

### 1. Aplique as Migrações do Banco de Dados
``` bash
python manage.py migrate
```
### 2. Crie um Superusuário (Opcional)

Para acessar a interface de administração do Django (/admin):
```bash
python manage.py createsuperuser
```

### 3. Inicie o Servidor
```bash
python manage.py runserver
```

Se tudo correu bem, sua API estará rodando em: http://127.0.0.1:8000/

---

## 📖 Documentação da API

Use uma ferramenta como Postman ou Insomnia para interagir com os endpoints. 
A seguir estão os endpoints disponíveis atualmente na API. A URL base para desenvolvimento local é http://127.0.0.1:8000.

### Endpoints de Autenticação e Conta (/api/auth/)

| Método     | Endpoint                  | Descrição                                                               | Autenticação         | Corpo (Body) de Exemplo                                                                 |
|------------|---------------------------|-------------------------------------------------------------------------|-----------------------|------------------------------------------------------------------------------------------|
| POST       | /api/auth/register/       | Registra um novo usuário.                                               | Não                   | `{"username": "...", "password": "...", "email": "...", "cpf": "...", "phone": "..."}`   |
| POST       | /api/auth/login/          | Autentica um usuário e retorna tokens de acesso e atualização.          | Não                   | `{"username": "...", "password": "..."}`                                                 |
| POST       | /api/auth/login/refresh/  | Gera um novo token de acesso usando um token de atualização válido.     | Não                   | `{"refresh": "seu_refresh_token"}`                                                       |
| GET        | /api/auth/me/             | Retorna os dados do perfil do usuário atualmente logado.                | Sim (Bearer Token)    | N/A                                                                                      |
| PUT/PATCH  | /api/auth/me/             | Atualiza os dados do perfil do usuário atualmente logado.               | Sim (Bearer Token)    | `{"first_name": "...", "email": "..."}`                                                  |

### Endpoints do Catálogo de Produtos (/api/catalogo/)

| Método | Endpoint                             | Descrição                                                     | Autenticação |
|--------|--------------------------------------|----------------------------------------------------------------|---------------|
| GET    | /api/catalogo/products/              | Lista todos os produtos disponíveis no catálogo.               | Não           |
| GET    | /api/catalogo/products/{id}/         | Retorna os detalhes de um produto específico pelo seu ID.      | Não           |
| GET    | /api/catalogo/categories/            | Lista todas as categorias de produtos.                         | Não           |
| GET    | /api/catalogo/craft-types/           | Lista todos os tipos de manualidade disponíveis.               | Não           |
| GET    | /api/catalogo/difficulties/          | Lista todos os níveis de dificuldade.                          | Não           |

### Acessar Rotas Protegidas:
Adicione o seguinte cabeçalho:
Authorization: Bearer <SEU_ACCESS_TOKEN>

---

## 👤 Autores

- **Bruno Alejandro**  
[LinkedIn](https://www.linkedin.com/in/brunoalejandrodev/)  
[GitHub](https://github.com/BrunoAlejandroDev/)
