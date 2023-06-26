import os
from time import sleep
from getpass import getpass
global tam
tam = 40

def interacao(n=1):
    if n == 1:
        getpass(estiloTexto(0, 33, "Clique ENTER para continuar..."))
    else:
        sleep(3)

def limparTela():
    if os.name == 'posix':
         _ = os.system('clear')
    else:
        _ = os.system('cls')

def estiloTexto(cor, fonte, text):
    estilo = f'\033[{cor};{fonte}m'+text+'\033[m'
    return estilo

def estiloTitulo(texto, espaco = 1):
    print(f"+{'-' * tam}+",) 
    print(("\t" * espaco),f"{estiloTexto(35, 1, texto)}")
    print(f"+{'-' * tam}+")

def validarOpcao(titulo, dictOpcoes):
    while True:
        limparTela()
        estiloTitulo(titulo)

        for i, j in dictOpcoes.items():
            print(f"| {f'{i} - {j}':{tam}}|")
        print(f"+{'-' * tam}+")

        try:
            opcao = int(input("Selecione uma das opções acima:\t"))
        except:
            print(estiloTexto(0, 33, "\nInsira somente os números informado na tela."))
            interacao(0)
            continue

        opcao = str(opcao)
        if opcao not in dictOpcoes:
            print(estiloTexto(0, 33, "\nOpção inválida!"))
            interacao(0)   
        else: 
            break

    return opcao

def validarVariavel(titulo, textoInput):
    while True:
        limparTela()
        estiloTitulo(titulo)
        valor = input(textoInput).lower()
        if not valor:
            print(estiloTexto(0, 33, "\nEsse campo não pode estar vazio."))
            interacao(0)
        elif len(valor) < 3:
            print(estiloTexto(0, 33, "\nÉ necessário inserir mais de 3 caracteres."))
            interacao(0)
        else:
            return valor
        
def validarInteiro(textoInput, lpTela = 0, comTitulo = None):
    if lpTela == 0:
        try:
            valor = int(input(textoInput))
            return valor
        except ValueError:
            print(estiloTexto(0, 33, "\nInsira somente números inteiros."))
            interacao(0)
            return False
    else:
        while True:
            limparTela()
            estiloTitulo(comTitulo)
            try:
                valor = int(input(textoInput))
                return valor
            except ValueError:
                print(estiloTexto(0, 33, "\nInsira somente números inteiros."))
                interacao(0)
            
        
import matplotlib.pyplot as plt
import sqlite3

def gerarGrafico():
    conn = sqlite3.connect('bancoDeDadosPlayFy.txt')
    cursor = conn.cursor()

    # Consulta SQL para obter a contagem de músicas por gênero
    query = "SELECT GENERO.nomeGenero, COUNT(*) FROM MUSICA JOIN GENERO ON MUSICA.idGenero = GENERO.idGenero GROUP BY GENERO.idGenero"
    cursor.execute(query)
    result = cursor.fetchall()

    # Extrai os dados do resultado da consulta
    generos = [row[0] for row in result]
    quantidade_musicas = [row[1] for row in result]

    # Plotar o gráfico de barras
    plt.bar(generos, quantidade_musicas)
    plt.xlabel('Gênero')
    plt.ylabel('Quantidade de Músicas')
    plt.title('Quantidade de Músicas por Gênero')
    plt.xticks(rotation=45)
    plt.show()

    conn.close()