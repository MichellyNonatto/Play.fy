

class Usuarios:
  import sqlite3
  def __init__(self, conn):
    from datetime import date
    self.nickname = ""
    self.ultimoAcesso = ""
    self.email = ""
    self.senha = ""
    self.tipoUsuario = ""
    self.conn = conn
    self.cursor = self.conn.cursor()

  def criarUsuario(self, usuario):
        self.cursor.execute("INSERT INTO USUARIO (nickname, email, senha,   tipoUsuario) VALUES (?, ?, ?);", usuario)

   