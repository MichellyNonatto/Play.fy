from assets import style

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

  def criarUsuario(self, usuario):
    self.cursor.execute("INSERT INTO USUARIO (nickname, ultimoAcesso, email, senha, tipoUsuario) VALUES (?, ?, ?, ?, ?);", usuario)
    self.conn.commit()
    print(f"\nPerfil criado com sucesso! Seja bem vindo '{style.styleText(1, 32, usuario[0])}'.")
  
  def conectarUsuario(self, usuario, data):
    self.cursor.execute("SELECT nickname, senha FROM USUARIO WHERE nickname = ? and senha = ?;", usuario)
    validacao = self.cursor.fetchall()
    if len(validacao) != 0:
      self.cursor.execute("UPDATE USUARIO SET ultimoAcesso = ? WHERE nickname = ?;", (data, usuario[0]))
      print(f"\n'{style.styleText(1, 32, usuario[0])}', seja bem-vindo ao Play.Fy.")
    else: 
      print(style.styleText(0, 33, "\nNickname ou senha incorretos, tente novamente ou faça o seu cadastro."))

  def mostrarUsuario(self):
    self.cursor.execute("SELECT nickname, email, tipoUsuario FROM USUARIO")
    resultado = self.cursor.fetchall()
    if resultado:
      print("{:<30} {:<40} {:<30}".format(f"{style.styleText(1,34,'Nickname')}", f"{style.styleText(1,34,'E-mail')}", f"{style.styleText(1,34,'Tipo Usuário')}\n"))
      for item in range(len(resultado)):
        print("{:<20} {:<30} {:<30}".format(resultado[item][0], resultado[item][1], resultado[item][2]))
    