from assets import components
from getpass import getpass
from datetime import date
from assets import user
from sqlite3 import Error
import schema

ultimoAcesso = date.today()

if __name__ == '__main__':
    components.limparTela()
    conn = schema.criarBanco("bancoDeDadosPlayFy.txt")

    print("=" * 70)
    print(f"\n\n\t{components.estiloTexto(0, 35, 'Bem-vindo ao Play.Fy, seu gerenciador de músicas ♪')}\n\n")
    print("=" * 70)
    components.interacao()

    artista = user.Artista(conn)
    ouvinte = user.Ouvinte(conn)
    usuario = user.Perfil(conn)

    opcao = 1
    while opcao != 0:
        dictOpcoes = {
        '1': 'Fazer Cadastro',
        '2': 'Fazer Login',
        '0': 'Finalizar o programa',
        }
        opcao = components.validarOpcao("Menu Inicial", dictOpcoes)
        
        #SAIR DO PROGRAMA
        if opcao == '0':
            components.limparTela()
            print(components.estiloTexto(0, 36, "Finalizando o programa..."))
            components.interacao(0)
            break

        #CRIAR USUÁRIO
        elif opcao == '1':
            cirarNickname = components.validarVariavel(dictOpcoes[opcao], "Insira o seu nickname:\t")
            while True:
                import re
                criarEmail = components.validarVariavel(dictOpcoes[opcao], "Insira o seu e-mail:\t")
                if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', criarEmail): break 
                else: 
                    print(components.estiloTexto(0, 33, f"\nInforme um e-mail válido.\nExemplo {cirarNickname}2023@gmail.com\n"))
                    components.interacao()
            criarSenha = components.validarVariavel(dictOpcoes[opcao], "Informe a sua senha:\t")
            
            dictTipoUsuario = {
                '1': 'Artista',
                '2': 'Ouvinte',
                '0': 'Cancelar Cadastro'
            }

            tipoUsuario = components.validarOpcao(dictOpcoes[opcao], dictTipoUsuario)
            tipoUsuario = int(tipoUsuario)

            if tipoUsuario == 0:
                break
            else:
                novoUsuario = (cirarNickname, ultimoAcesso, criarEmail, criarSenha, tipoUsuario, )
                try:
                    usuario.criarUsuario(novoUsuario)
                except Error as e:
                    components.limparTela()
                    print(components.estiloTexto(0, 33, "Nickname ou e-mail já existente em nossa plataforma, faça o login para acessar a sua conta.\n"))
                components.interacao(0)
                continue

        #LOGIN USUÁRIO
        elif opcao == '2':
            components.limparTela()
            loginNickname = components.validarVariavel(dictOpcoes["2"], "Insira o seu nickname:\t")
            
            while True:
                components.limparTela()
                components.estiloTitulo(dictOpcoes["2"])
                get_password = lambda prompt: getpass(prompt)
                loginSenha = get_password("Informe a sua senha:\t")
                if not loginSenha:
                    print(components.estiloTexto(0, 33, "\nEsse campo não pode estar vazio."))
                    components.interacao(0)
                elif len(loginSenha) < 3:
                    print(components.estiloTexto(0, 33, "\nÉ necessário inserir mais de 3 caracteres."))
                    components.interacao(0)
                else:
                    break
            
            conectarUsuario = (loginNickname, loginSenha, )
            try:
                usuario.conectarUsuario(conectarUsuario, ultimoAcesso)
                tipoUsuario = usuario.getTipoUsuario(conectarUsuario)
            except:
                components.limparTela()
                print(components.estiloTexto(0, 33, f"Nickname ou senha incorretos, tente novamente ou faça o seu cadastro.\n\nCaso lembre o seu e-mail selecione '\033[1;35m3 - Recuperar conta\033[m' \033[33mno Menu Inicial.\033[m\n"))
                components.interacao()
                continue
        
            #PERFIL CONECTADO
            while True:
                if tipoUsuario == 1:
                    dictArtista = {
                    '1':'Criar Álbum',
                    '2':'Vizualizar Álbum',
                    '3':'Excluir Álbum',
                    '4':'Adicionar Música',
                    '5':'Vizualizar Música',
                    '6':'Excluir Música',
                    '7':'Configurações',
                    '0':'Sair da conta'
                    }
                    opcaoAcao = components.validarOpcao(f"{conectarUsuario[0]}\tArtista", dictArtista)

                    #VOLTAR AO MENU PRINCIPAL
                    if opcaoAcao == '0':
                        break
                    #CRIAR UM ALBUM
                    elif opcaoAcao == '1':
                        nomeAlbum = components.validarVariavel(dictArtista['1'], "Insira o nome do album:\t")
                        artista.criarAlbum(nomeAlbum, conectarUsuario)
                        components.interacao(0)

                    #MOSTRAR ALBUM
                    elif opcaoAcao == '2':
                        components.limparTela()
                        components.estiloTitulo(dictArtista['2'])
                        artista.mostrarAlbum()
                        components.interacao()

                    #DELETAR ALBUM
                    elif opcaoAcao == '3':
                        while True:
                            components.limparTela()
                            components.estiloTitulo(dictArtista['3'])
                            if artista.mostrarAlbumArtista(conectarUsuario) == True:
                                try:
                                    idAlbum = int(input("\nnInsira o idAlbum que será deletado:\t"))
                                    artista.apagarAlbum(idAlbum, conectarUsuario)
                                    components.interacao(0)
                                    break
                                except:
                                    print(components.estiloTexto(0, 33, "\nInsira somente os números informado na tela."))
                                    components.interacao(0)
                                    continue
                            else:
                                components.interacao()
                                break

                    #CRIAR MÚSICA
                    elif opcaoAcao == '4':
                        adicionarMusica = components.validarVariavel(dictArtista['4'], "Informe o nome da música:\t")
                        duracoMusica = components.validarInteiro(f"Informe a duração de {adicionarMusica}:\t", 1, dictArtista['4'])
                        float(duracoMusica)
                        duracoMusica = duracoMusica/60
                        duracoMusica = round(duracoMusica, 2)                
                        
                        while True:
                            components.limparTela()
                            components.estiloTitulo(dictArtista['4'])
                            if artista.mostrarAlbumArtista(conectarUsuario) == True:
                                idAlbum = components.validarInteiro(f"Informe o idAlbum de {adicionarMusica}:\t")
                                if idAlbum == False:
                                    components.limparTela()
                                    continue
                                components.estiloTitulo(dictArtista['4'])
                                artista.mostrarGenero()
                                idGenero = components.validarInteiro(f"Informe o idGenero de {adicionarMusica}:\t")
                                if idGenero == False:
                                    components.limparTela()
                                    continue

                                novaMusica = (adicionarMusica, duracoMusica, conectarUsuario[0], idAlbum, idGenero)
                                    
                                if artista.criarMusica(novaMusica) == True:
                                    components.interacao(0)
                                    break
                                else:
                                    print(components.estiloTexto(0, 33, "\nidAlbum ou idGenero informado é um valor inválido"))
                                    components.interacao(0)
                                    continue
                                    
                            else:
                                components.interacao(0)
                                break
                            
                    #VIZUALIZAR MÚSICA
                    elif opcaoAcao == '5':
                        dictVizualizarMusica = {
                            '1':'Minhas músicas',
                            '2':'Outras músicas',
                            '3':'Música por categoria',
                            '0':'Voltar'
                        }
                        while True:
                            opcaoVizualizarMusica = components.validarOpcao(f"{conectarUsuario[0]}\tArtista", dictVizualizarMusica)

                            if opcaoVizualizarMusica == '1':
                                while True:
                                    components.limparTela()
                                    components.estiloTitulo(dictVizualizarMusica['1'])
                                    if artista.mostrarAlbumArtista(conectarUsuario) == True:
                                        idAlbumVizualizarMusica = components.validarInteiro("Informe o idAlbum para consultar:\t")
                                        if idAlbumVizualizarMusica == False:  
                                            components.limparTela()
                                            continue
                                        components.limparTela()
                                        components.estiloTitulo(dictVizualizarMusica['1'])
                                        artista.mostraMusica(idAlbumVizualizarMusica)
                                        components.interacao()
                                        break
                                    else:
                                        components.interacao()
                                        break

                            
                            elif opcaoVizualizarMusica == '2':
                                while True:
                                    components.limparTela()
                                    components.estiloTitulo(dictVizualizarMusica['1'])
                                    artista.mostrarAlbum()
                                    idAlbumVizualizarMusica = components.validarInteiro("Informe o idAlbum para consultar:\t")
                                    if idAlbumVizualizarMusica == False:
                                        components.limparTela()
                                        continue
                                    components.limparTela()
                                    components.estiloTitulo(dictVizualizarMusica['1'])
                                    artista.mostraMusica(idAlbumVizualizarMusica)
                                    components.interacao()
                                    break
                            elif opcaoVizualizarMusica == '3':
                                components.gerarGrafico()
                                components.interacao()
                            elif opcaoVizualizarMusica == '0':
                                break
                            else:
                                print(components.estiloTexto(0, 33, "\nOpção inválida!"))
                                components.interacao(0) 

                    #EXCLUIR MÚSICA
                    elif opcaoAcao == '6':
                        while True:
                            components.limparTela()
                            components.estiloTitulo(dictArtista['6'])
                            if artista.mostrarAlbumArtista(conectarUsuario) == True:
                                try:
                                    idAlbumExcluirMusica = int(input("Informe o idAlbum para consultar:\t"))
                                    components.limparTela()
                                    components.estiloTitulo(dictArtista['6'])
                                    if artista.mostraMusica(idAlbumExcluirMusica) == True:
                                        idMusicaExcluirMusica = int(input("Informe o idMuscia para excluir:\t"))
                                    else:
                                        components.interacao(0)
                                        break

                                except:
                                    print(components.estiloTexto(0, 33, "\nInsira somente números inteiros."))
                                    components.interacao(0)
                                    continue
                                try:
                                    excluirMusica = (idAlbumExcluirMusica,idMusicaExcluirMusica, )
                                    artista.apagarMusica(excluirMusica,conectarUsuario)
                                    components.interacao(0)
                                except:
                                    print(components.estiloTexto(0, 33, "\nidAlbum ou idGenero informado é um valor inválido"))
                                    components.interacao(0)
                                break
                            else:
                                components.interacao(0)
                                break
                    
                    #EDITAR CONTA
                    elif opcaoAcao == '7':
                        dictConta = {
                        '1':'Alterar nickname',
                        '2':'Alterar senha',
                        '3':'Vizualizar E-mail',
                        '0':'Voltar'
                        }
                        
                        while True:
                            opcaoConfiguracao = components.validarOpcao(dictArtista['7'], dictConta)

                            if opcaoConfiguracao == '1':
                                novoNickname = components.validarVariavel(dictConta['1'], "Informe o seu novo nickname:\t")
                                try:
                                    usuario.alterarNickname(novoNickname, conectarUsuario)
                                    components.interacao(0)
                                except:
                                    print(components.estiloTexto(0, 33, "Esse nickname já existente em nossa plataforma.\n"))
                                    components.interacao()
                            elif opcaoConfiguracao == '2':
                                novaSenha = components.validarVariavel(dictConta['2'], "Informe sua nova senha:\t")
                                usuario.alterarSenha(novaSenha, conectarUsuario)
                                components.interacao(0)
                            elif opcaoConfiguracao == '3':
                                components.limparTela()
                                components.estiloTitulo(dictConta['3'])
                                usuario.visualizarEmail(conectarUsuario)
                                components.interacao()
                            else:
                                break
                        
                elif tipoUsuario == 2:
                    dictOuvinte = {
                        '1':'Pesquisar artista',
                        '2':'Pesquisar música',
                        '3':'Vizualizar álbum',
                        '4':'Vizualizar música',
                        '5':'Configuraçoes',
                        '0':'Sair'
                    }
                    opcaoAcao = components.validarOpcao(f"{conectarUsuario[0]}\t\tOuvinte", dictOuvinte)

                    if opcaoAcao == '1':
                        nomeArtista = components.validarVariavel(dictOuvinte['1'], "Informe o nome do artista:\t")
                        components.limparTela()
                        components.estiloTitulo(dictOuvinte['1'])
                        ouvinte.pesquisarArtista(nomeArtista)
                        components.interacao()
                    elif opcaoAcao == '2':
                        nomeMusica = components.validarVariavel(dictOuvinte['2'], "Informe o nome da música:\t")
                        components.limparTela()
                        components.estiloTitulo(dictOuvinte['2'])
                        ouvinte.pesquisarMusica(nomeMusica)
                        components.interacao()
                    elif opcaoAcao == '3':
                        components.limparTela()
                        components.estiloTitulo(dictOuvinte['3'])
                        ouvinte.mostrarAlbum()
                        components.interacao()
                    elif opcaoAcao == '4':
                        nomeArtista = components.validarVariavel(dictOuvinte['1'], "Informe o nome do artista:\t")
                        components.limparTela()
                        components.estiloTitulo(dictOuvinte['1'])
                        if ouvinte.pesquisarArtista(nomeArtista) == True:
                            components.limparTela()
                            components.estiloTitulo(dictOuvinte['1'])
                            idAlbumPesquisar = components.validarInteiro("Insira o idAlbum:\t")
                            ouvinte.mostraMusica(idAlbumPesquisar)
                        components.interacao()
        
                    elif opcaoAcao == '5':
                        dictConta = {
                        '1':'Alterar nickname',
                        '2':'Alterar senha',
                        '3':'Vizualizar E-mail',
                        '0':'Voltar'
                        }
                        
                        while True:
                            opcaoConfiguracao = components.validarOpcao(dictOuvinte['5'], dictConta)

                            if opcaoConfiguracao == '1':
                                novoNickname = components.validarVariavel(dictConta['1'], "Informe o seu novo nickname:\t")
                                try:
                                    usuario.alterarNickname(novoNickname, conectarUsuario)
                                    components.interacao(0)
                                except:
                                    print(components.estiloTexto(0, 33, "Esse nickname já existente em nossa plataforma.\n"))
                                    components.interacao()
                            elif opcaoConfiguracao == '2':
                                novaSenha = components.validarVariavel(dictConta['2'], "Informe sua nova senha:\t")
                                usuario.alterarSenha(novaSenha, conectarUsuario)
                                components.interacao(0)
                            elif opcaoConfiguracao == '3':
                                components.limparTela()
                                components.estiloTitulo(dictConta['3'])
                                usuario.visualizarEmail(conectarUsuario)
                                components.interacao()
                            else:
                                break
                    else:
                        break


        
            
            
            



components.limparTela()
print(components.estiloTexto(0, 32, "Programa finalizado com sucesso!"))