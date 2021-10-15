# Projeto integrador - Logo Ali.

## 1 - Como executar o projeto.

### 1.1 - Requisitos.

Para executar esse projeto é necessário ter instalado no seu computador:

[x] Python >= 3.7
[x] Virtualenv

### 1.2 - Criando ambiente virtual e instalando pacotes.

Com virtualenv instalado basta executar o comando abaixo na pasta do projeto para criar um novo ambiente virtual.

Linux:

```sh
python3 -m virtualenv venv # criação do ambiente virtual.
source ./venv/bin/activate # para ativar ambiente virtual.
```

Windows:
```sh
virtualenv venv
./venv/Script/activate
```

Para instalar os pacotes basta executar o comando abaixo:

```
pip install -r requirements.txt
```

### 1.3 - Variaveis de ambiente para execução do projeto.

Definindo variaveis de ambiente em uma instancia local (nao há necessidade de criar variáveis de ambiente globais).

-- necessário para utilização do CLI para execução, criação do banco de dados e migrações.

Linux
```sh
export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True
```

Windows:
```sh
set FLASK_APP=app
set FLASK_ENV=Development
set FLASK_DEBUG=True
```

### 1.4 - Criando tabelas no banco de dados:

```sh
flask db init
flask db migrate
flask db upgrade
```

### 1.5 - Executando projeto.

1ª Forma:
```sh
python main.py
```

2ª Forma:
```sh
flask run
```

### 1.6 - Criando usuários.

Usanddo HTTPIE (pode usar outro client):

Instalando HTTPI
```sh
pip install httpie
```

Cadastrando um usuário:
```sh
http POST http://127.0.0.1:5000/user/signin name="Afonso Medeiros" email="afonso@afonso.com" password="123456"
```

Realizando login:
```sh
http POST http://127.0.0.1:5000/user/login email="afonso@afonso.com" password="123456"

HTTP/1.0 200 OK
Content-Length: 607
Content-Type: application/json
Date: Fri, 15 Oct 2021 07:18:23 GMT
Server: Werkzeug/2.0.2 Python/3.8.10

{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNDI4MjMwMywianRpIjoiODMwYjY2YTQtNTJmMy00NjM3LTkxNzEtYjY0NTk0YzhkYzgwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjM0MjgyMzAzLCJleHAiOjE2MzQyODMyMDN9.g94zTPJ7OH48OagLtikjUHZkdWlKqPzMcksxs1UEDeQ",
    "message": "Login succefull!",
    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNDI4MjMwMywianRpIjoiOWYzYjhjNWUtNDg1Yy00NjBmLTk3MmYtNjRlNmI1MzI1Mzc2IiwidHlwZSI6InJlZnJlc2giLCJzdWIiOjEsIm5iZiI6MTYzNDI4MjMwMywiZXhwIjoxNjM2ODc0MzAzfQ.Qo_2yl1ZM56oh19qflQ8cSExPiPOO5UpkECxMS5aU8A"
}
```