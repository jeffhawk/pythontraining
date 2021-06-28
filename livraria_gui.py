#coding: utf-8
#############################################################################
'''PROJETO DE SALA DE AULA - SISTEMA DE LIVRARIA
Software/Programa desenvolvido aplicando os conhecimentos obtidos em sala de 
aula para obtenção de nota na matéria de APPC
no curso de SISTEMAS DE INFORMAÇÃO, sob a supervisão do Ilmo. 
Prof. André de Carvalho

JEFFERSON EDUARDO LUIZ
RA 19568823

Foi empregado todo o conhecimento obtido em sala de aula e acrescentado 
algumas funcionalidades aprendidas de forma autônoma ao curso.
Também foi utilizado o GUI(Graphical User Interface) Tkinter para 
desenvolvimento do programa.

Estou tentando manter o estilo seguindo o guia do Python:
https://www.python.org/dev/peps/pep-0008/#maximum-line-length
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
import tkinter
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
caminho = sys.path[0] + '\InstantClient'
biblios = ['pip','cx_Oracle','setuptools','pywin32']
atua = ''
i=0
ico = sys.path[0] + './images/livraria1.png'
#Variável de controle para saber se está tudo ok e seguir com a execução
#biblio = False 

#============================================================================
# Verifica se existe as bibliotecas, caso contrário pergunta se quer 
# instala-las. Faço várias verificações de erros.
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
        Phantom.deiconify()
        Phantom.update()
        Phantom.destroy()
        biblio = True #Aqui sai do laço
    except ImportError as error1:
        from os import system
        messagebox.showerror('Erro Bibliotecas','Error: ' + str(error1))
        messagebox.showerror('Erro Bibliotecas','Erro ao tentar importar'+ \
            ' bibliotecas necessárias!!')
        atua = messagebox.askyesno('Instalar Bibliotecas','Deseja instalar as'+\
            ' bibliotecas necessárias? - S/N: ')
        if atua == YES:
            try:
                import pip
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', \
                    '--upgrade', 'pip'])
                for i in biblios:
                    subprocess.check_call([sys.executable, '-m', 'pip', \
                        'install', i])
                messagebox.showinfo('Bibliotecas','Instalação concluída!')
            except ImportError as errorimp:
                messagebox.showerror('Erro Bibliotecas','Error: '+ str(errorimp))
                raise
            except:
                messagebox.showerror('Erro','Unexpected error:')
                raise
        else:
            messagebox.showerror('Erro', 'Bibliotecas não instaladas,'+\
                ' Saindo...!')
            biblio = False
            quit()
    except OSError as err:
        messagebox.showerror('Erro OS', 'OS error: ' + str(err))
        if not os.path.exists(caminho):
            messagebox.showerror('OS Erro','Diretório não encontrado ou não'+\
                ' existe',)
            caminho = askstring('OS Error:', 'Entre com o caminho do Instant'+\
                ' Client: ')
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
print(atua)
if atua == YES:
    system('python.exe livraria_gui.py')
    #subprocess.check_call([sys.executable, '.\livraria_gui.py'])
    #quit()

#============================================================================

def verificaLivro(livro):
    T = Conecta_Bd()
    cursor    = T.conexao.cursor()
    cursor.execute("SELECT Codigo FROM Livros WHERE Nome='"+livro+"'")
    cursor.commit()
    return livro
               
def removaLivro (conexao):
    rem = 'N'
    
    try:
        cursor = conexao.cursor()
        nome = input('\nNome do livro? ')
        if not nome:
            messagebox.showinfo('Info','Favor entrar com o nome do Livro, não pode ser em branco!')
            return
        cursor.execute("SELECT Codigo FROM Livros WHERE Nome='"+nome+"'")
        linha = cursor.fetchone()    
        if not linha:
            messagebox.showinfo('Info','Livro não encontrado')
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
                messagebox.showinfo('Info','Livro removido com sucesso')
            else:
                linha = ''
                return
    except cx_Oracle.DataError as err:
                messagebox.showinfo('Info','DataBase error: {0}'.format(err), sys.exc_info()[0])
    except cx_Oracle.DatabaseError as err:
        error, = err.args
        messagebox.showinfo('Info','Oracle-Error-Code:', error.code)
        messagebox.showinfo('Info','Oracle-Error-Message:', error.message)
        if error.code == 1400:
            messagebox.showinfo('Info','Você deve inserir um nome para o Livro, não pode ser em branco')
            return
        #messagebox.showinfo('Info','DataBase error: {0}'.format(err), sys.exc_info()[0])
        elif error.code == 1:
            messagebox.showinfo('Info','Livro repetido')
            return
        elif error.code == 936:
            stack = inspect.stack()
            messagebox.showinfo('Info','Erro de Sintax, favor verificar código', stack[1].function)
        elif error.code == 933:
            messagebox.showinfo('Info','Favor usar "." ao invés de "," nos valores numéricos decimais')
        elif error.code == 904:
            messagebox.showinfo('Info','Campo não encontrado na tabela')
      
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
        messagebox.showinfo('Info','DataBase error: {0}'.format(err), sys.exc_info()[0])
    except cx_Oracle.DatabaseError as err:
        error, = err.args
        messagebox.showinfo('Info','Oracle-Error-Code:', error.code)
        #print('Oracle-Error-Message:', error.message)
        if error.code == 1400:
            messagebox.showinfo('Info','Você deve inserir um nome para o Livro, não pode ser em branco')
        #messagebox.showinfo('Info','DataBase error: {0}'.format(err), sys.exc_info()[0])
        elif error.code == 1:
            messagebox.showinfo('Info','Livro repetido')
        messagebox.showinfo('Info','DataBase error: {0}'.format(err), sys.exc_info()[0])
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
                messagebox.showinfo('Info','Digite um valor')
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
            messagebox.showinfo('Info','Você deve digitar um valor')
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

def centralizar_window(window):
    window.withdraw()
    window.update_idletasks()
    windowWidth =  window.winfo_reqwidth()
    windowHeight = window.winfo_reqheight()
    #messagebox.showinfo('Teste', 'Width' + str(windowWidth) + 'Height' + str(windowHeight))
    # Gets both half the screen width/height and window width/height
    positionRight = int(window.winfo_screenwidth()/2.5 - windowWidth/1.5)
    positionDown = int(window.winfo_screenheight()/2.5 - windowHeight/1.75)

    '''print(windowWidth)
    print(windowHeight)
    print(window.winfo_screenwidth())
    print(window.winfo_screenheight())
    print(positionRight)
    print(positionDown)'''
    # Positions the window in the center of the page.
    window.geometry("+{}+{}".format(positionRight, positionDown))
    #print(window.geometry())
    window.deiconify()

#============================================================================
class Conecta_Bd: #Definindo a conexão ao banco de dados

    def __init__(self) -> None:
        self.servidor = 'localhost/xe'
        self.usuario  = 'system'
        self.senha    = 'oracle'
        self.conexao = cx_Oracle.connect(dsn=self.servidor,user=self.usuario,password=self.senha)

    def connection(self):
        #global conexao
        servidor = 'localhost/xe'
        usuario  = 'system'
        senha    = 'oracle'
        try:
            self.conexao = cx_Oracle.connect(dsn=self.servidor,user=self.usuario,password=self.senha)
            cursor  = self.conexao.cursor()
        except cx_Oracle.DatabaseError:
            print ('Erro de conexão com o BD\n')
            return
        try:
            cursor.execute('CREATE SEQUENCE seqAutores START WITH 1 INCREMENT BY 1 MINVALUE 1 MAXVALUE 999 NOCACHE CYCLE')
            self.conexao.commit()
        except cx_Oracle.DatabaseError:
            pass # ignora, pois a sequência já existe

        try:
            cursor.execute('CREATE TABLE Autores (Id NUMBER(3) PRIMARY KEY, Nome NVARCHAR2(50) UNIQUE NOT NULL)')
            self.conexao.commit()
        except cx_Oracle.DatabaseError:
            pass # ignora, pois a tabela já existe

        try:
            cursor.execute('CREATE SEQUENCE seqLivros START WITH 1 INCREMENT BY 1 MAXVALUE 999 NOCACHE CYCLE')
            self.conexao.commit()
        except cx_Oracle.DatabaseError:
            pass # ignora, pois a tabela já existe

        try:
            cursor.execute('CREATE TABLE Livros (Codigo NUMBER(5) PRIMARY KEY, Nome NVARCHAR2(50) UNIQUE NOT NULL, Preco NUMBER(5,2) NOT NULL)')
            self.conexao.commit()
        except cx_Oracle.DatabaseError:
            pass # ignora, pois a tabela já existe

        try:
            cursor.execute('CREATE TABLE Autorias (Id NUMBER(3), Codigo NUMBER(5), FOREIGN KEY (Id) REFERENCES Autores(Id), FOREIGN KEY (Codigo) REFERENCES Livros(Codigo))')
            self.conexao.commit()
        except cx_Oracle.DatabaseError:
            pass # ignora, pois a tabela já existe


##############################################################################
class Cad_Autor:

    def __init__(self):
        T = Conecta_Bd()
        #global Tela_Cad_User, txt_Nome_User, txt_Senha_User
        self.Tela_Cad_Autor = Tk()
        self.Tela_Cad_Autor.title('Cadastro de Autores')
        centralizar_window(self.Tela_Cad_Autor)
        self.Tela_Cad_Autor.config()
        self.Tela_Cad_Autor.geometry('250x100')
        #---------------------------------------------------------------------
        Frame_Titulo_Autor = Frame(self.Tela_Cad_Autor)
        Frame_Titulo_Autor.pack(side=TOP)
        lblCadAutor = Label(Frame_Titulo_Autor, text='Cadastro de Autores', \
            font=('Arial', 16, 'bold'), fg='blue')
        lblCadAutor.pack(side=TOP)
        Frame_Dados_Autor = Frame(self.Tela_Cad_Autor)
        Frame_Dados_Autor.pack()
        lbl_Nome_Autor = Label(Frame_Dados_Autor, text='Autor: ', font=(\
            "Verdana", "8",'bold'))
        lbl_Nome_Autor.grid(row=0)
        self.txt_Nome_Autor = Entry(Frame_Dados_Autor, font=("Verdana", "8",\
            'bold'))
        self.txt_Nome_Autor.grid(row=0, column=1)
        #lbl_Pass_Autor = Label(Frame_Dados_Autor, text='Senha: ', font=\
        # ("Verdana", "8",'bold'))
        #lbl_Pass_Autor.grid(row=1)
        #txt_Senha_Autor = Entry(Frame_Dados_Autor, font=("Verdana", "8",\
        # 'bold'), show='*')
        #txt_Senha_Autor.grid(row=1, column=1)
        self.txt_Nome_Autor.focus()
        #---------------------------------------------------------------------
        Frame_Btn_Cad_Autor = Frame(self.Tela_Cad_Autor)
        Frame_Btn_Cad_Autor.pack(side=BOTTOM)
        btn_Cad_Autor = Button(Frame_Btn_Cad_Autor, text='Cadastrar', \
            command=lambda: self.cadastrar_autor(self.txt_Nome_Autor.get()), \
                fg='blue', font=("Verdana", "8",'bold'))
        #btn_Entrar.bind('<Button-1>', logar)
        btn_Cad_Autor.pack(side=LEFT)
        btn_Sair_Cad = Button(Frame_Btn_Cad_Autor, text='Cancelar', fg='blue'\
            , command=self.Tela_Cad_Autor.destroy, font=("Verdana", "8",'bold'))
        btn_Sair_Cad.pack(side=RIGHT)
    #=========================================================================
    def cadastrar_autor(self, autor):
        stack = inspect.stack()
        try:
            Conecta_Bd()
            T = Conecta_Bd()
            cursor = T.conexao.cursor()
            nome   = autor
            cursor.execute("INSERT INTO Autores (Id,Nome) VALUES \
                (seqAutores.nextval,'"+nome+"')")
            T.conexao.commit()
        except cx_Oracle.DataError as err:
            messagebox.showerror('Erro DB','DataBase error: {0}'.format(err), sys.exc_info()[0])
        except cx_Oracle.DatabaseError as err:
            error, = err.args
            messagebox.showerror('Erro DB','Oracle-Error-Code:', error.code)
            messagebox.showerror('Erro DB','Oracle-Error-Message:', error.message)
            if error.code == 1400:
                messagebox.showerror('Erro DB','Você deve inserir um nome para o Autor, não pode ser \
                    em branco', stack[1].function)
                return
            elif error.code == 1:
                messagebox.showerror('Erro DB','Autor repetido')
                return
            elif error.code == 936:
                messagebox.showerror('Erro DB','Erro de Sintax, favor verificar código', stack[1].\
                    function)
            elif error.code == 933:
                messagebox.showerror('Erro DB','Favor usar "." ao invés de "," nos valores numéricos\
                     decimais')
            elif error.code == 904:
                messagebox.showerror('Erro DB','Campo não encontrado na tabela')
        except KeyError:
            messagebox.showerror('Erro DB','Erro de Sintax, favor verificar código', stack[1].function)
        except:
            messagebox.showerror('Erro DB','DataBase error: {0}', sys.exc_info()[0])
        else:
            messagebox.showinfo('Info','Autor cadastrado com sucesso')
            self.Tela_Cad_Autor.destroy()

    def limpar(self):
        pass

##############################################################################
class Remov_Autor:

    def __init__(self) -> None:
        pass
        '''#global Tela_Lista_Func, tv
        self.Tela_Remov_Autor = Tk()
        self.Tela_Remov_Autor.title('Remover Autores')
        #self.Tela_Lista_Func.geometry('450x280')
        centralizar_window(self.Tela_Lista_Func)
        
        self.Frame_func = LabelFrame(self.Tela_Lista_Func, text='Autores:')
        self.Frame_func.pack(fill='both', expand='yes', padx=10, pady=10)

        self.tv = ttk.Treeview(self.Frame_func, columns=('ID',\
            'Nome'), show='headings' )
        ### 'Setor', 'Salario_Bruto', 'Bonus', 'Meses', 'Dias','Dep'), show='headings')
        self.tv.column('ID', minwidth=0, width=30)
        self.tv.column('Nome', minwidth=0, width=250)
        #self.tv.column('Setor', minwidth=0, width=150)
        #self.tv.column('Salario_Bruto', minwidth=0, width=70)
        #self.tv.column('Bonus', minwidth=0, width=50)
        #self.tv.column('Meses', minwidth=0, width=80)
        #self.tv.column('Dias', minwidth=0, width=60)
        #self.tv.column('Dep', minwidth=0, width=60)
        self.tv.heading('ID', text='ID')
        self.tv.heading('Nome', text='Nome Autor')
        #self.tv.heading('Setor', text='Setor')
        #self.tv.heading('Salario_Bruto', text='Sal. Bruto')
        #self.tv.heading('Bonus', text='Bonus')
        #self.tv.heading('Meses', text='M. Trabalhados')
        #self.tv.heading('Dias', text='Dias/Férias')
        #self.tv.heading('Dep', text='Dependentes')
        self.tv.pack()
        self.listar_autor()'''

    #=========================================================================
    def remover_autor(self, autor):
        try:
            T = Conecta_Bd()
            cursor = T.conexao.cursor()
            nome   = autor
            if not nome:
                messagebox.showinfo('Info','Você deve inserir um nome para o Autor, não pode ser em branco')
                return
            cursor.execute("SELECT Id FROM Autores WHERE Nome='"+nome+"'")
            T.conexao.commit ()
            linha = cursor.fetchone()
            if not linha:
                messagebox.showinfo('Info','Autor inexistente')
            else:
                cursor.execute("DELETE FROM Autores WHERE Nome='"+nome+"'")
                T.conexao.commit ()
                messagebox.showinfo('Info','Autor removido com sucesso')
        except cx_Oracle.DataError as err:
            messagebox.showinfo('Erro','DataBase error: {0}'.format(err), sys.exc_info()[0])
        except cx_Oracle.DatabaseError as err:
            error, = err.args
            messagebox.showinfo('Erro','Oracle-Error-Code:', error.code)
            messagebox.showinfo('Erro','Oracle-Error-Message:', error.message)
            if error.code == 1400:
                messagebox.showinfo('Info','Você deve inserir um nome para o Autor, não pode ser em branco')
                return
            elif error.code == 1:
                messagebox.showinfo('Info','Autor repetido')
                return
            elif error.code == 936:
                stack = inspect.stack()
                messagebox.showinfo('Info','Erro de Sintax, favor verificar código', stack[1].function)
            elif error.code == 933:
                messagebox.showinfo('Info','Favor usar "." ao invés de "," nos valores numéricos decimais')
            elif error.code == 2292:
                messagebox.showinfo('Info','O autor tem livros cadastrados, favor remover os livros primeiro!')
            elif error.code == 904:
                messagebox.showinfo('Info','Campo não encontrado na tabela')
        except:
            messagebox.showinfo('Info','DataBase error: {0}', sys.exc_info()[0])
        

##############################################################################
class Cad_Livro:
    def __init__(self):
        T = Conecta_Bd()
        #global Tela_Cad_User, txt_Nome_User, txt_Senha_User
        self.Tela_Cad_Livro = Tk()
        self.Tela_Cad_Livro.title('Cadastro de Livros')
        self.Tela_Cad_Livro.geometry('350x200')
        centralizar_window(self.Tela_Cad_Livro)
        self.Tela_Cad_Livro.config()
        
        #--------------------------------------------------------------------
        Frame_Titulo_Livro = Frame(self.Tela_Cad_Livro)
        Frame_Titulo_Livro.pack(side=TOP)
        lblCadLivro = Label(Frame_Titulo_Livro, text='Cadastro de Livros', \
            font=('Arial', 16, 'bold'), fg='blue')
        lblCadLivro.pack(side=TOP)
        Frame_Dados_Livro = Frame(self.Tela_Cad_Livro)
        Frame_Dados_Livro.pack()
        
        #--------------------------------------------------------------------
        lbl_Nome_Livro = Label(Frame_Dados_Livro, text='Nome do Livro: ', \
            font=("Verdana", "8",'bold'))
        lbl_Nome_Livro.grid(row=0)
        txt_Nome_Livro = Entry(Frame_Dados_Livro, font=("Verdana", "8",\
            'bold'))
        txt_Nome_Livro.grid(row=0, column=1)

        lbl_Nome_Autor = Label(Frame_Dados_Livro, text='Autor: ', font=(\
            "Verdana", "8",'bold'))
        lbl_Nome_Autor.grid(row=1)
        txt_Nome_Autor = Entry(Frame_Dados_Livro, font=("Verdana", "8",\
            'bold'))
        txt_Nome_Autor.grid(row=1, column=1)
        
        lbl_Valor_Livro = Label(Frame_Dados_Livro, text='Valor: ', font=(\
            "Verdana", "8",'bold'))
        lbl_Valor_Livro.grid(row=2)
        txt_Valor_Livro = Entry(Frame_Dados_Livro, font=("Verdana", "8",\
            'bold'))
        txt_Valor_Livro.grid(row=2, column=1)
        txt_Nome_Livro.focus()
    

        Frame_Btn_Cad_Autor = Frame(self.Tela_Cad_Livro)
        Frame_Btn_Cad_Autor.pack(side=BOTTOM)
        btn_Cad_Autor = Button(Frame_Btn_Cad_Autor, text='Cadastrar', \
            command=lambda: self.cadastrar_livro(txt_Nome_Livro.get(),\
                 txt_Nome_Autor.get(), txt_Valor_Livro.get()), \
                     fg='blue', font=("Verdana", "8",'bold'))
        #btn_Entrar.bind('<Button-1>', logar)
        btn_Cad_Autor.pack(side=LEFT)
        btn_Sair_Cad = Button(Frame_Btn_Cad_Autor, text='Cancelar', \
            fg='blue', command=self.Tela_Cad_Livro.destroy, font=("Verdana",\
                 "8",'bold'))
        btn_Sair_Cad.pack(side=RIGHT)

    #========================================================================
    def cadastrar_livro(self, livro, autor, valor):
        try:
            Conecta_Bd()
            T = Conecta_Bd()
            cursor    = T.conexao.cursor()
            nomeLivro = livro
            #verificaLivro(nomeLivro)
            if nomeLivro == '':
                messagebox.showinfo('Info','Precisa entrar com um nome de Livro!')
                return
            precoLivro = float(valor)
        except ValueError:
           messagebox.showerror('Erro DB','Preço inválido, Favor usar "."'+\
               ' ao invés de "," nos valores numéricos decimais')
        else: 
            nomeAutor = autor
            cursor.execute("SELECT Id FROM Autores WHERE Nome='"+nomeAutor+"'")
            linha = cursor.fetchone()
            if not linha:
                messagebox.showinfo0('Info','Autor inexistente')
            else:
                idAutor = linha[0]
                try:
                    cursor.execute("INSERT INTO Livros (Codigo,Nome,Preco)\
                         VALUES (seqLivros.nextval,'"+nomeLivro+"',"\
                             +str(precoLivro)+")")
                    T.conexao.commit()
                except cx_Oracle.DataError as err:
                    messagebox.showerror('Erro DB','DataBase error: {0}'\
                        .format(err), sys.exc_info()[0])
                except cx_Oracle.DatabaseError as err:
                    error, = err.args
                    messagebox.showerror('Erro DB','Oracle-Error-Code:',\
                         error.code)
                    messagebox.showerror('Erro DB','Oracle-Error-Message:',\
                         error.message)
                    if error.code == 1400:
                        messagebox.showerror('Erro DB','Você deve inserir'+\
                            ' um nome para o Livro, não pode ser em branco')
                        return
                    elif error.code == 1:
                        messagebox.showerror('Erro DB','Livro já cadastrado')
                        return
                    elif error.code == 936:
                        stack = inspect.stack()
                        messagebox.showerror('Erro DB','Erro de Sintax, favor verificar código', stack[1].function)
                    elif error.code == 933:
                        messagebox.showerror('Erro DB','Favor usar "." ao invés de "," nos valores numéricos decimais')
                    elif error.code == 904:
                        messagebox.showerror('Erro DB','Campo não encontrado na tabela')
                else:
                    cursor.execute("SELECT Codigo FROM Livros WHERE Nome='"+nomeLivro+"'")
                    linha  = cursor.fetchone()
                    CodigoLivro = linha[0]
                    
                    cursor.execute("INSERT INTO Autorias (Id,Codigo) VALUES ("+str(idAutor)+","+str(CodigoLivro)+")")
                    T.conexao.commit ()
                    messagebox.showinfo('Info','Livro cadastrado com sucesso')
                    self.Tela_Cad_Livro.destroy()

##############################################################################
class Listar_Aut():
    
    def __init__(self) -> None:
        #global Tela_Lista_Func, tv
        self.Tela_Lista_Aut = Tk()
        self.Tela_Lista_Aut.title('Listar Autores')
        #self.Tela_Lista_Func.geometry('450x280')
        centralizar_window(self.Tela_Lista_Aut)
        
        self.Frame_Aut = LabelFrame(self.Tela_Lista_Aut, text='Autores:')
        self.Frame_Aut.pack(fill='both', expand='yes', padx=10, pady=10)

        self.tv = ttk.Treeview(self.Frame_Aut, columns=('ID',\
            'Nome'), show='headings' )
        ### 'Setor', 'Salario_Bruto', 'Bonus', 'Meses', 'Dias','Dep'), show='headings')
        self.tv.column('ID', minwidth=0, width=30)
        self.tv.column('Nome', minwidth=0, width=250)
        #self.tv.column('Setor', minwidth=0, width=150)
        #self.tv.column('Salario_Bruto', minwidth=0, width=70)
        #self.tv.column('Bonus', minwidth=0, width=50)
        #self.tv.column('Meses', minwidth=0, width=80)
        #self.tv.column('Dias', minwidth=0, width=60)
        #self.tv.column('Dep', minwidth=0, width=60)
        self.tv.heading('ID', text='ID')
        self.tv.heading('Nome', text='Nome Autor')
        #self.tv.heading('Setor', text='Setor')
        #self.tv.heading('Salario_Bruto', text='Sal. Bruto')
        #self.tv.heading('Bonus', text='Bonus')
        #self.tv.heading('Meses', text='M. Trabalhados')
        #self.tv.heading('Dias', text='Dias/Férias')
        #self.tv.heading('Dep', text='Dependentes')
        self.tv.pack()

        Frame_Buttos = Frame(self.Tela_Lista_Aut)
        Frame_Buttos.pack()
        Btn_Rem_Aut = Button(self.Tela_Lista_Aut, text='Remover', command=lambda: messagebox.showinfo('Autor', self.tv.selection))
        Btn_Rem_Aut.pack(side=LEFT)

        self.listar_autor()
        
    def listar_autor(self):
        Conecta_Bd()
        try:
            BD = Conecta_Bd()
            cursor = BD.conexao.cursor()
            cursor.execute("SELECT * FROM Autores ORDER BY Autores.Nome")

            linha = cursor.fetchone() # linha(1,'Arthur')
            if not linha:
                messagebox.showwarning ('Alerta','Não há Funcionários cadastrados')
                return
            aut=0
            self.tv.delete(*self.tv.get_children())
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
            #print('|',end=''),print(' AUTOR '.center(aut,'*'),end=''), print('|')
            while linha:
                #print('|', end=''), print (linha[1].center(aut,' '),end=''), print('|')
                self.tv.insert('','end', values=linha)
                linha = cursor.fetchone()
        except cx_Oracle.DataError as err:
                    messagebox.showerror('DB Erro','DataBase error: ' + str(err))
        except cx_Oracle.DatabaseError as err:
            error, = err.args
            #messagebox.showerror('DB Erro','Oracle-Error-Code: '+ str(error.code))
            #messagebox.showerror('DB Erro','Oracle-Error-Message:' + str(error.message))
            if error.code == 1400:
                messagebox.showerror(error.code,'Você deve inserir um nome para o Livro, não pode ser em branco')
                return
            elif error.code == 1:
                messagebox.showerror(error.code,'Livro já cadastrado')
                return
            elif error.code == 936:
                messagebox.showerror(error.code,'Erro de Sintax, favor verificar código')
            elif error.code == 933:
                messagebox.showerror(error.code,'Favor usar "." ao invés de "," nos valores numéricos decimais')
            elif error.code == 904:
                messagebox.showerror(error.code,'Campo não encontrado na tabela')
            elif error.code == 955:
                pass
        except cx_Oracle.DatabaseError:
            messagebox.showerror('DB Error', 'Erro de conexão com o BD')
            return
        else:
            pass # ignora, pois a tabela já existe
        
##############################################################################
class Programa(object):
    '''fonte_Normal = ("Verdana", "8",'bold')
    fonte_Titulo = ('Arial', 16, 'bold')
    fonte_Texto = ('Times New Roman', 12)'''

    def __init__(self, parent):
        Conecta_Bd()
        self.Tela_Prin = parent
        self.Tela_Prin.geometry('680x420')
        centralizar_window(self.Tela_Prin)
        self.Tela_Prin.iconphoto(True, tk.PhotoImage(file=ico))
        self.Tela_Prin.title('Livraria - PROGRAMA PARA PARA CADASTRAR LIVROS\
 E SEUS AUTORES')
        MenuBar = Menu(self.Tela_Prin)
        self.Tela_Prin.config(menu=MenuBar)
        

        #====================================================================
        #Menu Cadastrar 
        Menu_Cad= Menu(MenuBar, tearoff=0)  
        Menu_Cad.add_command(label='Autor', command=Cad_Autor)
        Menu_Cad.add_command(label='Livro', command=Cad_Livro) 
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

        #====================================================================
        #Menu Listagem 
        Menu_Lis= Menu(MenuBar, tearoff=0)  
        Menu_Lis.add_command(label='Autores', command=Listar_Aut)
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
        root = tk.Tk()
        #root.update()
        #root.deiconify()
        #root.iconphoto(False, tk.PhotoImage(file=ico))
        #root.iconphoto(True, tk.PhotoImage(file=ico))
        myapp = Programa(root) #Chamando a classe
        root.mainloop() #Aguardando eventos mantedo a tela ativa
        #Programa_Prin._quit()
    except:
        raise
        messagebox.showinfo('Erro', 'Erro ao carregar programa principal')
        messagebox.showerror('Error',str(sys.exc_info()[0]) + ': ' + str(sys.exc_info()[1]))