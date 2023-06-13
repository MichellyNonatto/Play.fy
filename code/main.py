import schema

from assets import usuario
from assets import style
from sqlite3 import Error

def menu():
    opcoes = {
        "1": "Fazer Cadastro",
        "2": "Fazer Login",
        "0": "Sair",
    }
    
    while True:
        style.titulo("Menu Inicial")
        for k, v in opcoes.items():
            print(f"|{f' {k} - {v}':{30}}|")
        print(f"+{'-' * 30}")
        op = input(style.styleText(0, 33, 'Selecione uma das opções:\t'))
        if op not in opcoes:
            print(style.styleText(7, 31, "\nOpção inválida!"))
            style.limparTela()
        else:
            break
    return op

def submenu():

    return

if __name__ == '__main__':
    from getpass import getpass
    style.limparTela()
    getpass("="*70+f"\n\n\t{style.styleText(0,35,'Bem-vido ao Play.fy, seu gerenciador de músicas ♪')}\n\n"+"="*70+f"\n\nClique '{style.styleText(32,1,'ENTER')}' para continuar...")
    style.limparTela()
    print(style.styleText(0, 32, "Conenctando com o banco..."))
    from time import sleep
    sleep(2)
    conn = schema.criarBanco('bancoDeDadosPlayFy.txt')
    
    user = usuario.Usuarios(conn)


    while True:
        tabela = menu()
        from datetime import date
        ultimoAcesso = date.today()
        if tabela == "0":
            style.limparTela()
            print(style.styleText(0, 33, "Encerrando o programa...\n"))
            break      
        elif tabela == "1":
            style.limparTela()
            style.titulo("Menu - Cadastro")
            while True:
                nickname = input("\nInsira o seu nickname:\t").lower()
                if len(nickname) < 3: print(style.styleText(0, 33,"O nickname deve ter no mínimo 3 caracteres."))
                else: break
            while True:
                import re
                email = input("\nInsira o endereço de e-mail: ").lower()
                if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email): break 
                else: print(style.styleText(0, 33,f"Informe um e-mail válido. Exemplo {nickname}2023@gmail.com"))
            while True:
                senha = input("\nInsira sua senha: ")
                if len(senha) < 8: print(style.styleText(0, 33,"A senha deve ter no mínimo 8 caracteres."))
                else: break

            listaTipoUsuario = {
                "1": "Artista",
                "2": "Ouvinte",
                "0": "Cancelar Cadastro"
            }

            while True:
                style.limparTela()
                style.titulo("Tipo usuário")
                for k, v in listaTipoUsuario.items():
                    print(f"|{f' {k} - {v}':{30}}|")
                print(f"+{'-' * 30}")
                tipoUsuario = input(style.styleText(0, 33, 'Selecione uma das opções:\t'))
                if tipoUsuario not in listaTipoUsuario:
                    print(style.styleText(7, 31, "\nOpção inválida!"))
                    continue
                elif tipoUsuario == '0':
                    print(style.styleText(0, 32, "Cadastro do usuário cancelado."))
                    break
                else:
                    novoUsuario = (nickname, ultimoAcesso, email, senha, tipoUsuario, )

                try:
                    user.criarUsuario(novoUsuario)
                    sleep(5)
                except:
                    style.limparTela()
                    print(style.styleText(0, 33, "Nickname ou e-mail já existente em nossa plataforma, faça o login para acessar a sua conta."))
                    sleep(3)
                break
        elif tabela == "2":
            while True:
                style.limparTela()
                style.titulo("Menu - Login")
                nickname = input("\nInsira o seu nickname:\t")
                senha = input("Insira a sua senha: ")

                if not nickname or not senha: 
                    style.limparTela()
                    print(style.styleText(0, 33, "Os campos nickname e senha não podem estar vazios."))
                    sleep(3)
                    continue
                else: break
                        
            usuario = (nickname, senha, )
            loginUsuario = (usuario)
        continue       


style.limparTela()
print(style.styleText(0, 32, "Programa finalizado com sucesso!\n"))
user.mostrarUsuario()
print("\n")