import schema
from assets import usuario

def menu():
    
    print(22 * "\033[1;36m*\033[m")
    print("\033[1;36m*** Menu de Opções ***\033[m")
    print(22 * "\033[1;36m*\033[m")
    print("\033[m1. Cadastra-se\n2. Login\033[m")
    selecao = int(input("\033[1;mSelecione uma opção: \033[m"))
    return selecao

if __name__ == '__main__':
    banco = input("Informe o nome do arquivo: ")
    conn = schema.criarBanco(banco)
    
    user = usuario.Usuarios(conn)


