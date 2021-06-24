#coding: utf-8
#############################################################################
'''PROJETO DE SALA DE AULA - SISTEMA DE LIVRARIA
Software/Programa desenvolvido aplicando os conhecimentos obtidos em sala de 
aula para obtenção de nota na matéria de APPC
no curso de SISTEMAS DE INFORMAÇÃO, sob a supervisão do Ilmo. 
Prof. André de Carvalho

JEFFERSON EDUARDO LUIZ
RA 19568823

Foi empregado todo o conhecimento obtido em sala de aula e acrescentado algumas 
funcionalidades aprendidas de forma autônoma ao curso.
Também foi utilizado o GUI(Graphical User Interface) Tkinter para 
desenvolvimento do programa.

'''
#############################################################################
# Importando as bibliotecas
import os
import sys
import tkinter as tk
import subprocess
from os import system
from os import *
from tkinter import *
from tkinter import *
import time
from time import *
from tkinter.simpledialog import askstring
from tkinter import font
from tkinter import messagebox
from tkinter import Entry
from tkinter import ttk
from tkinter.font import BOLD
import inspect
from functools import partial
import string
import subprocess

#============================================================================
# Declaração de variáveis globais
biblio = False
caminho = 'InstantClient'
biblios = ['pip','cx_Oracle','setuptools','pywin32']
atua = ''
i=0
#biblio = False #variável de controle para saber se está tudo ok e seguir com a execução

#============================================================================
# Verifica se existe as bibliotecas, caso contrário pergunta se quer instala-las. Faço
#várias verificações de erros.
#============================================================================
while not biblio: #Aqui decidi deixar tudo em um laço(While) pois na 
                  #verificação tem a opção da instalação das Bibliotecas
    try:
        #Resolvi o problema da janela fantasma aparecendo quando entrava no
        # loop e perguntava se queria instalar as biblios, era uma instancia
        # do Tkinter que ficava aberta, eu nome-ei e instanciei ela para 
        # poder usar um destroy depois.        
        Phantom = Tk()
        Phantom.withdraw()

        #====================================================================
        # Importando as bibliotecas
        # Verifica se existe as bibliotecas, caso contrário pergunta se quer 
        # instala-las
        import cx_Oracle
        import win32
        from win32 import *
        import setuptools
        import pip

        #====================================================================
        #Aqui estou usando a funcionalidade da biblioteca
        #'os' para setar o caminho do instantclient
        os.chdir(caminho)
        #Tudo saindo OK ele atualiza a instancia fantasma e destroy
        Phantom.update()
        Phantom.destroy()
        biblio = True #Aqui sai do laço
    except ImportError as error1:
        from os import system
        messagebox.showerror('Erro Bibliotecas','Error: ' + str(error1))
        messagebox.showerror('Erro Bibliotecas','Erro ao tentar importar bibliotecas necessárias!!')
        atua = messagebox.askyesno('Instalar Bibliotecas','Deseja instalar as bibliotecas necessárias? - S/N: ')
        if atua == YES:
            try:
                import pip
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
                for i in biblios:
                    subprocess.check_call([sys.executable, '-m', 'pip', 'install', i])
                messagebox.showinfo('Bibliotecas','Instalação concluída!')
            except ImportError as errorimp:
                messagebox.showerror('Erro Bibliotecas','Error: '+ str(errorimp))
                exit()
            except:
                messagebox.showerror('Erro','Unexpected error:')
                raise
        else:
            messagebox.showerror('Erro', 'Bibliotecas não instaladas, Saindo...!')
            biblio = False
            quit()
    except OSError as err:
        messagebox.showerror('Erro OS', 'OS error: ' + str(err))
        if not os.path.exists(caminho):
            messagebox.showerror('OS Erro','Diretório não encontrado ou não existe',)
            caminho = askstring('OS Error:', 'Entre com o caminho do Instant Client: ')
            os.chdir(caminho)
            #programa()
            Phantom.update()
            Phantom.destroy()
            biblio=True 
    except:
        messagebox.showerror('Error', 'Unexpected error:')
        raise
    else:
        # Cláusula 'else' do 'try/except',  só é executada se
        # não ocorreu nenhum erro
        import setuptools
        import cx_Oracle
        import inspect
        biblio=True     # Este comando encerra o 'while True'

#============================================================================
def cadastreAutor (conexao):
    stack = inspect.stack()
    try:
        cursor = conexao.cursor()
        nome   = input('\nNome do autor? ')
        cursor.execute("INSERT INTO Autores (Id,Nome) VALUES (seqAutores.nextval,'"+nome+"')")
        conexao.commit()
    except cx_Oracle.DataError as err:
        print('DataBase error: {0}'.format(err), sys.exc_info()[0])
    except cx_Oracle.DatabaseError as err:
        error, = err.args
        print('Oracle-Error-Code:', error.code)
        print('Oracle-Error-Message:', error.message)
        if error.code == 1400:
            print('Você deve inserir um nome para o Autor, não pode ser em branco', stack[1].function)
            return
        elif error.code == 1:
            print('Autor repetido')
            return
        elif error.code == 936:
            print('Erro de Sintax, favor verificar código', stack[1].function)
        elif error.code == 933:
            print('Favor usar "." ao invés de "," nos valores numéricos decimais')
        elif error.code == 904:
            print('Campo não encontrado na tabela')
    except KeyError:
        print('Erro de Sintax, favor verificar código', stack[1].function)
    except:
        print('DataBase error: {0}', sys.exc_info()[0])
    else:
        print('Autor cadastrado com sucesso')

def removaAutor (conexao):
    try:
        cursor = conexao.cursor()
        nome   = input('\nNome do autor? ')
        if not nome:
            print('Você deve inserir um nome para o Autor, não pode ser em branco')
            return
        cursor.execute("SELECT Id FROM Autores WHERE Nome='"+nome+"'")
        conexao.commit ()
        linha = cursor.fetchone()
        if not linha:
            print('Autor inexistente')
        else:
            cursor.execute("DELETE FROM Autores WHERE Nome='"+nome+"'")
            conexao.commit ()
            print('Autor removido com sucesso')
    except cx_Oracle.DataError as err:
        print('DataBase error: {0}'.format(err), sys.exc_info()[0])
    except cx_Oracle.DatabaseError as err:
        error, = err.args
        print('Oracle-Error-Code:', error.code)
        print('Oracle-Error-Message:', error.message)
        if error.code == 1400:
            print('Você deve inserir um nome para o Autor, não pode ser em branco')
            return
        elif error.code == 1:
            print('Autor repetido')
            return
        elif error.code == 936:
            stack = inspect.stack()
            print('Erro de Sintax, favor verificar código', stack[1].function)
        elif error.code == 933:
            print('Favor usar "." ao invés de "," nos valores numéricos decimais')
        elif error.code == 2292:
            print('O autor tem livros cadastrados, favor remover os livros primeiro!')
        elif error.code == 904:
            print('Campo não encontrado na tabela')
    except:
        print('DataBase error: {0}', sys.exc_info()[0])
        
def listeAutor (conexao):
    try:
        cursor=conexao.cursor()
        cursor.execute("SELECT * FROM Autores ORDER BY Autores.Nome")

        linha = cursor.fetchone() # linha(1,'Arthur')
        if not linha:
            print ('Não há Autores cadastrados')
            return
        aut=0
        while linha:
            #print(linha)
            #print (len(linha[0]))
            if len(linha[1]) > aut:
                aut = len(linha[1])
            linha = cursor.fetchone()
        #print(aut)
        aut = aut + 2
        cursor.scroll(mode='first')
        linha = cursor.fetchone()
        print('|',end=''),print(' AUTOR '.center(aut,'*'),end=''), print('|')
        while linha:
            print('|', end=''), print (linha[1].center(aut,' '),end=''), print('|')
            linha = cursor.fetchone()
    except cx_Oracle.DataError as err:
        print('DataBase error: {0}'.format(err), sys.exc_info()[0])
    except cx_Oracle.DatabaseError as err:
        error, = err.args
        print('Oracle-Error-Code:', error.code)
        print('Oracle-Error-Message:', error.message)
        if error.code == 1400:
            print('Você deve inserir um nome para o Autor, não pode ser em branco')
            return
        elif error.code == 1:
            print('Autor repetido')
            return
        elif error.code == 936:
            stack = inspect.stack()
            print('Erro de Sintax, favor verificar código', stack[1].function)
        elif error.code == 933:
            print('Favor usar "." ao invés de "," nos valores numéricos decimais')
        elif error.code == 904:
            print('Campo não encontrado na tabela')
    except:
        print('DataBase error: {0}', sys.exc_info()[0])

def verificaLivro(livro):
    cursor    = conexao.cursor()
    cursor.execute("SELECT Codigo FROM Livros WHERE Nome='"+livro+"'")
    cursor.commit()
    return livro

def cadastreLivro (conexao):
    try:
        cursor    = conexao.cursor()
        nomeLivro = input('\nNome do livro? ')
        #verificaLivro(nomeLivro)
        if nomeLivro == '':
            print('Precisa entrar com um nome de Livro!')
            return
        precoLivro = float(input('Preço do livro? '))
    except ValueError:
        print('Preço inválido, Favor usar "." ao invés de "," nos valores numéricos decimais')
    else: 
        nomeAutor = input('Nome do autor? ')
        cursor.execute("SELECT Id FROM Autores WHERE Nome='"+nomeAutor+"'")
        linha = cursor.fetchone()
        if not linha:
            print('Autor inexistente')
        else:
            idAutor = linha[0]
            try:
                cursor.execute("INSERT INTO Livros (Codigo,Nome,Preco) VALUES (seqLivros.nextval,'"+nomeLivro+"',"+str(precoLivro)+")")
                conexao.commit ()
            except cx_Oracle.DataError as err:
                print('DataBase error: {0}'.format(err), sys.exc_info()[0])
            except cx_Oracle.DatabaseError as err:
                error, = err.args
                print('Oracle-Error-Code:', error.code)
                print('Oracle-Error-Message:', error.message)
                if error.code == 1400:
                    print('Você deve inserir um nome para o Livro, não pode ser em branco')
                    return
                elif error.code == 1:
                    print('Livro já cadastrado')
                    return
                elif error.code == 936:
                    stack = inspect.stack()
                    print('Erro de Sintax, favor verificar código', stack[1].function)
                elif error.code == 933:
                    print('Favor usar "." ao invés de "," nos valores numéricos decimais')
                elif error.code == 904:
                    print('Campo não encontrado na tabela')
            else:
                cursor.execute("SELECT Codigo FROM Livros WHERE Nome='"+nomeLivro+"'")
                linha  = cursor.fetchone()
                CodigoLivro = linha[0]
                
                cursor.execute("INSERT INTO Autorias (Id,Codigo) VALUES ("+str(idAutor)+","+str(CodigoLivro)+")")
                conexao.commit ()
                print('Livro cadastrado com sucesso')
               
def removaLivro (conexao):
    rem = 'N'
    
    try:
        cursor = conexao.cursor()
        nome = input('\nNome do livro? ')
        if not nome:
            print('Favor entrar com o nome do Livro, não pode ser em branco!')
            return
        cursor.execute("SELECT Codigo FROM Livros WHERE Nome='"+nome+"'")
        linha = cursor.fetchone()    
        if not linha:
            print('Livro não encontrado')
        else:
            #cursor=conexao.cursor()
            cursor.execute("SELECT Livros.Nome, Autores.Nome, Livros.Preco FROM Livros, Autorias, Autores WHERE Livros.Codigo=Autorias.Codigo AND Autorias.Id=Autores.Id AND Livros.Nome='"+nome+"' ORDER BY Livros.Nome")
            linha = cursor.fetchone()
            if not linha:
                print ('Não há livros cadastrados')
                return
            liv=0
            aut=0
            val=8
            while linha:
                #print(linha)
                #print (len(linha[0]))
                if len(linha[0]) > liv:
                    liv = len(linha[0])
                if len(linha[1]) > aut:
                    aut = len(linha[1])   
                linha = cursor.fetchone()
            #print(aut)
            liv = liv + 2
            aut = aut + 2
            cursor.scroll(mode='first')
            linha = cursor.fetchone()
            print('|',end=''),print(' LIVRO '.center(liv,'*') + '|' + ' AUTOR '.center(aut,'*') + '|' +' VALOR '.center(val,'*'),end=''), print('|')
            while linha:
                print('|', end=''), print (linha[0].center(liv,' ')+'|'+linha[1].center(aut,' ')+'|'+str(linha[2]).center(val,' '),end=''), print('|')
                linha = cursor.fetchone()
            cursor.scroll(mode='first')
            linha = cursor.fetchone()
            rem = input('\n\nGostaria mesmo de remover o Livro?: ')
            if rem=='s' or rem=='S':
                #cursor = conexao.cursor()
                cursor.execute("SELECT Codigo FROM Livros WHERE Nome='"+nome+"'")
                linha = cursor.fetchone()
                CodigoLivro = linha[0]
                cursor.execute("SELECT Id FROM Autorias WHERE Codigo="+str(CodigoLivro))
                linha   = cursor.fetchone()
                idAutor = linha[0]
                cursor.execute("DELETE FROM Autorias WHERE Id="     + str(idAutor))
                cursor.execute("DELETE FROM Livros   WHERE Codigo=" + str(CodigoLivro))
                conexao.commit ()
                print('Livro removido com sucesso')
            else:
                linha = ''
                return
    except cx_Oracle.DataError as err:
                print('DataBase error: {0}'.format(err), sys.exc_info()[0])
    except cx_Oracle.DatabaseError as err:
        error, = err.args
        print('Oracle-Error-Code:', error.code)
        print('Oracle-Error-Message:', error.message)
        if error.code == 1400:
            print('Você deve inserir um nome para o Livro, não pode ser em branco')
            return
        #print('DataBase error: {0}'.format(err), sys.exc_info()[0])
        elif error.code == 1:
            print('Livro repetido')
            return
        elif error.code == 936:
            stack = inspect.stack()
            print('Erro de Sintax, favor verificar código', stack[1].function)
        elif error.code == 933:
            print('Favor usar "." ao invés de "," nos valores numéricos decimais')
        elif error.code == 904:
            print('Campo não encontrado na tabela')
      
def listeLivros (conexao):
    cursor=conexao.cursor()
    cursor.execute("SELECT Livros.Nome, Autores.Nome, Livros.Preco FROM Livros, Autorias, Autores WHERE Livros.Codigo=Autorias.Codigo AND Autorias.Id=Autores.Id ORDER BY Livros.Nome")
    linha = cursor.fetchone()
    if not linha:
        print ('Não há livros cadastrados')
    liv=0
    aut=0
    val=8
    while linha:
        #print(linha)
        #print (len(linha[0]))
        if len(linha[0]) > liv:
            liv = len(linha[0])
        if len(linha[1]) > aut:
            aut = len(linha[1])   
        linha = cursor.fetchone()
    #print(aut)
    liv = liv + 2
    aut = aut + 2
    cursor.scroll(mode='first')
    linha = cursor.fetchone()
    print('|',end=''),print(' LIVRO '.center(liv,'*') + '|' + ' AUTOR '.center(aut,'*') + '|' +' VALOR '.center(val,'*'),end=''), print('|')
    while linha:
        print('|', end=''), print (linha[0].center(liv,' ')+'|'+linha[1].center(aut,' ')+'|'+str(linha[2]).center(val,' '),end=''), print('|')
        linha = cursor.fetchone()    

def listeLivroAte(conexao):
    try:
        livro = input('Você gostaria de listar livros até que valor?: ')
        cursor=conexao.cursor()
        cursor.execute('SELECT Livros.Nome, Autores.Nome, Livros.Preco FROM Livros, Autores, Autorias WHERE Livros.Preco <= ' + livro + ' AND Livros.Codigo=Autorias.Codigo AND Autorias.Id=Autores.Id ORDER BY Livros.Preco ASC')
        linha = cursor.fetchone()
        if not linha:
            print ('Não há Livros cadastrados')
            return
    except cx_Oracle.DataError as err:
        print('DataBase error: {0}'.format(err), sys.exc_info()[0])
    except cx_Oracle.DatabaseError as err:
        error, = err.args
        print('Oracle-Error-Code:', error.code)
        #print('Oracle-Error-Message:', error.message)
        if error.code == 1400:
            print('Você deve inserir um nome para o Livro, não pode ser em branco')
        #print('DataBase error: {0}'.format(err), sys.exc_info()[0])
        elif error.code == 1:
            print('Livro repetido')
        print('DataBase error: {0}'.format(err), sys.exc_info()[0])
    else:
        liv=0
        aut=0
        val=8
        while linha:
            #print(linha)
            #print (len(linha[0]))
            if len(linha[0]) > liv:
                liv = len(linha[0])
            if len(linha[1]) > aut:
                aut = len(linha[1])   
            linha = cursor.fetchone()
        #print(aut)
        liv = liv + 2
        aut = aut + 2
        cursor.scroll(mode='first')
        linha = cursor.fetchone()
        print('|',end=''),print(' LIVRO '.center(liv,'*') + '|' + ' AUTOR '.center(aut,'*') + '|' +' VALOR '.center(val,'*'),end=''), print('|')
        while linha:
            print('|', end=''), print (linha[0].center(liv,' ')+'|'+linha[1].center(aut,' ')+'|'+str(linha[2]).center(val,' '),end=''), print('|')
            linha = cursor.fetchone()    

def listeLivroEntre(conexao):
    while True:
        try:
            livro = input('Você gostaria de listar livros de que valor?: ')
            livro1 = input('Até qual valor?: ')
            if not(livro or livro1):
                print('Digite um valor')
                return
            cursor=conexao.cursor()
            cursor.execute('SELECT Livros.Nome, Autores.Nome, Livros.Preco FROM Livros, Autores, Autorias WHERE Livros.Preco >= ' + livro + ' AND Livros.Preco <=' + livro1 + ' AND Livros.Codigo=Autorias.Codigo AND Autorias.Id=Autores.Id ORDER BY Livros.Preco ASC')
            linha = cursor.fetchone()
            if not linha:
                print ('Não há Livros cadastrados')
                return
            liv=0
            aut=0
            val=8
            while linha:
                #print(linha)
                #print (len(linha[0]))
                if len(linha[0]) > liv:
                    liv = len(linha[0])
                if len(linha[1]) > aut:
                    aut = len(linha[1])   
                linha = cursor.fetchone()
            #print(aut)
            liv = liv + 2
            aut = aut + 2
            cursor.scroll(mode='first')
            linha = cursor.fetchone()
            print('|',end=''),print(' LIVRO '.center(liv,'*') + '|' + ' AUTOR '.center(aut,'*') + '|' +' VALOR '.center(val,'*'),end=''), print('|')
            while linha:
                print('|', end=''), print (linha[0].center(liv,' ')+'|'+linha[1].center(aut,' ')+'|'+str(linha[2]).center(val,' '),end=''), print('|')
                linha = cursor.fetchone()
            return
        except ValueError:
            print('Você deve digitar um valor')
            return
           
def listeLivroApartir(conexao):
    livro = input('Você gostaria de listar livros a partir de qual valor?: ')
    cursor=conexao.cursor()
    cursor.execute('SELECT Livros.Nome, Autores.Nome, Livros.Preco FROM Livros, Autores, Autorias WHERE Livros.Preco >= ' + livro + ' AND Livros.Codigo=Autorias.Codigo AND Autorias.Id=Autores.Id ORDER BY Livros.Preco')
    linha = cursor.fetchone()
    if not linha:
        print ('Não há Livros cadastrados')
        return
    liv=0
    aut=0
    val=8
    while linha:
        #print(linha)
        #print (len(linha[0]))
        if len(linha[0]) > liv:
            liv = len(linha[0])
        if len(linha[1]) > aut:
            aut = len(linha[1])   
        linha = cursor.fetchone()
    #print(aut)
    liv = liv + 2
    aut = aut + 2
    cursor.scroll(mode='first')
    linha = cursor.fetchone()
    print('|',end=''),print(' LIVRO '.center(liv,'*') + '|' + ' AUTOR '.center(aut,'*') + '|' +' VALOR '.center(val,'*'),end=''), print('|')
    while linha:
        print('|', end=''), print (linha[0].center(liv,' ')+'|'+linha[1].center(aut,' ')+'|'+str(linha[2]).center(val,' '),end=''), print('|')
        linha = cursor.fetchone()

'''def cabecalho():
    print (colored('*'.center(150,'*'),'green', attrs=['bold']))
    print (colored('   PROGRAMA PARA CADASTRAR LIVROS E SEUS AUTORES   '.center(150,'▓'),'red', attrs=['bold']))
    print (colored('*'.center(150,'*'),'green', attrs=['bold']))

def tela_prin():
    system('cls')
    cabecalho()
    print (colored('\n\n\n\n\nMENU------------------------->  Opção:','yellow'))
    print (colored(''.center(38,'-'),'grey', attrs=['bold']))
    print (colored('CADASTROS-------------------->   ','green'),end=''), print('| 1 |')
    print (colored('REMOÇÃO---------------------->   ','green'),end=''), print('| 2 |')
    print (colored('LISTAGEM--------------------->   ','green'),end=''), print('| 3 |') # fazer
    print (colored('TERMINAR--------------------->   ','green'),end=''), print('| 0 |')
    #print (f'Teste'.format('\033[1;34m'))
    print (colored(''.center(38,'-'),'grey'))

def tela_cadastro():
    system('cls')
    cabecalho()
    print (colored('*'.center(150,'*'),'blue',attrs=['bold']))
    print (colored('   CADASTRO   '.center(150,'▓',),'blue',attrs=['bold']))
    print (colored('*'.center(150,'*'),'blue',attrs=['bold']))
    print (colored('\n\nMENU CADASTRO---------------->  Opção:','yellow'))
    print (colored(''.center(38,'-'),'grey', attrs=['bold']))
    print (colored('CADASTRAR Autor-------------->   ','green'),end=''), print('| 1 |')
    print (colored('CADASTRAR Livro-------------->   ','green'),end=''), print('| 2 |')
    print (colored('RETORNAR--------------------->   ','green'),end=''), print('| 0 |') # fazer
    print (colored(''.center(38,'-'),'grey'))

def tela_cad_ator():
    system('cls')
    cabecalho()
    print (colored('*'.center(150,'*'),'blue',attrs=['bold']))
    print (colored('   CADASTRAR Autor   '.center(150,'▓',),'blue',attrs=['bold']))
    print (colored('*'.center(150,'*'),'blue',attrs=['bold']))

def tela_cad_livro():
    system('cls')
    cabecalho()
    print (colored('*'.center(150,'*'),'blue',attrs=['bold']))
    print (colored('   CADASTRAR Livro   '.center(150,'▓',),'blue',attrs=['bold']))
    print (colored('*'.center(150,'*'),'blue',attrs=['bold']))

def tela_remocao():
    system('cls')
    cabecalho()
    print (colored('*'.center(150,'*'),'red',attrs=['bold']))
    print (colored('   REMOÇÃO   '.center(150,'▓',),'red',attrs=['bold']))
    print (colored('*'.center(150,'*'),'red',attrs=['bold']))
    print (colored('\n\nMENU REMOVER----------------->  Opção:','yellow'))
    print (colored(''.center(38,'-'),'grey', attrs=['bold']))
    print (colored('REMOVER Autor---------------->   ','green'),end=''), print('| 1 |')
    print (colored('REMOVER Livro---------------->   ','green'),end=''), print('| 2 |')
    print (colored('RETORNAR--------------------->   ','green'),end=''), print('| 0 |') # fazer
    print (colored(''.center(38,'-'),'grey'))

def tela_rem_autor():
    system('cls')
    cabecalho()
    print (colored('*'.center(150,'*'),'red',attrs=['bold']))
    print (colored('   REMOVER Autor   '.center(150,'▓',),'red',attrs=['bold']))
    print (colored('*'.center(150,'*'),'red',attrs=['bold']))

def tela_rem_livro():
    system('cls')
    cabecalho()
    print (colored('*'.center(150,'*'),'red',attrs=['bold']))
    print (colored('   REMOVER Livro   '.center(150,'▓',),'red',attrs=['bold']))
    print (colored('*'.center(150,'*'),'red',attrs=['bold']))

def tela_listagem():
    system('cls')
    cabecalho()
    print (colored('*'.center(150,'*'),'yellow',attrs=['bold']))
    print (colored('   LISTAR   '.center(150,'▓',),'yellow',attrs=['bold']))
    print (colored('*'.center(150,'*'),'yellow',attrs=['bold']))
    print (colored('\n\nMENU LISTAR------------------>  Opção:','yellow'))
    print (colored(''.center(38,'-'),'grey', attrs=['bold']))
    print (colored('LISTAR Autor----------------->   ','green'),end=''), print('| 1 |')
    print (colored('LISTAR Livros---------------->   ','green'),end=''), print('| 2 |')
    print (colored('RETORNAR--------------------->   ','green'),end=''), print('| 0 |') # fazer
    print (colored(''.center(38,'-'),'grey'))

def tela_list_autor():
    system('cls')
    cabecalho()
    print (colored('*'.center(150,'*'),'blue',attrs=['bold']))
    print (colored('   LISTAR Autor   '.center(150,'▓',),'blue',attrs=['bold']))
    print (colored('*'.center(150,'*'),'blue',attrs=['bold']))

def tela_list_livros():
    system('cls')
    cabecalho()
    print (colored('*'.center(150,'*'),'yellow',attrs=['bold']))
    print (colored('   LISTAR Livros  '.center(150,'▓',),'yellow',attrs=['bold']))
    print (colored('*'.center(150,'*'),'yellow',attrs=['bold']))
    print (colored('\n\nMENU LISTAR LIVROS----------->  Opção:','yellow'))
    print (colored(''.center(38,'-'),'grey', attrs=['bold']))
    print (colored('LISTAR - Todos os Livros----->   ','green'),end=''), print('| 1 |')
    print (colored('LISTAR - Livros até valor---->   ','green'),end=''), print('| 2 |')
    print (colored('LISTAR - Livros entre valores>   ','green'),end=''), print('| 3 |')
    print (colored('LISTAR - Livros acima valor-->   ','green'),end=''), print('| 4 |')
    print (colored('RETORNAR--------------------->   ','green'),end=''), print('| 0 |') # fazer
    print (colored(''.center(38,'-'),'grey'))

def tela_list_todos_livros():
    system('cls')
    cabecalho()
    print (colored('*'.center(150,'*'),'yellow',attrs=['bold']))
    print (colored('   LISTAR Livros  '.center(150,'▓',),'yellow',attrs=['bold']))
    print (colored('*'.center(150,'*'),'yellow',attrs=['bold']))

def saida():
    system('cls')
    print ('\n\n\n')
    print ('*'.center(150,'*'))
    print (colored(' OBRIGADO POR USAR ESTE PROGRAMA '.center(150,'▓'),'red'))
    print ('*'.center(150,'*'))
    time.sleep(3)
'''
def connection():
    global conexao
    servidor = 'localhost/xe'
    usuario  = 'system'
    senha    = 'oracle'
    try:
        conexao = cx_Oracle.connect(dsn=servidor,user=usuario,password=senha)
        cursor  = conexao.cursor()
    except cx_Oracle.DatabaseError:
        print ('Erro de conexão com o BD\n')
        return
    '''
    try:
        cursor.execute('DROP TABLE Autorias')
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a tabela nao existe

    try:
        cursor.execute('DROP SEQUENCE seqAutores')
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a sequencia nao existe

    try:
        cursor.execute('DROP TABLE Autores')
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a tabela nao existe

    try:
        cursor.execute('DROP SEQUENCE seqLivros')
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a sequencia nao existe

    try:
        cursor.execute('DROP TABLE Livros')
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a tabela nao existe
    '''
    try:
        cursor.execute('CREATE SEQUENCE seqAutores START WITH 1 INCREMENT BY 1 MINVALUE 1 MAXVALUE 999 NOCACHE CYCLE')
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a sequência já existe

    try:
        cursor.execute('CREATE TABLE Autores (Id NUMBER(3) PRIMARY KEY, Nome NVARCHAR2(50) UNIQUE NOT NULL)')
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a tabela já existe

    try:
        cursor.execute('CREATE SEQUENCE seqLivros START WITH 1 INCREMENT BY 1 MAXVALUE 999 NOCACHE CYCLE')
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a tabela já existe

    try:
        cursor.execute('CREATE TABLE Livros (Codigo NUMBER(5) PRIMARY KEY, Nome NVARCHAR2(50) UNIQUE NOT NULL, Preco NUMBER(5,2) NOT NULL)')
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a tabela já existe

    try:
        cursor.execute('CREATE TABLE Autorias (Id NUMBER(3), Codigo NUMBER(5), FOREIGN KEY (Id) REFERENCES Autores(Id), FOREIGN KEY (Codigo) REFERENCES Livros(Codigo))')
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a tabela já existe

def centralizar_window(window):
    windowWidth =  window.winfo_reqwidth()
    windowHeight = window.winfo_reqheight()
    #messagebox.showinfo('Teste', 'Width' + str(windowWidth) + 'Height' + str(windowHeight))
    # Gets both half the screen width/height and window width/height
    positionRight = int(window.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(window.winfo_screenheight()/2 - windowHeight/2)
    # Positions the window in the center of the page.
    window.geometry("+{}+{}".format(positionRight, positionDown))


#============================================================================
class Programa(object):

    def __init__(self, parent):
        connection()
        self.Tela_Prin = parent
        centralizar_window(self.Tela_Prin)
        self.Tela_Prin.geometry('680x420+350+150')
        self.Tela_Prin.title('Livraria - PROGRAMA PARA PARA CADASTRAR LIVROS\
 E SEUS AUTORES')
        MenuBar = Menu(self.Tela_Prin)
        self.Tela_Prin.config(menu=MenuBar)
        #====================================================================
        #Menu Cadastrar 
        Menu_Cad= Menu(MenuBar, tearoff=0)  
        Menu_Cad.add_command(label='Autor')
        Menu_Cad.add_command(label='Livro') 
        #Menu_Cad.add_separator()  
        #Menu_Cad.add_command(label="Sair", command=_quit)  
        MenuBar.add_cascade(label='Cadastrar', menu=Menu_Cad)
        #====================================================================
        #Menu Remover 
        Menu_Rem= Menu(MenuBar, tearoff=0)  
        Menu_Rem.add_command(label='Autor')
        Menu_Rem.add_command(label='Livro') 
        #Menu_Cad.add_separator()  
        #Menu_Cad.add_command(label="Sair", command=_quit)  
        MenuBar.add_cascade(label='Remover', menu=Menu_Rem)
        ########################################################
        #Menu Listagem 
        Menu_Lis= Menu(MenuBar, tearoff=0)  
        Menu_Lis.add_command(label='Autores')
        MenuBar.add_cascade(label="Listagem", menu=Menu_Lis)
        Menu_Lis1 = Menu(Menu_Lis, tearoff=0)
        Menu_Lis1.add_command(label='Listar Todos os Livros')
        Menu_Lis1.add_command(label='LISTAR - Livros até valor')
        Menu_Lis1.add_command(label='LISTAR - Livros entre valores')
        Menu_Lis1.add_command(label='LISTAR - Livros acima valor')
        Menu_Lis.add_cascade(label='Livros', menu=Menu_Lis1)
        ##########################################################
        #Menu Sair
        Menu_Sair= Menu(MenuBar, tearoff=0)  
        #Menu_Cad.add_command(label='Autor')
        #Menu_Cad.add_command(label='Livro') 
        #Menu_Cad.add_separator()  
        Menu_Sair.add_command(label="Sair", command=self._quit)  
        MenuBar.add_cascade(label='Sair', menu=Menu_Sair)
        #############################################################
        #Barra de Status
        statusbar = tk.Label(self.Tela_Prin, text='Livraria BD + GUI', bd=1, relief=tk.SUNKEN, anchor=tk.W)
        statusbar.pack(side=tk.BOTTOM, fill=tk.X)
 
        #Menu_Cad.add_separator()  
        #Menu_Cad.add_command(label="Sair", command=_quit)  

        #self.Tela_Prin.mainloop()


    def _quit(self):  
        self.Tela_Prin.quit()
        self.Tela_Prin.destroy()
        #exit()   



if __name__ == '__main__':
    try:
        #Programa() #Chamando a classe
        #mainloop() #Aguardando eventos mantedo a tela ativa
        root = Tk()
        #root.update()
        #root.deiconify()    
        myapp = Programa(root) #Chamando a classe
        root.mainloop() #Aguardando eventos mantedo a tela ativa
        #Programa_Prin._quit()
    except:
        messagebox.showinfo('Erro', 'Erro ao carregar programa principal')
        messagebox.showerror('Error',str(sys.exc_info()[0]) + ': ' + str(sys.exc_info()[1]))