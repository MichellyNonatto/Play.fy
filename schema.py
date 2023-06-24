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
        generoMusical =["Rock", "Hip Hop", "Eletrônica", "Jazz", "Pagode", "MPB", "Reggae", "Samba", "Funk", "Pop", "Samba", "Forró", "Metal"]
        c.execute("""CREATE TABLE IF NOT EXISTS GENERO (
            "idGenero" INTEGER,
            "nomeGenero" VARCHAR(45) NOT NULL UNIQUE,
            PRIMARY KEY ("idGenero" AUTOINCREMENT))""")
        
        #ADICIONANDO GENÊRO A TABELA
        c.execute("""SELECT nomeGenero FROM GENERO""")
        resultado = c.fetchall()
        for item in generoMusical:
            try:
                c.execute("""INSERT INTO GENERO (nomeGenero) VALUES (?);""", (item, ))
                conn.commit()
            except:
                pass
        
        #ÁLBUM
        c.execute("""CREATE TABLE IF NOT EXISTS ALBUM (
            "idAlbum" INTEGER,
            "nomeAlbum" VARCHAR(45) NOT NULL UNIQUE,
            "idUsuario" INTEGER,
            PRIMARY KEY ("idAlbum" AUTOINCREMENT),
            FOREIGN KEY (idUsuario) REFERENCES USUARIO (idUsuario))""")
        
        #MÚSICA
        c.execute("""CREATE TABLE IF NOT EXISTS MUSICA(
            "idMusica" INTEGER,
            "nomeMusica" VARCHAR(45) NOT NULL,
            "duracao" INT NOT NULL,
            "nomeArtista" VARCHAR(45),
            "idAlbum" INTEGER,
            "idGenero" INTEGER,
            PRIMARY KEY ("idMusica" AUTOINCREMENT),
            FOREIGN KEY (nomeArtista) REFERENCES USUARIO (nickname),
            FOREIGN KEY (idAlbum) REFERENCES ALBUM (idAlbum),
            FOREIGN KEY (idGenero) REFERENCES GENERO (idGenero)) """)

        return conn

    except Error as e:
        return e