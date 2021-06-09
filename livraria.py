#coding: utf-8
#teste
#Declaração de variáveis globais
global biblio 
biblios = ['pip','PySimpleGUI','cx_Oracle','setuptools','termcolor','pywin32']
#caminho = 'C:\\Courses\\instantclient-basic-windows.x64-19.6.0.0.0dbru\\instantclient_19_6'
global caminho
atua = ''
i=0
#Importando as bibliotecas
import win32api
from win32api import GetSystemMetrics
import os, ctypes, sys
import tkinter
import PySimpleGUI as psg
import setuptools
import string
import termcolor
import cx_Oracle
import pip
import subprocess
import time
from os import system
from termcolor import colored
# #Verifica se existe as bibliotecas, caso contrário pergunta se quer instala-las
def Main():
    biblio = False
    while not biblio:
        try:
            import win32api
            from win32api import GetSystemMetrics
            import os, ctypes, sys
            import tkinter
            import PySimpleGUI as psg
            import setuptools
            import string
            import termcolor
            import cx_Oracle
            import pip
            import subprocess
            import time
            from os import system
            from termcolor import colored
            biblio = True
            caminho = 'C:\Courses\instantclient-basic-windows.x64-19.6.0.0.0dbru\instantclient_19_6'
            os.chdir(caminho)
        except ImportError as error1:
            from os import system
            system('cls')
            print("Error: {0}".format(error1))
            print('Erro ao tentar importar bibliotecas necessárias!!')
            #for i in sys.modules.keys():
            #    print(i)
            atua = input('Deseja instalar as bibliotecas necessárias? - S/N: ')
            if atua == 's' or atua == 'S':
                try:
                    import os, ctypes, sys
                    from os import system
                    import string
                    import pip
                    import subprocess
                    import time
                    for i in biblios:
                        subprocess.check_call([sys.executable, '-m', 'pip', 'install', i])
                    print('Instalação efetuada!')
                    import win32api
                    from win32api import GetSystemMetrics
                    import PySimpleGUI as psg
                    import setuptools
                    import cx_Oracle
                    import termcolor
                    from termcolor import colored
                    os.chdir(caminho)
                    biblio = True
                except ImportError as errorimp:
                    system('cls')
                    print("Error: {0}".format(errorimp))
                except OSError as oserror:
                    system('cls')
                    print("OS error: {0}".format(oserror), sys.exc_info()[0])
                    if not os.path.exists(caminho):
                        print('Diretório não encontrado ou não existe\n\n',)
                        caminho = input('Entre com o caminho do Instant Client: ')
                        os.chdir(caminho)
                        #biblio=True
                        break
                    else:
                        os.chdir("C:\\Courses\\instantclient-basic-windows.x64-19.6.0.0.0dbru\\instantclient_19_6")
                except:
                    print("Unexpected error:", sys.exc_info()[0])
                    raise
            else:
                print('Bibliotecas não  instaladas!')
                biblio = False
                break
        except OSError as err:
            system('cls')
            print("OS error: {0}".format(err), sys.exc_info()[0])
            if not os.path.exists(caminho):
                print('Diretório não encontrado ou não existe\n\n',)
                caminho = input('Entre com o caminho do Instant Client: ')
                os.chdir(caminho)
                #biblio=True
            else:
                os.chdir("C:\\Courses\\instantclient-basic-windows.x64-19.6.0.0.0dbru\\instantclient_19_6")  
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        else:
            # Cláusula "else" do "try/except",  só é executada se
            # não ocorreu nenhum erro
            break  # Este comando encerra o "while True"
    programa()

def cadastreAutor (conexao):
    cursor = conexao.cursor()
    nome   = input("\nNome do autor? ")

    try:
        cursor.execute("INSERT INTO Autores (Id,Nome) VALUES (seqAutores.nextval,'"+nome+"')")
        conexao.commit()
    except cx_Oracle.DatabaseError:
        print("Autor repetido")
    else:
        print("Autor cadastrado com sucesso")

def removaAutor (conexao):
    cursor = conexao.cursor()
    nome   = input("\nNome do autor? ")
    try:
        cursor.execute("SELECT Id FROM Autores WHERE Nome='"+nome+"'")
        conexao.commit ()
        linha = cursor.fetchone()
        if not linha:
            print("Autor inexistente")
        else:
            cursor.execute("DELETE FROM Autores WHERE Nome='"+nome+"'")
            conexao.commit ()
            print("Autor removido com sucesso")
    except cx_Oracle.DatabaseError as err:
        print("DataBase error: {0}".format(err), sys.exc_info()[0])
        print('O autor tem livros cadastrados, favor remover os livros primeiro!')
    
def listeAutor (conexao):
    cursor=conexao.cursor()
    cursor.execute("SELECT * FROM Autores")

    linha = cursor.fetchone()
    if not linha:
        print ("Não há Autores cadastrados")
        return
    aut=0
    while linha:
        #print(linha)
        #print (len(linha[0]))
        if len(linha[1]) > aut:
            aut = len(linha[1])+4
        linha = cursor.fetchone()
    #print(aut)
    cursor.scroll(mode="first")
    linha = cursor.fetchone()
    print('|',end=''),print(' AUTOR '.center(aut,'*'),end=''), print('|')
    while linha:
        print('|', end=''), print (linha[1].center(aut,' '),end=''), print('|')
        linha = cursor.fetchone()

def cadastreLivro (conexao):
    cursor    = conexao.cursor()
    nomeLivro = input("\nNome do livro? ")
    
    try:
        precoLivro = float(input("Preço do livro? "))
    except ValueError:
        print("Preço inválido")
    else:   
        nomeAutor = input("Nome do autor? ")

        cursor.execute("SELECT Id FROM Autores WHERE Nome='"+nomeAutor+"'")
        linha = cursor.fetchone()
        if not linha:
            print("Autor inexistente")
        else:
            idAutor = linha[0]

            try:
                cursor.execute("INSERT INTO Livros (Codigo,Nome,Preco) VALUES (seqLivros.nextval,'"+nomeLivro+"',"+str(precoLivro)+")")
                conexao.commit ()
            except cx_Oracle.DatabaseError:
                print("Livro repetido")
            else:
                cursor.execute("SELECT Codigo FROM Livros WHERE Nome='"+nomeLivro+"'")
                linha  = cursor.fetchone()
                CodigoLivro = linha[0]
                
                cursor.execute("INSERT INTO Autorias (Id,Codigo) VALUES ("+str(idAutor)+","+str(CodigoLivro)+")")
                conexao.commit ()
                print("Livro cadastrado com sucesso")
               
def removaLivro (conexao):
    cursor = conexao.cursor()
    nome = input("\nNome do livro? ")

    cursor.execute("SELECT Codigo FROM Livros WHERE Nome='"+nome+"'")
    linha = cursor.fetchone()
        
    if not linha:
        print("Livro inexistente")
    else:
        CodigoLivro = linha[0]
        
        cursor.execute("SELECT Id FROM Autorias WHERE Codigo="+str(CodigoLivro))
        linha   = cursor.fetchone()
        idAutor = linha[0]
        
        cursor.execute("DELETE FROM Autorias WHERE Id="     + str(idAutor))
        cursor.execute("DELETE FROM Livros   WHERE Codigo=" + str(CodigoLivro))
        conexao.commit ()
        
        print("Autor removido com sucesso")
      
def listeLivros (conexao):
    cursor=conexao.cursor()
    cursor.execute("SELECT Livros.Nome, Autores.Nome, Livros.Preco FROM Livros, Autorias, Autores WHERE Livros.Codigo=Autorias.Codigo AND Autorias.Id=Autores.Id")

    linha = cursor.fetchone()
    if not linha:
        print ("Não há livros cadastrados")
        return
   
    liv=0
    aut=0
    val=13
    while linha:
        #print(linha)
        #print (len(linha[0]))
        if len(linha[0]) > liv:
            liv = len(linha[0])+4
        if len(linha[1]) > aut:
            aut = len(linha[1])+4   
        linha = cursor.fetchone()
    #print(aut)
    cursor.scroll(mode="first")
    linha = cursor.fetchone()
    print('|',end=''),print(' NOME DO LIVRO '.center(liv,'*') + '|' + ' AUTOR '.center(aut,'*') + '|' +' VALOR '.center(val,'*'),end=''), print('|')
    while linha:
        print('|', end=''), print (linha[0].center(liv,' ')+'|'+linha[1].center(aut,' ')+'|'+str(linha[2]).center(val,' '),end=''), print('|')
        linha = cursor.fetchone()    

def cabecalho():
    print ('*'.center(150,'*'))
    print (colored('   PROGRAMA PARA CADASTRAR LIVROS E SEUS AUTORES   '.center(150,'▓'),'red'))
    print ('*'.center(150,'*'))

def tela_prin():
    system('cls')
    cabecalho()
    print ('\n\nMENU---------> Opção:')
    print (''.center(23,'-'))
    print ("CADASTROS---->       1")
    print ("REMOÇÃO------>       2")
    print ("LISTAGEM----->       3") # fazer
    print ("TERMINAR----->       0\n")
    #print (f'Teste'.format('\033[1;34m'))

def tela_cadastro():
    system('cls')
    cabecalho()
    print ('*'.center(150,'*'))
    print (colored('   CADASTRAR   '.center(150,'▓',),'blue'))
    print ('*'.center(150,'*'))
    print ("\n\n1) CADASTRAR Autor")
    print ("2) CADASTRAR Livro")
    print ("0) RETORNAR\n")

def tela_remocao():
    system('cls')
    cabecalho()
    print ('*'.center(150,'*'))
    print (colored('   REMOÇÃO   '.center(150,'▓',),'blue'))
    print ('*'.center(150,'*'))
    print ("\n\n1) REMOVER Autor")
    print ("2) REMOVER Livro")
    print ("0) RETORNAR\n")

def tela_listagem():
    system('cls')
    cabecalho()
    print ('*'.center(150,'*'))
    print (colored('   LISTAR   '.center(150,'▓',),'blue'))
    print ('*'.center(150,'*'))
    print ("\n\n1) LISTAR    Autor")
    #print ("2) LISTAR Livro")
    print ("2) LISTAR    todos os Livros")
    print ("3) LISTAR    os Livros até certo preço") # fazer
    print ("4) LISTAR    os Livros numa faixa de preço") # fazer
    print ("5) LISTAR    os Livros acima de um certo preço") # fazer
    print ("0) RETORNAR\n")

def saida():
    system('cls')
    print ('\n\n\n')
    print ('*'.center(150,'*'))
    print (colored(' OBRIGADO POR USAR ESTE PROGRAMA '.center(150,'▓'),'red'))
    print ('*'.center(150,'*'))

def connection():
    global conexao
    servidor = 'localhost/xe'
    usuario  = 'system'
    senha    = 'oracle'
    try:
        conexao = cx_Oracle.connect(dsn=servidor,user=usuario,password=senha)
        cursor  = conexao.cursor()
    except cx_Oracle.DatabaseError:
        print ("Erro de conexão com o BD\n")
        return
    '''
    try:
        cursor.execute("DROP TABLE Autorias")
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a tabela nao existe

    try:
        cursor.execute("DROP SEQUENCE seqAutores")
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a sequencia nao existe

    try:
        cursor.execute("DROP TABLE Autores")
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a tabela nao existe

    try:
        cursor.execute("DROP SEQUENCE seqLivros")
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a sequencia nao existe

    try:
        cursor.execute("DROP TABLE Livros")
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a tabela nao existe
    '''
    try:
        cursor.execute("CREATE SEQUENCE seqAutores START WITH 1 INCREMENT BY 1 MINVALUE 1 MAXVALUE 999 NOCACHE CYCLE")
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a sequência já existe

    try:
        cursor.execute("CREATE TABLE Autores (Id NUMBER(3) PRIMARY KEY, Nome NVARCHAR2(50) UNIQUE NOT NULL)")
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a tabela já existe

    try:
        cursor.execute("CREATE SEQUENCE seqLivros START WITH 1 INCREMENT BY 1 MAXVALUE 999 NOCACHE CYCLE")
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a tabela já existe

    try:
        cursor.execute("CREATE TABLE Livros (Codigo NUMBER(5) PRIMARY KEY, Nome NVARCHAR2(50) UNIQUE NOT NULL, Preco NUMBER(5,2) NOT NULL)")
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a tabela já existe

    try:
        cursor.execute("CREATE TABLE Autorias (Id NUMBER(3), Codigo NUMBER(5), FOREIGN KEY (Id) REFERENCES Autores(Id), FOREIGN KEY (Codigo) REFERENCES Livros(Codigo))")
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a tabela já existe

def programa():
    #print ("PROGRAMA PARA PARA CADASTRAR LIVROS E SEUS AUTORES")
    connection()
    fimDoPrograma=False
    fimdocadastro=False
    fimdaremocao=False
    fimdalistagem=False

    while not fimDoPrograma:
        tela_prin()    
        try:
            opcao = int(input("Digite sua opção:    "));
        except ValueError:
            print ("Opção inválida\n")
        else:
            # renumerar opções abaixo e usar até 4 novos subprogramas
            # procurar economizar nessa quantidade acima de subprogramas
            if opcao==1:
                fimdocadastro=False
                while not fimdocadastro:
                    tela_cadastro()                   
                    try:
                        opcad = int(input("Digite sua opção: "))
                    except ValueError:
                        print ("Opção inválida\n")
                    else:
                        if opcad==1:
                            cadastreAutor (conexao)
                            time.sleep(3)
                        elif opcad==2:
                            cadastreLivro (conexao)
                            time.sleep(3)
                        elif opcad==0:
                            fimdocadastro=True
                        else:
                            print ("Opção inválida\n")
                        
                    #cadastreAutor (conexao)
            elif opcao==2:
                fimdaremocao=False
                while not fimdaremocao:
                    tela_remocao()                   
                    try:
                        opcad = int(input("Digite sua opção: "))
                    except ValueError:
                        print ("Opção inválida\n")
                    else:
                        if opcad==1:
                            removaAutor (conexao)
                            win32api.Beep(500, 3000)
                            time.sleep(3)
                        elif opcad==2:
                            removaLivro (conexao)
                            time.sleep(3)
                        elif opcad==0:
                            fimdaremocao=True
                        else:
                            print ("Opção inválida\n")
                
            elif opcao==3:
                fimdalistagem=False
                while not fimdalistagem:
                    tela_listagem()                   
                    try:
                        opcad = int(input("Digite sua opção: "))
                    except ValueError:
                        print ("Opção inválida\n")
                    else:
                        if opcad==1:
                            listeAutor (conexao)
                            time.sleep(3)
                            input("Press Enter to continue...")
                        elif opcad==2:
                            listeLivros (conexao)
                            time.sleep(3)
                            input("Press Enter to continue...")
                        elif opcad==0:
                            fimdalistagem=True
                        else:
                            print ("Opção inválida\n")
            elif opcao==4:
                removaLivro (conexao)
            elif opcao==5:
                listeLivros (conexao)
            elif opcao==0:
                fimDoPrograma=True
            else:
                print ("Opção inválida\n")

    saida()            
    #print ("\nOBRIGADO POR USAR ESTE PROGRAMA")


# daqui para cima  temos definições de subprogramas
# daqui para baixo temos o programa

''' 
    print ("6) LISTAR    todos os Livros")
    print ("7) LISTAR    os Livros até certo preço") # fazer
    print ("8) LISTAR    os Livros numa faixa de preço") # fazer
    print ("9) LISTAR    os Livros acima de um certo preço") # fazer
'''


Main()

