def styleText(cor, fonte, text):
    estilo = f'\033[{cor};{fonte}m'+text+'\033[m'
    return estilo
    
def titulo(text):
    limparTela()
    tam = 30
    print(f"+{'-' * tam}+")
    print(f"\t{styleText(35, 1, text)}")
    print(f"+{'-' * tam}+")

def limparTela():
    import os
    from time import sleep
    def  screen_clear():
        if os.name == 'posix':
            _ = os.system('clear')
        else:
            _ = os.system('cls')

    sleep(1)
    screen_clear()