from assets.components import estiloTexto

class Usuarios:
    import sqlite3
    def __init__(self, conn):
        self.nickname = ""
        self.ultimoAcesso = ""
        self.email = ""
        self.senha = ""
        self.tipoUsuario = ""
        self.conn = conn
        self.cursor = self.conn.cursor()

    def mostrarAlbum(self):
        self.cursor.execute("SELECT idAlbum, nomeAlbum, nickname FROM ALBUM INNER JOIN USUARIO ON ALBUM.idUsuario = USUARIO.idUsuario ORDER BY nomeAlbum;")
        resultado = self.cursor.fetchall()
        if resultado:
            print("{:<40} {:<40} {:<40}".format(f"{estiloTexto(1,34,'idAlbum')}", f"{estiloTexto(1,34,'Nome')}",f"{estiloTexto(1,34,'Criador')}","\n"))
            for item in range(len(resultado)):
                print("{:<30} {:<30} {:<30}".format(resultado[item][0], resultado[item][1], resultado[item][2]))
        else:
            print(estiloTexto(35, 0, "Não encontramos nenhum álbum, seja você o primeiro a criar um!\n"))

    def mostraMusica(self, selecionar):
        self.cursor.execute("SELECT idMusica, nomeMusica, duracao, nomeArtista, nomeGenero, nomeAlbum FROM MUSICA LEFT JOIN GENERO ON MUSICA.idGenero = GENERO.idGenero INNER JOIN ALBUM ON MUSICA.idAlbum = ALBUM.idAlbum WHERE MUSICA.idAlbum = ? ORDER BY nomeMusica;", (selecionar, ))
        resultado = self.cursor.fetchall()
        if resultado:
            print("{:<40} {:<40} {:<40} {:<40} {:<40}".format(f"{estiloTexto(1,34,'idMusica')}", f"{estiloTexto(1,34,'Música')}", f"{estiloTexto(1,34,'Duração em minutos')}",f"{estiloTexto(1,34,'Artista')}",f"{estiloTexto(1,34,'Gênero')}",f"{estiloTexto(1,34,'Álbum')}","\n"))
            for item in resultado:
                musica = item[1] if item[1] is not None else ""
                duracao = item[2] if item[2] is not None else ""
                artista = item[3] if item[3] is not None else ""
                genero = item[4] if item[4] is not None else ""
                print("{:<30} {:<30} {:<30} {:<30} {:<30}".format(item[0], musica, duracao, artista, genero))
            return True
        else:
            print(estiloTexto(35, 0, "Não encontramos nenhuma música vinculada a este álbum.\n"))
            return False

class Perfil(Usuarios):
    def criarUsuario(self, usuario):
        self.cursor.execute("INSERT INTO USUARIO (nickname, ultimoAcesso, email, senha, tipoUsuario) VALUES (?, ?, ?, ?, ?);", usuario)
        self.conn.commit()
        print(estiloTexto(32, 1, f"\nPerfil criado com sucesso! Seja bem-vindo {usuario[0]}\n"))

    def conectarUsuario(self, usuario, data):
        self.cursor.execute("SELECT idUsuario FROM USUARIO WHERE nickname = ? and senha = ?;", usuario)
        validacao = self.cursor.fetchall()
        if validacao:
             self.cursor.execute("UPDATE USUARIO SET ultimoAcesso = ? WHERE idUsuario = ?;", (data, validacao[0][0])) 

    def getTipoUsuario(self, usuario):
        self.cursor.execute("SELECT tipoUsuario FROM USUARIO WHERE nickname = ? and senha = ?;", usuario)
        resultado = self.cursor.fetchall()
        for tupla in resultado:
            for list in tupla:
                indice = list
        return indice
    
    def mostrarUsuario(self):
        self.cursor.execute("SELECT nickname, email, tipoUsuario FROM USUARIO;")
        resultado = self.cursor.fetchall()
        if resultado:
            print("{:<40} {:<40} {:<40}".format(f"{estiloTexto(1,34,'Nickname')}", f"{estiloTexto(1,34,'E-mail')}", f"{estiloTexto(1,34,'Tipo Usuário')}\n"))
        for item in range(len(resultado)):
            print("{:<30} {:<30} {:<30}".format(resultado[item][0], resultado[item][1], resultado[item][2]))

    def alterarNickname(self, nickname, usuario):
        self.cursor.execute("SELECT idUsuario FROM USUARIO WHERE nickname = ? and senha = ?;", usuario)
        idUsuario = self.cursor.fetchone()[0]
        if idUsuario:
            self.cursor.execute("UPDATE USUARIO SET nickname = ? WHERE idUsuario = ?", (nickname, idUsuario))
            self.conn.commit()
            print(estiloTexto(1, 32, f"Nickname alterado com sucesso!\n"))
    
    def alterarSenha(self, senha, usuario):
        self.cursor.execute("SELECT idUsuario FROM USUARIO WHERE nickname = ? and senha = ?;", usuario)
        idUsuario = self.cursor.fetchone()[0]
        if idUsuario:
            self.cursor.execute("UPDATE USUARIO SET senha = ? WHERE idUsuario = ?", (senha, idUsuario))
            self.conn.commit()
            print(estiloTexto(1, 32, f"Sua senha foi alterada com sucesso!\n"))
    
    def visualizarEmail(self, usuario):
        self.cursor.execute("SELECT idUsuario FROM USUARIO WHERE nickname = ? and senha = ?;", (usuario))
        idUsuario = self.cursor.fetchone()
        print(idUsuario)
        if idUsuario:
            self.cursor.execute("SELECT email FROM USUARIO WHERE idUsuario = ?;", (idUsuario ))
            email = self.cursor.fetchone()[0]
        print(email)

class Artista(Usuarios):
    def criarAlbum(self, nomeAlbum, usuario):
        self.cursor.execute("SELECT idUsuario FROM USUARIO WHERE nickname = ? and senha = ?;", usuario)
        idUsuario = self.cursor.fetchone()[0]
        self.cursor.execute("INSERT INTO ALBUM (nomeAlbum, idUsuario) VALUES (?, ?);", (nomeAlbum, idUsuario))
        self.conn.commit()
        print(estiloTexto(1, 32, f"Álbum {nomeAlbum}, criado com sucesso!\n"))

    def mostrarAlbumArtista(self, usuario):
        self.cursor.execute("SELECT idUsuario FROM USUARIO WHERE nickname = ? and senha = ?;", usuario)
        idUsuario = self.cursor.fetchone()[0]
        if idUsuario:
            self.cursor.execute("SELECT idAlbum, nomeAlbum, nickname FROM ALBUM INNER JOIN USUARIO ON ALBUM.idUsuario = USUARIO.idUsuario WHERE USUARIO.idUsuario = ?;", (idUsuario,))
            resultado = self.cursor.fetchall()
            print("{:<40} {:<40} {:<40}".format(f"{estiloTexto(1,34,'idAlbum')}", f"{estiloTexto(1,34,'Nome')}", f"{estiloTexto(1,34,'Criador')}","\n"))
            if resultado:
                for item in range(len(resultado)):
                    print("{:<30} {:<30} {:<30}".format(resultado[item][0], resultado[item][1], resultado[item][2]))
                return True
            else:
                print(estiloTexto(35, 0, "Não encontramos nenhum álbum vinculado ao seu perfil!\n"))
                return False
        
    def apagarAlbum(self, idAlbum, usuario):
        self.cursor.execute("SELECT idUsuario FROM USUARIO WHERE nickname = ? and senha = ?;", usuario)
        idUsuario = self.cursor.fetchone()[0]
        self.cursor.execute("SELECT nomeAlbum FROM ALBUM WHERE idAlbum= ? and idUsuario = ?", (idAlbum, idUsuario, ))
        nomeAlbum = self.cursor.fetchone()[0]
        self.cursor.execute("DELETE FROM MUSICA WHERE idAlbum = ?;", (idAlbum, ))
        self.cursor.execute("DELETE FROM ALBUM WHERE idAlbum = ?;", (idAlbum, ))
        self.conn.commit()
        print(estiloTexto(32, 1, f"Álbum {nomeAlbum}, foi deletado com sucesso!"))

    def criarMusica(self, musica):
        self.cursor.execute("""SELECT idAlbum, idGenero FROM GENERO INNER JOIN ALBUM WHERE  idAlbum = ? and idGenero = ?""", (musica[3], musica[4], ))
        verificar = self.cursor.fetchone()
        if verificar:
            self.cursor.execute("INSERT INTO MUSICA (nomeMusica, duracao, nomeArtista, idAlbum, idGenero) VALUES (?, ?, ?, ?, ?);", musica)
            self.conn.commit()
            print(estiloTexto(32, 1, f"{musica[0]} foi adicionado com sucesso!"))
            return True
        else: 
            return False
    
    def mostrarGenero(self):
       self.cursor.execute("SELECT * FROM GENERO;")
       resultado = self.cursor.fetchall()
       if resultado:
        print("{:<30} {:<30}".format(f"{estiloTexto(1,34,'Id')}", f"{estiloTexto(1,34,'Nome')}","\n"))
        for item in range(len(resultado)):
          print("{:<20} {:<20} ".format(resultado[item][0], resultado[item][1]))
    
    def apagarMusica(self, musica, usuario):
        self.cursor.execute("SELECT idUsuario FROM USUARIO WHERE nickname = ? and senha = ?;", usuario)
        idUsuario = self.cursor.fetchone()[0]
        self.cursor.execute("SELECT nomeMusica FROM MUSICA INNER JOIN ALBUM ON MUSICA.idAlbum = ALBUM.idAlbum WHERE ALBUM.idUsuario = ? AND MUSICA.idMusica = ?;", (idUsuario, musica[1]))
        nomeMusica = self.cursor.fetchone()[0]
        if nomeMusica:
            self.cursor.execute("DELETE FROM MUSICA WHERE MUSICA.idAlbum = ? AND MUSICA.idMusica = ?", (musica))
            self.conn.commit()
            print(estiloTexto(32, 1, f"Música {nomeMusica}, foi deletada com sucesso!"))

class Ouvinte(Usuarios):
    def pesquisarArtista(self, nomeArtista):
        self.cursor.execute('SELECT idAlbum, nickname, nomeAlbum FROM ALBUM INNER JOIN USUARIO ON ALBUM.idUsuario = USUARIO.idUsuario WHERE USUARIO.nickname = ? ORDER BY nomeAlbum;', (nomeArtista,))
        resultado = self.cursor.fetchall()

        if resultado:
            print("{:<40} {:<40} {:<40}".format(f"{estiloTexto(1,34,'idAlbum')}",f"{estiloTexto(1,34,'Artista')}", f"{estiloTexto(1,34,'Álbum')}","\n"))
            for item in resultado:
                print("{:<30} {:<30} {:<30}".format(item[0], item[1], item[2]))
            return True
        else:
            print(estiloTexto(35, 0, "Não encontramos nenhum álbum vinculado a este artista.\n"))
            return False
        
    def pesquisarMusica(self, nomeMusica):
        self.cursor.execute('SELECT nomeMusica, duracao, nomeArtista, nomeAlbum FROM MUSICA INNER JOIN ALBUM ON MUSICA.idAlbum = ALBUM.idAlbum WHERE MUSICA.nomeMusica = ? ORDER BY nomeMusica;', (nomeMusica,))
        resultado = self.cursor.fetchall()
        if resultado:
            print("{:<40} {:<40} {:<40} {:<40}".format(f"{estiloTexto(1,34,'Música')}", f"{estiloTexto(1,34,'Duração')}",f"{estiloTexto(1,34,'Artista')}",f"{estiloTexto(1,34,'Álbum')}","\n"))
            for item in resultado:
                print("{:<30} {:<30} {:<30} {:<30}".format(item[0], item[1],item[2], item[3]))
            return True
        else:
            print(estiloTexto(35, 0, "Não encontramos nenhuma música com esse nome.\n"))
            return False

