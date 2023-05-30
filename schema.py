import sqlite3
from sqlite3 import Error

def criarBanco(nomeBanco):
    conn = sqlite3.connect(nomeBanco)
    c = conn.cursor()

    try:
        #TABELA USUÁRIO
        c.execute("""CREATE TABLE IF NOT EXISTS "USUARIO" ("idUsuario" INTEGER NOT NULL, "nickname" VARCHAR(45) NOT NULL UNIQUE, "email" VARCHAR(45) NOT NULL, "senha" VARCHAR(12) NOT NULL, "tipoUsuario" VARCHAR(45) NOT NULL), PRIMARY KEY("idUsuario" AUTOINCREMENT);""")

        #

        return conn
    
    except Error as e:
        print(e)


        





