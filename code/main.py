import schema

from assets import usuario
from assets import style

def menu():
    tam = 30

    opcoes = {
        "1": "Fazer Cadastro",
        "2": "Fazer Login",
        "0": "Sair",
    }
    
    while True:
        style.titulo("Menu Inicial")
        for k, v in opcoes.items():
            print(f"|{f' {k} - {v}':{tam}}|")
        print(f"+{'-' * tam}")
        op = input(style.styleText(0, 33, 'Selecione uma das opções:\t'))
        if op not in opcoes:
            print(style.styleText(7, 31, "\nOpção inválida!"))
            style.limparTela()
        else:
            break
    return op

if __name__ == '__main__':
    from getpass import getpass
    style.limparTela()
    getpass("="*70+f"\n\n\t{style.styleText(0,35,'Bem-vido ao Play.fy, seu gerenciador de músicas ♪')}\n\n"+"="*70+f"\n\nClique '{style.styleText(32,1,'ENTER')}' para continuar...")
    style.limparTela()
    print(style.styleText(0, 32, "Conenctando com o banco..."))
    from time import sleep
    sleep(2)
    conn = schema.criarBanco('bd.txt')
    
    user = usuario.Usuarios(conn)

    while True:
        tabela = menu()
        if tabela == "0":
            style.limparTela()
            print(style.styleText(0, 33, "Encerrando o programa...\n"))
            break      
        if tabela == "1":
            from sqlite3 import Error
            style.titulo(f"Menu - Cadastro")
            nickname = input("\nInsira o seu nickname:\t") 
            email = input("\nInsira o seu e-mail:\t")
            
            while True:
                senha = input("\nInsira sua senha:\t")
                if len(senha) < 8: print("Mínimo de caracter é 8.")
                else: break
                print("\b")

        listaTipoUsuario = {
            "1": "Artista",
            "2": "Ouvinte",
            "0": "Cancelar Cadastro"
        }

        while True:
            from sqlite3 import Error
            print("\nLista tipo usuário\n")
            for k, v in listaTipoUsuario.items():
                print(f"{k} - {v}")
            tipoUsuario = input(style.styleText(0, 33, 'Selecione uma das opções:\t'))
            if tipoUsuario not in listaTipoUsuario:
                print(style.styleText(7, 31, "\nOpção inválida!"))
            elif tipoUsuario == '0':
                print(style.styleText(0, 32, "Cadastro do usuário cancelada."))
                break
            else:
                novoUsuario = (nickname, email, senha, tipoUsuario, )

            try:
                user.criarUsuario(novoUsuario)
            except Error as e:
                style.limparTela()
                print("É necessário preencher todos os campos.")

style.limparTela()
print(style(0, 32, "Programa finalizado com sucesso!"))
        