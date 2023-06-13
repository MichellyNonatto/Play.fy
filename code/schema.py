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
             "email" VARCHAR(45) NOT NULL UNIQUE, 
             "senha" VARCHAR(12) NOT NULL, 
             "tipoUsuario" INT NOT NULL, 
             PRIMARY KEY("idUsuario" AUTOINCREMENT))""")
        
        #GENÊRO
        generoMusical = ("Rock", "Hip Hop", "Eletrônica", "Jazz", "Pagode", "MPB", "Reggae", "Samba", "Funk")
        c.execute("""CREATE TABLE IF NOT EXISTS GENERO (
            "idGenero" INTEGER,
            "nomeGenero" VARCHAR(45) NOT NULL,
            PRIMARY KEY ("idGenero" AUTOINCREMENT))""")

        #ADICIONANDO VALORES DE GENÊRO
        for n in range(len(generoMusical)):
            c.execute("""INSERT INTO GENERO (nomeGenero) VALUES (?);""", (generoMusical[n], ))

        #ALBÚM
        c.execute("""CREATE TABLE IF NOT EXISTS ALBUM (
            "idAlbum" INTEGER,
            "nomeAlbum" VARCHAR(45) NOT NULL,
            "idGenero" INTEGER,
            PRIMARY KEY ("idAlbum" AUTOINCREMENT),
            FOREIGN KEY (idGenero) REFERENCES GENERO (idGenero))""")
        
        #MÚSICA
        c.execute("""CREATE TABLE IF NOT EXISTS MUSICA(
            idMusica INTEGER,
            nomeMusica VARCHAR(45) NOT NULL,
            duracao INT NOT NULL,
            nomeArtista VARCHAR(45),
            idAlbum INTEGER,
            FOREIGN KEY (nomeArtista) REFERENCES USUARIO (nickname),
            FOREIGN KEY (idAlbum) REFERENCES ALBUM (idAlbum)
            )""")
        return conn
    
    except Error as e:
        print(e)