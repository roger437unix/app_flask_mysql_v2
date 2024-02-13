![](https://static.javatpoint.com/tutorial/flask/images/flask-tutorial.png)


# Agenda Flask Python com Banco MySQL


### 1. Criar Docker container MySQL

docker run -d --rm --name=mysql
-v $PWD/dados:/var/lib/mysql
-p 3306:3306
-e MYSQL_ROOT_PASSWORD=mysql
-e MYSQL_ROOT_HOST=%
-e MYSQL_DATABASE=db_users
-e MYSQL_USER=tux
-e MYSQL_PASSWORD=ABC123xyz
mysql
--default-authentication-plugin=mysql_native_password


### 2. Conexão ao banco

mariadb -utux -p -h 127.0.0.1 db_users


### 3. Criar ambiente virtual

*python -m venv .venv*


### 4. Ativar o ambiente virtual

*source .venv/bin/activate*     ==> Linux <br/>
*source .venv/Scripts/activate* ==> Windows


### 5. Instalar os requisitos

*pip install -r requirements.txt*


### 6. Executar a aplicação

*python app.py*


### 7. Para sair do ambiente virtual Python

*deactivate*
