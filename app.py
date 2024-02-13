'''
--> Criar Docker container MySQL <--

docker run -d --rm --name=mysql \
-v $PWD/dados:/var/lib/mysql \
-p 3306:3306 \
-e MYSQL_ROOT_PASSWORD=mysql \
-e MYSQL_ROOT_HOST=% \
-e MYSQL_DATABASE=db_users \
-e MYSQL_USER=tux \
-e MYSQL_PASSWORD=ABC123xyz \
mysql \
--default-authentication-plugin=mysql_native_password

mariadb -utux -p -h 127.0.0.1 db_users

'''

#-------------------------------------------------------------------

from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine, text
import os
from credenciais import db_config

app = Flask(__name__)

user = db_config['user']
pw   = db_config['password']
url  = db_config['host']     
db   = db_config['database']


# Connect to the database
engine = create_engine(f"mysql+mysqlconnector://{user}:{pw}@{url}/{db}")    
connection = engine.connect()

query_create_table = '''
CREATE TABLE IF NOT EXISTS users (
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(50) NOT NULL,
fone VARCHAR(50) NOT NULL,
email VARCHAR(50) NOT NULL
);
'''
connection.execute(text(f"{query_create_table}"))


def select():
    global lista
    lista = []
    result = connection.execute(text("SELECT * FROM users"))         
    for row in result:
        lista.append(row)
    # print(f'Select ==> {lista}')


lista = []
select()


@app.get("/")
def home():       
    return render_template("base.html", lista_front=lista)


@app.post("/add")
def add():
    user = []    
    nome  = request.form.get("nome")
    fone  = request.form.get("fone")
    email = request.form.get("email")

    if nome != '' and fone != '' and email != '':        
        user.append(nome)
        user.append(fone)
        user.append(email)

        try:
            query_insert = f"INSERT INTO users (nome, fone, email) \
            VALUES ('{nome}', '{fone}', '{email}')"

            connection.execute(text(query_insert))
            connection.execute(text("COMMIT"))
            select()  
        except:
            print('Falha no "insert"')                             
    else:
        print('** Usuário não cadastrato, todos os dados devem ser fornecidos **')    
    return redirect(url_for("home"))


@app.post("/sort")
def sort():
    if lista != []:
        print(f'** Ordenando a lista **')
        lista.sort(key=lambda x: x[1])       
    return redirect(url_for("home"))


@app.post("/reverse")
def reverse():
    global lista
    if lista != []:
        print(f'** Invertendo a lista **')        
        lista = sorted(lista, reverse=True, key=lambda x: x[1])
    return redirect(url_for("home"))


@app.post("/clear")
def clear():    
    print(f'==> Apagando todos registros do banco de dados <==')
    lista_id = []
    try:
        result = connection.execute(text("SELECT id FROM users"))         
        for row in result:
            lista_id.append(row[0])
        for id in lista_id:
            connection.execute(text(f"DELETE FROM users WHERE id = {id}"))
        connection.execute(text("COMMIT"))    
        select()
    except:
        print('Falha em "limpar tabela"')
    return redirect(url_for("home"))


@app.get("/delete/<id_banco>")
def delete(id_banco):
    id = id_banco
    print(f'==> Removendo Id: {id}')
    try:
        connection.execute(text(f"DELETE FROM users WHERE id = {id}"))
        connection.execute(text("COMMIT"))
        select()
    except:
        print('Falha ao excluir usuário')         
    return redirect(url_for("home"))


if __name__ == '__main__':    
    app.run(host="0.0.0.0", debug=True)    