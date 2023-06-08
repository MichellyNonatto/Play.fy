import style
class Usuarios:
  import sqlite3
  def __init__(self, conn):
    from datetime import date
    self.nickname = ""
    self.ultimoAcesso = date.today()
    self.email = ""
    self.senha = ""
    self.tipoUsuario = ""
    self.conn = conn
    self.cursor = self.conn.cursor()

  def criarUsuario(self, usuario):
    self.cursor.execute("INSERT INTO USUARIO (nickname, email, senha, tipoUsuario) VALUES (?, ?, ?, ?);", usuario)
    self.conn.commit()
    return print(f"Perfil criado com sucesso! Seja bem vindo '{style(1, 32, usuario[0])}'.")
  
  def mostrarUsuario(self):
    self.cursor.execute("SELECT * FROM USUARIO")
    resultado = self.cursor.fetchall()
    if resultado:
      for item in range(len(resultado)):
        print(resultado[item][0], resultado[item][1], resultado[item][2], resultado[item][3], resultado[item][4], resultado[item][5])
      input(f"Clique '{style.styleText(32,1,'ENTER')}' para continuar...")
      return print("\033[32mConsulta concluída com sucesso!\033[m\n")
    