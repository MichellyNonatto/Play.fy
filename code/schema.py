import sqlite3
from sqlite3 import Error

def criarBanco(nomeBanco):
    conn = sqlite3.connect(nomeBanco)
    c = conn.cursor()

    try:
        #TABELA USUÁRIO
        c.execute("""CREATE TABLE IF NOT EXISTS USUARIO (
            "idUsuario" INTEGER,
             "nickname" VARCHAR(45) NOT NULL UNIQUE,
             "ultimoAcesso" DATE, 
             "email" VARCHAR(45) NOT NULL, 
             "senha" VARCHAR(12) NOT NULL, 
             "tipoUsuario" INT NOT NULL, 
             PRIMARY KEY("idUsuario" AUTOINCREMENT))""")
        return conn
    
    except Error as e:
        print(e)