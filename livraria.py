#coding: utf-8
#Declaração de variáveis globais
Arq = "biblios.txt"
Py = 'PySimpleGUI'
Oracx = 'cx_Oracle'
biblio = False
biblios = ['PySimpleGUI','cx_Oracle','pip','termcolor']
caminho = 'C:\\Courses1\\instantclient-basic-windows.x64-19.6.0.0.0dbru\\instantclient_19_6'
atua = ''
i=0
#Importando as bibliotecas
# #Verifica se existe as bibliotecas, caso contrário pergunta se quer instala-las 
try:
    import os, ctypes, sys
    import PySimpleGUI as psg   
    import string
    import termcolor
    import cx_Oracle
    import pip
    import time
    import subprocess
    from os import system
    from termcolor import colored
    biblio = True
    os.chdir("C:\\Courses\\instantclient-basic-windows.x64-19.6.0.0.0dbru\\instantclient_19_6")
except ImportError as error1:
    print(f"Error: {0}".format(error1))
    print('Erro ao tentar importar bibliotecas necessárias!!')
    for i in sys.modules.keys():
        print(i)
    atua = input('Deseja instalar as bibliotecas necessárias? - S/N: ')
    if atua == 's' or atua == 'S':
        import os, ctypes, sys
        import PySimpleGUI as psg   
        import string
        import termcolor
        import cx_Oracle
        import pip
        import subprocess
        from os import system
        import subprocess
        from termcolor import colored
        for i in biblios:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', i])
        print('Instalação efetuada!')
        biblio = True
    else:
        print('Bibliotecas não  instaladas!')
        biblio = False
except OSError as err:
    system('cls')
    print("OS error: {0}".format(err), sys.exc_info()[0])
    if not os.path.exists(caminho):
        print('Diretório não encontrado ou não existe\n\n',)
        caminho = input('Entre com o caminho do Instant Client: ')
        os.chdir(caminho)
    else:
        os.chdir("C:\\Courses1\\instantclient-basic-windows.x64-19.6.0.0.0dbru\\instantclient_19_6")  
except:
    raise


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

    cursor.execute("SELECT Id FROM Autores WHERE Nome='"+nome+"'")
    conexao.commit ()

    linha = cursor.fetchone()
    if not linha:
        print("Autor inexistente")
    else:
        cursor.execute("DELETE FROM Autores WHERE Nome='"+nome+"'")
        conexao.commit ()
        print("Autor removido com sucesso")
    

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
        
    while linha:
        print (linha[0]+" "+linha[1]+" "+str(linha[2]))
        linha = cursor.fetchone()    

def cabecalho():
    print ('*'.center(180,'*'))
    print (colored('   PROGRAMA PARA PARA CADASTRAR LIVROS E SEUS AUTORES   '.center(180,'▓'),'red'))
    print ('*'.center(180,'*'))

def tela_prin():
    system('cls')
    cabecalho()
    print ('\n\nMENU---------> Opção:')
    print (''.center(23,'-'))
    print ("CADASTROS---->      1")
    print ("REMOÇÃO------>      2")
    print ("LISTAGEM----->      3") # fazer
    print ("TERMINAR----->      0\n")
    #print (f'Teste'.format('\033[1;34m'))

def tela_cadastro():
    system('cls')
    cabecalho()
    print ('*'.center(180,'*'))
    print (colored('   CADASTROS   '.center(180,'▓',),'blue'))
    print ('*'.center(180,'*'))

def programa():
    print ("PROGRAMA PARA PARA CADASTRAR LIVROS E SEUS AUTORES")
	
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

    fimDoPrograma=False
    fimdocadastro=False
    fimdaremocao=False
    fimdalistagem=False

    while not fimDoPrograma:
        tela_prin()    
        try:
            opcao = int(input("Digite sua opção: "));
        except ValueError:
            print ("Opção inválida\n")
        else:
            # renumerar opções abaixo e usar até 4 novos subprogramas
            # procurar economizar nessa quantidade acima de subprogramas
            if opcao==1:
                while not fimdocadastro:
                    tela_cadastro()
                    print ("\n\n1) CADASTRAR Autor")
                    print ("2) CADASTRAR Livro")
                    print ("0) RETORNAR\n")
                   
                    try:
                        opcad = int(input("Digite sua opção: "))
                    except ValueError:
                        print ("Opção inválida\n")
                    else:
                        if opcad==1:
                            cadastreAutor (conexao)
                            time.sleep(3)
                        elif opcad==2:
                            removaAutor (conexao)
                        elif opcad==0:
                            fimdocadastro=True
                        else:
                            print ("Opção inválida\n")
                        
                    #cadastreAutor (conexao)
            elif opcao==2:
                removaAutor (conexao)
            elif opcao==3:
                cadastreLivro (conexao)
            elif opcao==4:
                removaLivro (conexao)
            elif opcao==5:
                listeLivros (conexao)
            elif opcao==0:
                fimDoPrograma=True
            else:
                print ("Opção inválida\n")
                
    print ("\nOBRIGADO POR USAR ESTE PROGRAMA")

# daqui para cima  temos definições de subprogramas
# daqui para baixo temos o programa

''' 
    print ("6) LISTAR    todos os Livros")
    print ("7) LISTAR    os Livros até certo preço") # fazer
    print ("8) LISTAR    os Livros numa faixa de preço") # fazer
    print ("9) LISTAR    os Livros acima de um certo preço") # fazer
'''
def Main():
    if biblio == True:
        print('Entrou no sistema, OK!')
        programa()
    else:
        print('Decidiu não instalar e saiu!')





Main()

