import os
import PySimpleGUI as psg

#Declaração de variáveis globais
Arq = "biblios.txt"
Var = 'PySimpleGUI'

atua = ''


#Subs, Módulos e Classes
'''def verificaarquivo():
        
    try:
        with open(Arq, 'r') as f:
            #print (os.path.exists(Arq))
            return True
    except IOError:
        print ('Arquivo não encontrado!')
        return False
'''    
def verificabiblio():
    #Usando try conforme apreendido em sala de aula para deixar em bloco de verificação de erro
    try:
        #Variável local
        Flag = 0                                                                        #variável de controle

        os.system('pip freeze > ' + Arq)                                                # Gera um arquivo com as bibliotecas instaladas no Python

        with open(Arq, 'r',encoding='utf8') as j:                                       #Abre o arquivo para leitura
            for linha in j:                                                             #Lê todas as linhas do arquivo
                linha = linha.strip('\n')                                               #Quebra as linhas separando-as, colocando cada linha em uma unidade de lista
                linha = linha.split('==')                                               #Usa o "==" para seccionar e separar o nome da biblioteca
                #num_lines += 1
                #num_words += len(words)
                #print(linha[0])
                if linha[0] == Var:                                                     #testa se a lista de bibliotecas contém a biblioteca desejada
                    Flag = 1
                    print('Bibliotecas Ok!')
                    print('Bibliotecas encontradas, entrando no sistema.....')
                    #print(Flag)
                    return True
            if Flag == 0:                
                print('Bibliotecas não encontradas!!!!!!\n')
                atua = input('Deseja instalar bibliotecas? - S/N :')
                if atua == 'S' or atua =='s':
                    print('atualizando bibliotecas.......')
                    os.system('python -m pip install PySimpleGUI')
                    return True
                else:
                    return False
    except ValueError:
        print ("Opção inválida\n")
        #return False


def Main():
    if verificabiblio() == True:
        print('Entrou no sistema, OK!')
    else:
        print('Decidiu não instalar e saiu!')





Main()