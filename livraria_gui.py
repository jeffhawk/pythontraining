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
from tkinter.font import BOLD, Font
import inspect
from functools import partial
import string
import subprocess


#============================================================================
# Declaração de variáveis globais
biblio = False
caminho = sys.path[0] + '\InstantClient'
BIBLIOS = ['pip','cx_Oracle','setuptools','pywin32', 'pillow']
atua = ''
i=0
ICO = sys.path[0] + './images/biblioteca.png'
IMG = sys.path[0] + '/images/lendo-um-livro.png'
stack = inspect.stack()
fonte_Normal = ("Verdana", "8",'bold')
fonte_Titulo = ('Arial', 16, 'bold')
fonte_Texto = ('Times New Roman', 12)

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
        import PIL
        from PIL import Image
        from PIL import ImageQt
        from PIL import ImageTk

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
                for i in BIBLIOS:
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
        import PIL
        from PIL import Image
        from PIL import ImageQt
        from PIL import ImageTk
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
        servidor = 'localhost/xe'
        usuario  = 'system'
        senha    = 'oracle'
        try:
            self.conexao = cx_Oracle.connect(dsn=self.servidor,user=self.usuario,password=self.senha)
            cursor  = self.conexao.cursor()
        except cx_Oracle.DatabaseError:
            messagebox.showerror('Erro','Erro de conexão com o BD')
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
    BD = Conecta_Bd()
    def __init__(self):
        
        #global Tela_Cad_User, txt_Nome_User, txt_Senha_User
        self.Tela_Cad_Autor = Toplevel()
        self.Tela_Cad_Autor.title('Cadastro de Autores')
        centralizar_window(self.Tela_Cad_Autor)
        self.Tela_Cad_Autor.config()
        #self.Tela_Cad_Autor.geometry('250x100')
        #---------------------------------------------------------------------
        Frame_Titulo_Autor = Frame(self.Tela_Cad_Autor)
        Frame_Titulo_Autor.pack(side=TOP, fill='both', expand='yes', padx=5, pady=5)
        lblCadAutor = Label(Frame_Titulo_Autor, text='Cadastro de Autores', \
            font=('Arial', 16, 'bold'), fg='blue')
        lblCadAutor.pack(side=TOP, fill='both', expand='yes', padx=5, pady=5)
        Frame_Dados_Autor = LabelFrame(self.Tela_Cad_Autor, text='Cadastro:')
        Frame_Dados_Autor.pack(fill='both', expand='yes', padx=10, pady=10)
        lbl_Nome_Autor = Label(Frame_Dados_Autor, text='Autor: ', font=(\
            "Verdana", "8",'bold'))
        lbl_Nome_Autor.grid(row=0)
        self.txt_Nome_Autor = Entry(Frame_Dados_Autor, font=("Verdana", "8",\
            'bold'))
        self.txt_Nome_Autor.grid(row=0, column=1, padx=10, pady=15)
        #lbl_Pass_Autor = Label(Frame_Dados_Autor, text='Senha: ', font=\
        # ("Verdana", "8",'bold'))
        #lbl_Pass_Autor.grid(row=1)
        #txt_Senha_Autor = Entry(Frame_Dados_Autor, font=("Verdana", "8",\
        # 'bold'), show='*')
        #txt_Senha_Autor.grid(row=1, column=1)
        self.txt_Nome_Autor.focus()
        #---------------------------------------------------------------------
        Frame_Btn_Cad_Autor = Frame(self.Tela_Cad_Autor)
        Frame_Btn_Cad_Autor.pack(side=BOTTOM, fill='both', expand='yes', padx=10, pady=10)
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
        #stack = inspect.stack()
        try:
            cursor = self.BD.conexao.cursor()
            nome   = autor
            cursor.execute("INSERT INTO Autores (Id,Nome) VALUES \
                (seqAutores.nextval,'"+nome+"')")
            self.BD.conexao.commit()
        except cx_Oracle.DataError as err:
            messagebox.showerror('Erro DB','DataBase error: '+\
                + str((err))+', ' +str(sys.exc_info()[0]))
            self.Tela_Cad_Autor.focus()
        except cx_Oracle.DatabaseError as err:
            error, = err.args
            messagebox.showerror('Erro DB','Oracle-Error-Code:'+\
                 str(error.code))
            messagebox.showerror('Erro DB','Oracle-Error-Message:'+\
                str(error.message))
            #messagebox.showerror('Erro DB','DataBase error: {0}.
            # format('+str(err)+'))' + str(sys.exc_info()[0]))
            if error.code == 1400:
                messagebox.showerror('Erro DB','Você deve inserir um nome para o Autor, não pode ser em branco.')
                self.Tela_Cad_Autor.focus()
                self.txt_Nome_Autor.focus_set()
                return
            elif error.code == 1:
                messagebox.showerror('Erro DB','Autor já cadastrado')
                self.Tela_Cad_Autor.focus()
                self.txt_Nome_Autor.delete(first=0, last='end') 
                # outra sintax: (0, 'end') onde o 0 representa o primeiro
                #caracter
                self.txt_Nome_Autor.focus_set()
                return
            elif error.code == 936:
                messagebox.showerror('Erro DB','Erro de Sintax, favor '+\
                    'verificar código' + str(stack[1].function))
                self.Tela_Cad_Autor.focus()
            elif error.code == 933:
                messagebox.showerror('Erro DB','Favor usar "." ao invés de'+\
                    ' "," nos valores numéricos decimais')
                self.Tela_Cad_Autor.focus()
            elif error.code == 904:
                messagebox.showerror('Erro DB','Campo não encontrado na'+\
                    ' tabela')
                self.Tela_Cad_Autor.focus()
        except KeyError:
            messagebox.showerror('Erro DB','Erro de Sintax, favor verificar código' +str(stack[1].function))
            self.Tela_Cad_Autor.focus()
        except:
            raise
            messagebox.showerror('Erro DB','DataBase error: ' + str(sys.exc_info()[0]))
            self.Tela_Cad_Autor.focus()
        else:
            messagebox.showinfo('Info','Autor cadastrado com sucesso')
            self.Tela_Cad_Autor.destroy()
    #=========================================================================
    def limpar(self):
        pass

##############################################################################
class Listar_Aut:
    BD = Conecta_Bd()
    
    def __init__(self) -> None:
        #global Tela_Lista_Func, tv
        self.Tela_Lista_Aut = Toplevel()
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
        self.tv.pack( padx=10, pady=10)

        self.listar_autor()
        
    def listar_autor(self):
        try:
            cursor = self.BD.conexao.cursor()
            cursor.execute("SELECT * FROM Autores ORDER BY Autores.Nome")

            linha = cursor.fetchone() # linha(1,'Arthur')
            if not linha:
                messagebox.showwarning ('Alerta','Não há Autores cadastrados')
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
            messagebox.showerror('Erro DB','DataBase error: '+\
                + str((err))+', ' +str(sys.exc_info()[0]))
            self.Tela_Lista_Aut.focus()
        except cx_Oracle.DatabaseError as err:
            error, = err.args
            messagebox.showerror('Erro DB','Oracle-Error-Code:'+\
                 str(error.code))
            messagebox.showerror('Erro DB','Oracle-Error-Message:'+\
                str(error.message))
            #messagebox.showerror('Erro DB','DataBase error: {0}.
            # format('+str(err)+'))' + str(sys.exc_info()[0]))
            if error.code == 1400:
                messagebox.showerror('Erro DB','Você deve inserir um nome '+\
                    'para o Autor, não pode ser em branco. Local: ' \
                        +str(stack[0].function)+', '+ str(stack[1].function))
                self.Tela_Lista_Aut.focus()
                return
            elif error.code == 1:
                messagebox.showerror('Erro DB','Autor já cadastrado')
                self.Tela_Lista_Aut.focus()
                # outra sintax: (0, 'end') onde o 0 representa o primeiro
                #caracter
                
                return
            elif error.code == 936:
                messagebox.showerror('Erro DB','Erro de Sintax, favor '+\
                    'verificar código' + str(stack[1].function))
                self.Tela_Lista_Aut.focus()
            elif error.code == 933:
                messagebox.showerror('Erro DB','Favor usar "." ao invés de'+\
                    ' "," nos valores numéricos decimais')
                self.Tela_Lista_Aut.focus()
            elif error.code == 904:
                messagebox.showerror('Erro DB','Campo não encontrado na'+\
                    ' tabela')
                self.Tela_Lista_Aut.focus()
        except KeyError:
            messagebox.showerror('Erro DB','Erro de Sintax, favor verificar código', stack[1].function)
            self.Tela_Lista_Aut.focus()
        except:
            raise
            messagebox.showerror('Erro DB','DataBase error: ' + str(sys.exc_info()[0]))
            sself.Tela_Lista_Aut.focus()
        else:
            pass
            '''messagebox.showinfo('Info','Autor cadastrado com sucesso')
            self.Tela_Cad_Autor.destroy()'''
        
##############################################################################
class Remov_Autor:
    BD = Conecta_Bd()
    def __init__(self) -> None:
        #global Tela_Lista_Func, tv
        fonte = ("Verdana", "8",'bold')
        self.Tela_Remov_Autor = Toplevel()
        self.Tela_Remov_Autor.title('Remover Autores')
        #self.Tela_Lista_Func.geometry('450x280')
        centralizar_window(self.Tela_Remov_Autor)

        frame_Titulo = Frame(self.Tela_Remov_Autor)
        frame_Titulo.pack(side=TOP, fill='both', expand='yes', padx=1, pady=1)
        lbl_titulo = Label(frame_Titulo, text='Remover Autor', font=fonte_Titulo, fg='blue')
        lbl_titulo.pack(padx=1, pady=1)
        
        self.Frame_Rem_Autor = LabelFrame(self.Tela_Remov_Autor, text='Identificação')
        self.Frame_Rem_Autor.pack(fill='both', expand='yes', padx=5, pady=5)
        lblIdAutor = Label(self.Frame_Rem_Autor, text="Autor:", font=fonte_Normal)#, width=15)
        lblIdAutor.pack(side=LEFT, padx=10, pady=10)
        self.txtIdAutor = Entry(self.Frame_Rem_Autor)
        #self.txtIdAutor["width"] = 15
        self.txtIdAutor["font"] = fonte
        self.txtIdAutor.pack(side=LEFT, padx=10, pady=10)

        Frame_BTN = Frame(self.Tela_Remov_Autor)
        Frame_BTN.pack(side=BOTTOM, fill='both', expand='yes', padx=3, pady=3)
        btnBuscar = Button(Frame_BTN, text="Buscar", font=fonte)
        btnBuscar["command"] = lambda: self.remover_autor(self.txtIdAutor.get())
        btnBuscar.pack(side=LEFT, padx=3, pady=3)
        btn_cancelar = Button(Frame_BTN, text='Cancelar', command=self.Tela_Remov_Autor.destroy)
        btn_cancelar.pack(side=RIGHT, padx=3, pady=3)


        self.txtIdAutor.focus_set()

        self.Tela_Remov_Autor.mainloop()

    #=========================================================================
    def remover_autor(self, autor):
        #stack = inspect.stack()
        try:
            cursor = self.BD.conexao.cursor()
            nome   = autor
            if not nome:
                messagebox.showinfo('Info','Você deve inserir um nome para o Autor, não pode ser em branco')
                self.Tela_Remov_Autor.focus()
                self.txtIdAutor.focus_set()
                return
            cursor.execute("SELECT Id FROM Autores WHERE Nome='"+nome+"'")
            self.BD.conexao.commit ()
            linha = cursor.fetchone()
            if not linha:
                messagebox.showinfo('Info','Autor inexistente')
                self.Tela_Remov_Autor.focus()
                self.txtIdAutor.delete()
                self.txtIdAutor.focus_set()

            else:
                op = messagebox.askyesno('Remover', 'Você deseja realmente remover o autor ' +nome+ ' ?')
                if op == YES:
                    cursor.execute("DELETE FROM Autores WHERE Nome='"+nome+"'")
                    self.BD.conexao.commit()
                    messagebox.showinfo('Info','Autor removido com sucesso')
                self.Tela_Remov_Autor.destroy()
        except cx_Oracle.DataError as err:
            messagebox.showinfo('Erro','DataBase error: {0}'.format(err), sys.exc_info()[0])
            self.Tela_Remov_Autor.focus()
        except cx_Oracle.DatabaseError as err:
            error, = err.args
            #messagebox.showinfo('Erro','Oracle-Error-Code:' + str(error.code))
            #messagebox.showinfo('Erro','Oracle-Error-Message:'+ str(error.message))
            if error.code == 1400:
                messagebox.showinfo('Info','Você deve inserir um nome para o Autor, não pode ser em branco')
                self.Tela_Remov_Autor.focus()
                return
            elif error.code == 1:
                messagebox.showinfo('Info','Autor repetido')
                self.Tela_Remov_Autor.focus()
                return
            elif error.code == 936:
                messagebox.showinfo('Info','Erro de Sintax, favor verificar código' + str(stack[1].function))
                self.Tela_Remov_Autor.focus()
            elif error.code == 933:
                messagebox.showinfo('Info','Favor usar "." ao invés de "," nos valores numéricos decimais')
                self.Tela_Remov_Autor.focus()
            elif error.code == 2292:
                messagebox.showinfo('Info','O autor tem livros cadastrados, favor remover os livros primeiro!')
                self.Tela_Remov_Autor.destroy()
            elif error.code == 904:
                messagebox.showinfo('Info','Campo não encontrado na tabela')
                self.Tela_Remov_Autor.focus()
        except:
            messagebox.showinfo('Info','DataBase error: ' + str(sys.exc_info()[0]))
            self.Tela_Remov_Autor.focus()

##############################################################################
class Cad_Livro:
    BD = Conecta_Bd()
    def __init__(self):
        #global Tela_Cad_User, txt_Nome_User, txt_Senha_User
        self.Tela_Cad_Livro = Toplevel()
        self.Tela_Cad_Livro.title('Cadastro de Livros')
        #self.Tela_Cad_Livro.geometry('350x200')
        centralizar_window(self.Tela_Cad_Livro)
        self.Tela_Cad_Livro.config()
        
        #--------------------------------------------------------------------
        Frame_Titulo_Livro = Frame(self.Tela_Cad_Livro)
        Frame_Titulo_Livro.pack(side=TOP, fill='both', expand='yes', padx=5)
        lblCadLivro = Label(Frame_Titulo_Livro, text='Cadastro de Livros', \
            font=('Arial', 16, 'bold'), fg='blue')
        lblCadLivro.pack(side=TOP, fill='both', expand='yes', padx=5, pady=5)


        Frame_Dados_Livro = LabelFrame(self.Tela_Cad_Livro, text='Cadastro:')
        Frame_Dados_Livro.pack(fill='both', expand='yes', padx=10, pady=5)
        lbl_Nome_Livro = Label(Frame_Dados_Livro, text='Nome do Livro: ', \
            font=("Verdana", "8",'bold'))
        lbl_Nome_Livro.grid(row=0)
        self.txt_Nome_Livro = Entry(Frame_Dados_Livro, font=("Verdana", "8",\
            'bold'))
        self.txt_Nome_Livro.grid(row=0, column=1, padx=5, pady=5)

        lbl_Nome_Autor = Label(Frame_Dados_Livro, text='Autor: ', font=(\
            "Verdana", "8",'bold'))
        lbl_Nome_Autor.grid(row=1, padx=5, pady=5)
        self.txt_Nome_Autor = Entry(Frame_Dados_Livro, font=("Verdana", "8",\
            'bold'))
        self.txt_Nome_Autor.grid(row=1, column=1, padx=5, pady=5)
        
        lbl_Valor_Livro = Label(Frame_Dados_Livro, text='Valor: ', font=(\
            "Verdana", "8",'bold'))
        lbl_Valor_Livro.grid(row=2, padx=5, pady=5)
        self.txt_Valor_Livro = Entry(Frame_Dados_Livro, font=("Verdana", "8",\
            'bold'))
        self.txt_Valor_Livro.grid(row=2, column=1)
        self.txt_Nome_Livro.focus()
    

        Frame_Btn_Cad_Autor = Frame(self.Tela_Cad_Livro)
        Frame_Btn_Cad_Autor.pack(side=BOTTOM, fill='both', expand='yes', padx=10, pady=10)
        btn_Cad_Autor = Button(Frame_Btn_Cad_Autor, text='Cadastrar', \
            command=lambda: self.cadastrar_livro(self.txt_Nome_Livro.get(),\
                 self.txt_Nome_Autor.get(), self.txt_Valor_Livro.get()), \
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
            cursor    = self.BD.conexao.cursor()
            nomeLivro = livro
            #verificaLivro(nomeLivro)
            if nomeLivro == '':
                messagebox.showinfo('Info','Precisa entrar com um nome de'+\
                    ' Livro!')
                self.Tela_Cad_Livro.focus()
                self.txt_Nome_Livro.focus_set()
                return
            precoLivro = float(valor)
        except ValueError:
            messagebox.showerror('Erro DB','Preço inválido, Favor usar "."'+\
               ' ao invés de "," nos valores numéricos decimais')
            self.Tela_Cad_Livro.focus()
        else: 
            nomeAutor = autor
            if nomeAutor == '':
                messagebox.showinfo('Livros', 'Você deve digitar um nome '+\
                    'para o autor')
                self.Tela_Cad_Livro.focus()
                self.txt_Nome_Autor.focus_set()
                return
            cursor.execute("SELECT Id FROM Autores WHERE Nome='"\
                +nomeAutor+"'")
            linha = cursor.fetchone()
            if not linha:
                messagebox.showinfo('Info','Autor inexistente')
                self.Tela_Cad_Livro.focus()
            else:
                idAutor = linha[0]
                try:
                    cursor.execute("INSERT INTO Livros (Codigo,Nome,Preco)\
                         VALUES (seqLivros.nextval,'"+nomeLivro+"',"\
                             +str(precoLivro)+")")
                    self.BD.conexao.commit()
                except cx_Oracle.DataError as err:
                    messagebox.showerror('Erro DB','DataBase error: '\
                        .format(err), sys.exc_info()[0])
                    self.Tela_Cad_Livro.focus()
                except cx_Oracle.DatabaseError as err:
                    error, = err.args
                    messagebox.showerror('Erro DB','Oracle-Error-Code:',\
                         error.code)
                    messagebox.showerror('Erro DB','Oracle-Error-Message:',\
                         error.message)
                    self.Tela_Cad_Livro.focus()
                    if error.code == 1400:
                        messagebox.showerror('Erro DB','Você deve inserir'+\
                            ' um nome para o Livro, não pode ser em branco')
                        self.Tela_Cad_Livro.focus()
                        return
                    elif error.code == 1:
                        messagebox.showerror('Erro DB','Livro já cadastrado')
                        self.Tela_Cad_Livro.focus()
                        return
                    elif error.code == 936:
                        stack = inspect.stack()
                        messagebox.showerror('Erro DB','Erro de Sintax, favor verificar código'+str(stack[1].function))
                        self.Tela_Cad_Livro.focus()
                    elif error.code == 933:
                        messagebox.showerror('Erro DB','Favor usar "." ao invés de "," nos valores numéricos decimais')
                        self.Tela_Cad_Livro.focus()
                    elif error.code == 904:
                        messagebox.showerror('Erro DB','Campo não encontrado na tabela')
                        self.Tela_Cad_Livro.focus()
                else:
                    cursor.execute("SELECT Codigo FROM Livros WHERE Nome='"+nomeLivro+"'")
                    linha  = cursor.fetchone()
                    CodigoLivro = linha[0]
                    
                    cursor.execute("INSERT INTO Autorias (Id,Codigo) VALUES ("+str(idAutor)+","+str(CodigoLivro)+")")
                    self.BD.conexao.commit ()
                    messagebox.showinfo('Info','Livro cadastrado com sucesso')
                    self.Tela_Cad_Livro.destroy()

##############################################################################
class Remov_Livro:
    BD = Conecta_Bd()

    def __init__(self) -> None:
        #global Tela_Lista_Func, tv
        self.Tela_Remove_Livro = Toplevel()
        self.Tela_Remove_Livro.title('Remover Livros')
        #self.Tela_Lista_Func.geometry('450x280')
        centralizar_window(self.Tela_Remove_Livro)
        self.Tela_Remove_Livro.config()
        #Frame de Busca
        search_Frame = LabelFrame(self.Tela_Remove_Livro, text='Buscar:')
        search_Frame.pack(fill='both', expand='yes', padx=10, pady=10)
        lbl_nome_livro = Label(search_Frame,text='Livro:')
        lbl_nome_livro.pack(side=LEFT, padx=5, pady=5)
        self.txt_nome_livro = Entry(search_Frame)
        self.txt_nome_livro.pack(side=LEFT, padx=5, pady=5)
        btn_buscar = Button(search_Frame, text='Listar', command=lambda: self.busca_livro(self.txt_nome_livro.get()))
        btn_buscar.pack(side=RIGHT, padx=5, pady=5)
        #self.nome_livro = askstring('Livros', 'Você gostaria de listar livros à partir de que valor?: ')
        self.txt_nome_livro.focus_set()

        self.Frame_Livros = LabelFrame(self.Tela_Remove_Livro, text='Livros:')
        self.Frame_Livros.pack(fill='both', expand='yes', padx=10, pady=10)
        self.tv = ttk.Treeview(self.Frame_Livros, columns=('ID', 'Livro', 'Autor', 'Valor'), show='headings' )
        ### 'Setor', 'Salario_Bruto', 'Bonus', 'Meses', 'Dias','Dep'), show='headings')
        self.tv.column('ID', minwidth=0, width=20)
        self.tv.column('Livro', minwidth=0, width=120)
        self.tv.column('Autor', minwidth=0, width=90)
        self.tv.column('Valor', minwidth=0, width=50)
        #self.tv.column('Bonus', minwidth=0, width=50)
        #self.tv.column('Meses', minwidth=0, width=80)
        #self.tv.column('Dias', minwidth=0, width=60)
        #self.tv.column('Dep', minwidth=0, width=60)
        self.tv.heading('ID', text='ID')
        self.tv.heading('Livro', text='Nome Livro')
        self.tv.heading('Autor', text='Autor')
        self.tv.heading('Valor', text='Valor')
        #self.tv.heading('Bonus', text='Bonus')
        #self.tv.heading('Meses', text='M. Trabalhados')
        #self.tv.heading('Dias', text='Dias/Férias')
        #self.tv.heading('Dep', text='Dependentes')
        self.tv.pack()

        action_Frame = LabelFrame(self.Tela_Remove_Livro, text='Ações:')
        action_Frame.pack(fill='both', expand='yes', padx=10, pady=10)
        btn_deletar = Button(action_Frame, text='Excluir', command=self.remova_livro)
        btn_deletar.pack(side=LEFT, padx=5, pady=5)
        btn_Cancelar = Button(action_Frame, text='Cancelar', command=self.Tela_Remove_Livro.destroy)
        btn_Cancelar.pack(side=RIGHT, padx=5, pady=5)
        self.Tela_Remove_Livro.mainloop()
        '''
        #print(self.valor)
        if self.nome_livro == None:
            messagebox.showinfo('Erro','Você deve inserir um nome '+\
                    'para o Livro, não pode ser em branco.')
            self.Tela_Remove_Livro.destroy()
        else:
            self.remova_livro(self.nome_livro)'''

    def busca_livro(self, livro):
        try:
            cursor = self.BD.conexao.cursor()
            nome = livro+'%'
            if nome == '':
                messagebox.showinfo('Info','Favor entrar com o nome do Livro, não pode ser em branco!')
                #self.Tela_Remove_Livro.update()
                #self.Tela_Remove_Livro.deiconify()
                self.Tela_Remove_Livro.focus()
                self.txt_nome_livro.focus_set()
                return
            cursor.execute("SELECT codigo FROM Livros WHERE Nome LIKE '"+nome+"'")
            linha = cursor.fetchone()    
            if not linha:
                messagebox.showinfo('Info','Livro não encontrado')
                self.tv.delete(*self.tv.get_children())
                self.txt_nome_livro.delete(0,END)
                self.Tela_Remove_Livro.focus()
                self.txt_nome_livro.focus_set()
                return
            else:
                cursor.execute("SELECT Livros.codigo, Livros.Nome, Autores.Nome, Livros.Preco FROM Livros, Autorias, Autores WHERE Livros.Codigo=Autorias.Codigo AND Autorias.Id=Autores.Id AND Livros.Nome LIKE '"+nome+"' ORDER BY Livros.Nome")
                linha = cursor.fetchone()
                if not linha:
                    messagebox.showinfo('Remover Livros','Não há livros cadastrados')
                    self.Tela_Remove_Livro.focus()
                    self.txt_nome_livro.focus_set()
                    return
                self.tv.delete(*self.tv.get_children())
                cursor.scroll(mode='first')
                linha = cursor.fetchone()
                #print('|',end=''),print(' LIVRO '.center(liv,'*') + '|' + ' AUTOR '.center(aut,'*') + '|' +' VALOR '.center(val,'*'),end=''), print('|')
                while linha:
                    #print('|', end=''), print (linha[0].center(liv,' ')+'|'+linha[1].center(aut,' ')+'|'+str(linha[2]).center(val,' '),end=''), print('|')
                    self.tv.insert('','end', values=linha)
                    linha = cursor.fetchone()
        except cx_Oracle.DataError as err:
            messagebox.showerror('Erro DB','DataBase error: '+str((err))+', ' +str(sys.exc_info()[0]))
            self.Tela_Cad_Autor.focus()
        except cx_Oracle.DatabaseError as err:
            error, = err.args
            messagebox.showerror('Erro DB','Oracle-Error-Code:'+str(error.code))
            messagebox.showerror('Erro DB','Oracle-Error-Message:'+str(error.message))
            self.Tela_Remove_Livro.focus()
            self.txt_nome_livro.focus_set()
            if error.code == 1400:
                messagebox.showerror('Erro DB','Você deve inserir um nome '+\
                    'para o Livro, não pode ser em branco. Local: ' \
                        +str(stack[0].function)+', '+ str(stack[1].function))
                self.Tela_Remove_Livro.focus()
                self.txt_nome_livro.focus_set()
                return
            elif error.code == 1:
                messagebox.showerror('Erro DB','Livro já cadastrado')
                self.txt_nome_livro.delete(first=0, last='end') 
                # outra sintax: (0, 'end') onde o 0 representa o primeiro
                #caracter
                self.Tela_Remove_Livro.focus()
                self.txt_nome_livro.focus_set()
                return
            elif error.code == 936:
                messagebox.showerror('Erro DB','Erro de Sintax, favor '+\
                    'verificar código' + str(stack[1].function))
                self.Tela_Remove_Livro.focus()
                self.txt_nome_livro.focus_set()
            elif error.code == 933:
                messagebox.showerror('Erro DB','Favor usar "." ao invés de'+\
                    ' "," nos valores numéricos decimais')
                self.Tela_Remove_Livro.focus()
                self.txt_nome_livro.focus_set()
            elif error.code == 904:
                messagebox.showerror('Erro DB','Campo não encontrado na'+\
                    ' tabela')
                self.Tela_Remove_Livro.focus()
                self.txt_nome_livro.focus_set()
        except KeyError:
            messagebox.showerror('Erro DB','Erro de Sintax, favor verificar código', stack[1].function)
            self.Tela_Remove_Livro.focus()
            self.txt_nome_livro.focus_set()
        except:
            raise
            messagebox.showerror('Erro DB','DataBase error: ' + str(sys.exc_info()[0]))
            self.Tela_Cad_Autor.focus()
        else:
            pass

    def remova_livro (self):
        #rem = 'N'
        try:
            selec = self.tv.selection()[0]
            valores = self.tv.item(selec, 'values')
            if (self.tv.selection() == '') or (self.tv.selection == None):
                print('Nada')
            else:
                print(valores)
                print('selecionado')
                print(valores[1]   )
            nome1 = valores[1]
            #cursor=conexao.cursor()
            cursor = self.BD.conexao.cursor()
            #nome = livro
            #cursor.scroll(mode='first')
            #linha = cursor.fetchone()
            rem = messagebox.askyesno('Remover Livro','Gostaria mesmo de remover o Livro?: ')
            if rem == YES:
                #cursor = conexao.cursor()
                cursor.execute("SELECT Codigo FROM Livros WHERE Nome='"+nome1+"'")
                linha = cursor.fetchone()
                CodigoLivro = linha[0]
                cursor.execute("SELECT Id FROM Autorias WHERE Codigo="+str(CodigoLivro))
                linha   = cursor.fetchone()
                idAutor = linha[0]
                cursor.execute("DELETE FROM Autorias WHERE Id="+str(idAutor)+" AND codigo="+str(CodigoLivro))
                cursor.execute("DELETE FROM Livros   WHERE Codigo=" + str(CodigoLivro))
                self.BD.conexao.commit ()
                #messagebox.showinfo('Info','Livro removido com sucesso')
                #return
            else:
                linha = ''
                return
        except cx_Oracle.DataError as err:
            messagebox.showerror('Erro DB','DataBase error: '+ str((err))+', ' +str(sys.exc_info()[0]))
            self.Tela_Remove_Livro.focus()
            self.txt_nome_livro.focus_set()
        except cx_Oracle.DatabaseError as err:
            error, = err.args
            messagebox.showerror('Erro DB','Oracle-Error-Code:'+ str(error.code))
            messagebox.showerror('Erro DB','Oracle-Error-Message:'+ str(error.message))
            #messagebox.showerror('Erro DB','DataBase error: {0}.
            # format('+str(err)+'))' + str(sys.exc_info()[0]))

            if error.code == 1400:
                messagebox.showerror('Erro DB','Você deve inserir um nome para o Livro, não pode ser em branco. Local: '+str(stack[0].function)+', '+ str(stack[1].function))
                self.Tela_Remove_Livro.focus()
                self.txt_nome_livro.focus_set()
                return
            elif error.code == 1:
                messagebox.showerror('Erro DB','Livro já cadastrado')
                self.txt_nome_livro.delete(first=0, last='end')
                self.Tela_Remove_Livro.focus()
                self.txt_nome_livro.focus_set()
                # outra sintax: (0, 'end') onde o 0 representa o primeiro
                #caracter
                return
            elif error.code == 936:
                messagebox.showerror('Erro DB','Erro de Sintax, favor '+\
                    'verificar código' + str(stack[1].function))
                self.Tela_Remove_Livro.focus()
                self.txt_nome_livro.focus_set()
            elif error.code == 933:
                messagebox.showerror('Erro DB','Favor usar "." ao invés de'+\
                    ' "," nos valores numéricos decimais')
                self.Tela_Remove_Livro.focus()
                self.txt_nome_livro.focus_set()
            elif error.code == 904:
                messagebox.showerror('Erro DB','Campo não encontrado na'+\
                    ' tabela')
                self.Tela_Remove_Livro.focus()
                self.txt_nome_livro.focus_set()
            self.Tela_Remove_Livro.focus()
            self.txt_nome_livro.focus_set()
        except KeyError:
            messagebox.showerror('Erro DB','Erro de Sintax, favor verificar código', stack[1].function)
            self.Tela_Remove_Livro.focus()
            self.txt_nome_livro.focus_set()
        except IndexError:
            messagebox.showerror(title='Erro', message='Favor selecionar o item para deleção.')
            self.Tela_Remove_Livro.focus()
            self.txt_nome_livro.focus_set()
            return
        except:
            messagebox.showerror('Erro DB','DataBase error: ' + str(sys.exc_info()[0]))
            self.Tela_Remove_Livro.focus()
            self.txt_nome_livro.focus_set()
        else:
            messagebox.showinfo('Info','Livro removido com sucesso')
            self.tv.delete(*self.tv.get_children())
            self.Tela_Remove_Livro.focus()
            self.txt_nome_livro.focus_set()

##############################################################################
class Listar_Livros:
    BD = Conecta_Bd()

    def __init__(self) -> None:
        #global Tela_Lista_Func, tv
        
        self.Tela_Lista_Livros = Toplevel()
        self.Tela_Lista_Livros.title('Listar Livros')
        #self.Tela_Lista_Func.geometry('450x280')
        centralizar_window(self.Tela_Lista_Livros)
        
        self.Frame_Livros = LabelFrame(self.Tela_Lista_Livros, text='Livros:')
        self.Frame_Livros.pack(fill='both', expand='yes', padx=10, pady=10)

        self.tv = ttk.Treeview(self.Frame_Livros, columns=('ID',\
            'Livro', 'Autor', 'Valor'), show='headings' )
        ### 'Setor', 'Salario_Bruto', 'Bonus', 'Meses', 'Dias','Dep'), show='headings')
        self.tv.column('ID', minwidth=0, width=30)
        self.tv.column('Livro', minwidth=0, width=250)
        self.tv.column('Autor', minwidth=0, width=150)
        self.tv.column('Valor', minwidth=0, width=70)
        #self.tv.column('Bonus', minwidth=0, width=50)
        #self.tv.column('Meses', minwidth=0, width=80)
        #self.tv.column('Dias', minwidth=0, width=60)
        #self.tv.column('Dep', minwidth=0, width=60)
        self.tv.heading('ID', text='ID')
        self.tv.heading('Livro', text='Nome Livro')
        self.tv.heading('Autor', text='Autor')
        self.tv.heading('Valor', text='Valor')
        #self.tv.heading('Bonus', text='Bonus')
        #self.tv.heading('Meses', text='M. Trabalhados')
        #self.tv.heading('Dias', text='Dias/Férias')
        #self.tv.heading('Dep', text='Dependentes')
        self.tv.pack( padx=10, pady=10)

        self.liste_livros()
    
    def liste_livros (self):
        BD = Conecta_Bd()
        try:
            cursor = BD.conexao.cursor()
            cursor.execute("SELECT Livros.codigo, Livros.Nome, Autores.Nome, Livros.Preco FROM Livros, Autorias, Autores WHERE Livros.Codigo=Autorias.Codigo AND Autorias.Id=Autores.Id ORDER BY Livros.Nome")
            linha = cursor.fetchone()
            if not linha:
                print ('Não há livros cadastrados')
                self.Tela_Lista_Livros.destroy()
            liv=0
            aut=0
            val=8
            self.tv.delete(*self.tv.get_children())
            '''while linha:
                #print(linha)
                #print (len(linha[0]))
                if len(linha[0]) > liv:
                    liv = len(linha[0])
                if len(linha[1]) > aut:
                    aut = len(linha[1])   
                linha = cursor.fetchone()
            #print(aut)
            liv = liv + 2
            aut = aut + 2'''
            cursor.scroll(mode='first')
            linha = cursor.fetchone()
            #print('|',end=''),print(' LIVRO '.center(liv,'*') + '|' + ' AUTOR '.center(aut,'*') + '|' +' VALOR '.center(val,'*'),end=''), print('|')
            while linha:
                #print(linha)
                #print('|', end=''), print (linha[0].center(liv,' ')+'|'+linha[1].center(aut,' ')+'|'+str(linha[2]).center(val,' '),end=''), print('|')
                self.tv.insert('','end', values=linha)
                linha = cursor.fetchone()
        except cx_Oracle.DataError as err:
            messagebox.showerror('Erro DB','DataBase error: '+\
                + str((err))+', ' +str(sys.exc_info()[0]))
            self.Tela_Lista_Livros.focus()
        except cx_Oracle.DatabaseError as err:
            error, = err.args
            messagebox.showerror('Erro DB','Oracle-Error-Code:'+\
                 str(error.code))
            messagebox.showerror('Erro DB','Oracle-Error-Message:'+\
                str(error.message))
            #messagebox.showerror('Erro DB','DataBase error: {0}.
            # format('+str(err)+'))' + str(sys.exc_info()[0]))
            if error.code == 1400:
                messagebox.showerror('Erro DB','Você deve inserir um nome '+\
                    'para o Autor, não pode ser em branco. Local: ' \
                        +str(stack[0].function)+', '+ str(stack[1].function))
                self.Tela_Lista_Livros.focus()
                return
            elif error.code == 1:
                messagebox.showerror('Erro DB','Autor já cadastrado')
                self.Tela_Lista_Livros.focus()
                return
            elif error.code == 936:
                messagebox.showerror('Erro DB','Erro de Sintax, favor '+\
                    'verificar código' + str(stack[1].function))
                self.Tela_Lista_Livros.focus()
            elif error.code == 933:
                messagebox.showerror('Erro DB','Favor usar "." ao invés de'+\
                    ' "," nos valores numéricos decimais')
                self.Tela_Lista_Livros.focus()
            elif error.code == 904:
                messagebox.showerror('Erro DB','Campo não encontrado na'+\
                    ' tabela')
                self.Tela_Lista_Livros.focus()
        except KeyError:
            messagebox.showerror('Erro DB','Erro de Sintax, favor verificar código', stack[1].function)
            self.Tela_Lista_Livros.focus()
        except:
            raise
            messagebox.showerror('Erro DB','DataBase error: ' + str(sys.exc_info()[0]))
            self.Tela_Lista_Livros.focus()
        else:
            pass
            self.Tela_Lista_Livros.focus()

##############################################################################
class Listar_Livros_Ate:
    BD = Conecta_Bd()
    
    def __init__(self) -> None:
        #global Tela_Lista_Func, tv
        self.Tela_Lista_Ate = Toplevel()
        self.Tela_Lista_Ate.title('Listar Livros até valor$')
        #self.Tela_Lista_Func.geometry('450x280')
        centralizar_window(self.Tela_Lista_Ate)
        self.Tela_Lista_Ate.focus()
        self.Frame_Livros = LabelFrame(self.Tela_Lista_Ate, text='Livros:')
        self.Frame_Livros.pack(fill='both', expand='yes', padx=10, pady=10)

        self.tv = ttk.Treeview(self.Frame_Livros, columns=('ID',\
            'Livro', 'Autor', 'Valor'), show='headings' )
        ### 'Setor', 'Salario_Bruto', 'Bonus', 'Meses', 'Dias','Dep'), show='headings')
        self.tv.column('ID', minwidth=0, width=30)
        self.tv.column('Livro', minwidth=0, width=250)
        self.tv.column('Autor', minwidth=0, width=150)
        self.tv.column('Valor', minwidth=0, width=70)
        #self.tv.column('Bonus', minwidth=0, width=50)
        #self.tv.column('Meses', minwidth=0, width=80)
        #self.tv.column('Dias', minwidth=0, width=60)
        #self.tv.column('Dep', minwidth=0, width=60)
        self.tv.heading('ID', text='ID')
        self.tv.heading('Livro', text='Nome Livro')
        self.tv.heading('Autor', text='Autor')
        self.tv.heading('Valor', text='Valor')
        #self.tv.heading('Bonus', text='Bonus')
        #self.tv.heading('Meses', text='M. Trabalhados')
        #self.tv.heading('Dias', text='Dias/Férias')
        #self.tv.heading('Dep', text='Dependentes')
        self.tv.pack( padx=10, pady=10)
        search_Frame = LabelFrame(self.Tela_Lista_Ate, text='Listar:')
        search_Frame.pack(fill='both', expand='yes', padx=10, pady=10)
        lbl_Valor = Label(search_Frame,text='Valor:')
        lbl_Valor.pack(side=LEFT, padx=5, pady=5)
        self.txt_valor_ate = Entry(search_Frame)
        self.txt_valor_ate.pack(side=LEFT, padx=5, pady=5)
        btn_Cancelar = Button(search_Frame, text='Cancelar', command=self.Tela_Lista_Ate.destroy)
        btn_Cancelar.pack(side=RIGHT, padx=5, pady=5)
        btn_Listar = Button(search_Frame, text='Listar', command=lambda: self.liste_livros_ate(self.txt_valor_ate.get()))
        btn_Listar.pack(side=RIGHT, padx=5, pady=5)
        self.valor = askstring('Livros', 'Você gostaria de listar livros à partir de que valor?: ')
        self.txt_valor_ate.focus_set()
        #print(self.valor)
        if self.valor == None:
            messagebox.showinfo('Erro','Você deve inserir um nome '+\
                    'para o Livro, não pode ser em branco.')
            self.Tela_Lista_Ate.destroy()
        else:
            self.liste_livros_ate(self.valor)
        

    def liste_livros_ate(self, valor): 
        try:
            cursor=self.BD.conexao.cursor()
            cursor.execute('SELECT Livros.codigo, Livros.Nome, Autores.Nome, Livros.Preco FROM Livros, Autores, Autorias WHERE Livros.Preco <= ' + valor + ' AND Livros.Codigo=Autorias.Codigo AND Autorias.Id=Autores.Id ORDER BY Livros.Preco ASC')
            linha = cursor.fetchone()
            if not linha:
                messagebox.showinfo('Livros', 'Não há Livros cadastrados')
                self.Tela_Lista_Ate.destroy()
                return
        except cx_Oracle.DataError as err:
            messagebox.showerror('Erro DB','DataBase error: '+str((err))+', ' +str(sys.exc_info()[0]))
            self.Tela_Lista_Ate.focus()
        except cx_Oracle.DatabaseError as err:
            error, = err.args
            messagebox.showerror('Erro DB','Oracle-Error-Code:'+str(error.code))
            messagebox.showerror('Erro DB','Oracle-Error-Message:'+str(error.message))
            if error.code == 1400:
                messagebox.showerror('Erro DB','Você deve inserir um nome '+\
                    'para o Livro, não pode ser em branco. Local: ' \
                        +str(stack[0].function)+', '+ str(stack[1].function))
                self.Tela_Lista_Ate.focus()
                return
            elif error.code == 1:
                messagebox.showerror('Erro DB','Livro já cadastrado')
                self.Tela_Lista_Ate.focus()
                return
            elif error.code == 936:
                messagebox.showerror('Erro DB','Erro de Sintax, favor '+\
                    'verificar código' + str(stack[0].function))
                self.Tela_Lista_Ate.destroy()
            elif error.code == 933:
                messagebox.showerror('Erro DB','Favor usar "." ao invés de'+\
                    ' "," nos valores numéricos decimais')
                self.Tela_Lista_Ate.focus()
                self.Tela_Lista_Ate.destroy()
            elif error.code == 904:
                messagebox.showerror('Erro DB','Campo não encontrado na'+\
                    ' tabela')
                self.Tela_Lista_Ate.focus()
        except KeyError:
            messagebox.showerror('Erro DB','Erro de Sintax, favor verificar código', stack[1].function)
            self.Tela_Lista_Ate.focus()
        except:
            raise
            messagebox.showerror('Erro DB','DataBase error: ' + str(sys.exc_info()[0]))
            self.Tela_Lista_Ate.focus()
        else:
            liv = 0
            aut=0
            val=8
            self.tv.delete(*self.tv.get_children())
            '''while linha:
                #print(linha)
                #print (len(linha[0]))
                if len(linha[0]) > liv:
                    liv = len(linha[0])
                if len(linha[1]) > aut:
                    aut = len(linha[1])   
                linha = cursor.fetchone()
            #print(aut)
            #liv = liv + 2
            #aut = aut + 2'''
            cursor.scroll(mode='first')
            linha = cursor.fetchone()
            #print('|',end=''),print(' LIVRO '.center(liv,'*') + '|' + ' AUTOR '.center(aut,'*') + '|' +' VALOR '.center(val,'*'),end=''), print('|')
            while linha:
                #print('|', end=''), print (linha[0].center(liv,' ')+'|'+linha[1].center(aut,' ')+'|'+str(linha[2]).center(val,' '),end=''), print('|')
                self.tv.insert('','end', values=linha)
                linha = cursor.fetchone()
            self.txt_valor_ate.delete(first=0, last='end')
            self.txt_valor_ate.focus_set()

##############################################################################
class Listar_Livros_Entre:
    BD = Conecta_Bd()
    
    def __init__(self) -> None:
        #global Tela_Lista_Func, tv
        self.Tela_Lista_Entre = Toplevel()
        self.Tela_Lista_Entre.title('Listar Livros de $ até $')
        #self.Tela_Lista_Func.geometry('450x280')
        centralizar_window(self.Tela_Lista_Entre)
        self.Tela_Lista_Entre.focus()
        self.Frame_Livros = LabelFrame(self.Tela_Lista_Entre, text='Livros:')
        self.Frame_Livros.pack(fill='both', expand='yes', padx=10, pady=10)

        self.tv = ttk.Treeview(self.Frame_Livros, columns=('ID',\
            'Livro', 'Autor', 'Valor'), show='headings' )
        ### 'Setor', 'Salario_Bruto', 'Bonus', 'Meses', 'Dias','Dep'), show='headings')
        self.tv.column('ID', minwidth=0, width=30)
        self.tv.column('Livro', minwidth=0, width=250)
        self.tv.column('Autor', minwidth=0, width=150)
        self.tv.column('Valor', minwidth=0, width=70)
        #self.tv.column('Bonus', minwidth=0, width=50)
        #self.tv.column('Meses', minwidth=0, width=80)
        #self.tv.column('Dias', minwidth=0, width=60)
        #self.tv.column('Dep', minwidth=0, width=60)
        self.tv.heading('ID', text='ID')
        self.tv.heading('Livro', text='Nome Livro')
        self.tv.heading('Autor', text='Autor')
        self.tv.heading('Valor', text='Valor')
        #self.tv.heading('Bonus', text='Bonus')
        #self.tv.heading('Meses', text='M. Trabalhados')
        #self.tv.heading('Dias', text='Dias/Férias')
        #self.tv.heading('Dep', text='Dependentes')
        self.tv.pack(fill='both', expand='yes', padx=10, pady=10)
        search_Frame = LabelFrame(self.Tela_Lista_Entre, text='Listar:')
        search_Frame.pack(fill='both', expand='yes', padx=10, pady=10)
        lbl_Valor1 = Label(search_Frame,text='De:')
        lbl_Valor1.pack(side=LEFT, padx=5, pady=5)
        self.txt_valor_apartir = Entry(search_Frame)
        self.txt_valor_apartir.pack(side=LEFT, padx=5, pady=5)
        lbl_Valor2 = Label(search_Frame,text='Até:')
        lbl_Valor2.pack(side=LEFT, padx=5, pady=5)
        self.txt_valor_ate = Entry(search_Frame)
        self.txt_valor_ate.pack(side=LEFT)
        btn_Cancelar = Button(search_Frame, text='Cancelar', command=self.Tela_Lista_Entre.destroy)
        btn_Cancelar.pack(side=RIGHT, padx=5, pady=5)
        btn_Listar = Button(search_Frame, text='Listar', command=lambda: self.liste_livros_entre(self.txt_valor_apartir.get(), self.txt_valor_ate.get()))
        btn_Listar.pack(side=RIGHT, padx=5, pady=5)
        self.valor1 = askstring('Livros', 'Você gostaria de listar livros à partir de que valor?: ')
        self.valor2 = askstring('Livros', 'até qual valor?: ')
        self.txt_valor_apartir.focus_set()
        if (self.valor1) == None or (self.valor2) == None:
            messagebox.showinfo('Erro','Você deve inserir uma faixa de '+\
                'valor para o Livro, não pode ser em branco.')
            self.Tela_Lista_Entre.destroy()
        else:
            self.liste_livros_entre(self.valor1, self.valor2)

        

    def liste_livros_entre(self, valor1, valor2): 
        try:
            cursor=self.BD.conexao.cursor()
            cursor.execute('SELECT Livros.codigo, Livros.Nome, Autores.Nome, Livros.Preco FROM Livros, Autores, Autorias WHERE Livros.Preco >= ' + valor1 + ' AND Livros.Preco <= ' +valor2+ ' AND Livros.Codigo=Autorias.Codigo AND Autorias.Id=Autores.Id ORDER BY Livros.Preco ASC')
            linha = cursor.fetchone()
            if not linha:
                messagebox.showinfo('Livros', 'Não há Livros cadastrados'+\
                    ' nesta faixa de valor.')
                self.txt_valor_apartir.delete(first=0, last='end')
                self.txt_valor_ate.delete(first=0, last='end')
                self.tv.delete(*self.tv.get_children())
                self.Tela_Lista_Entre.focus()
                self.txt_valor_apartir.focus_set()
                return
        except cx_Oracle.DataError as err:
            messagebox.showerror('Erro DB','DataBase error: '+\
                + str((err))+', ' +str(sys.exc_info()[0]))
            self.Tela_Lista_Entre.focus()
        except cx_Oracle.DatabaseError as err:
            error, = err.args
            #messagebox.showerror('Erro DB','Oracle-Error-Code:'+\
            #     str(error.code))
            #messagebox.showerror('Erro DB','Oracle-Error-Message:'+\
            #    str(error.message))
            #messagebox.showerror('Erro DB','DataBase error: {0}.
            # format('+str(err)+'))' + str(sys.exc_info()[0]))
            if error.code == 1400:
                messagebox.showerror('Erro DB','Você deve inserir um nome '+\
                    'para o Livro, não pode ser em branco. Local: ' \
                        +str(stack[0].function)+', '+ str(stack[1].function))
                self.Tela_Lista_Entre.focus()
                return
            elif error.code == 1:
                messagebox.showerror('Erro DB','Livro já cadastrado')
                self.Tela_Lista_Entre.destroy()
                return
            elif error.code == 936:
                messagebox.showerror('Erro DB','Erro de Sintax, favor '+\
                    'verificar código' + str(stack[0].function))
                self.Tela_Lista_Entre.destroy()
            elif error.code == 933:
                messagebox.showerror('Erro DB','Favor usar "." ao invés de'+\
                    ' "," nos valores numéricos decimais')
                self.Tela_Lista_Entre.destroy()
            elif error.code == 904:
                messagebox.showerror('Erro DB','Campo não encontrado na'+\
                    ' tabela')
                self.Tela_Lista_Entre.destroy()
            elif error.code == 920:
                raise
                messagebox.showerror('Erro DB','Erro de Sintax, favor '+\
                    'verificar código' + str(stack[0].function))
                self.Tela_Lista_Entre.destroy()
        except KeyError:
            messagebox.showerror('Erro DB','Erro de Sintax, favor verificar código', stack[1].function)
            self.Tela_Lista_Entre.destroy()
        except:
            raise
            messagebox.showerror('Erro DB','DataBase error: ' + str(sys.exc_info()[0]))
            self.Tela_Lista_Ate.focus()
        else:
            liv = 0
            aut=0
            val=8
            self.tv.delete(*self.tv.get_children())
            '''while linha:
                #print(linha)
                #print (len(linha[0]))
                if len(linha[0]) > liv:
                    liv = len(linha[0])
                if len(linha[1]) > aut:
                    aut = len(linha[1])   
                linha = cursor.fetchone()
            #print(aut)
            #liv = liv + 2
            #aut = aut + 2'''
            cursor.scroll(mode='first')
            linha = cursor.fetchone()
            #print('|',end=''),print(' LIVRO '.center(liv,'*') + '|' + ' AUTOR '.center(aut,'*') + '|' +' VALOR '.center(val,'*'),end=''), print('|')
            while linha:
                #print('|', end=''), print (linha[0].center(liv,' ')+'|'+linha[1].center(aut,' ')+'|'+str(linha[2]).center(val,' '),end=''), print('|')
                self.tv.insert('','end', values=linha)
                linha = cursor.fetchone()
            self.txt_valor_apartir.delete(first=0, last='end')
            self.txt_valor_ate.delete(first=0, last='end')
            self.Tela_Lista_Entre.focus()
            self.txt_valor_apartir.focus_set()

##############################################################################
class Listar_Livros_Apartir:

    BD = Conecta_Bd()
    
    def __init__(self) -> None:
        #global Tela_Lista_Func, tv
        self.Tela_Lista_Apartir = Toplevel()
        self.Tela_Lista_Apartir.title('Listar Livros a partir do valor$')
        #self.Tela_Lista_Func.geometry('450x280')
        centralizar_window(self.Tela_Lista_Apartir)
        self.Tela_Lista_Apartir.focus()
        self.Frame_Livros = LabelFrame(self.Tela_Lista_Apartir, text='Livros:')
        self.Frame_Livros.pack(fill='both', expand='yes', padx=10, pady=10)

        self.tv = ttk.Treeview(self.Frame_Livros, columns=('ID',\
            'Livro', 'Autor', 'Valor'), show='headings' )
        ### 'Setor', 'Salario_Bruto', 'Bonus', 'Meses', 'Dias','Dep'), show='headings')
        self.tv.column('ID', minwidth=0, width=30)
        self.tv.column('Livro', minwidth=0, width=250)
        self.tv.column('Autor', minwidth=0, width=150)
        self.tv.column('Valor', minwidth=0, width=70)
        #self.tv.column('Bonus', minwidth=0, width=50)
        #self.tv.column('Meses', minwidth=0, width=80)
        #self.tv.column('Dias', minwidth=0, width=60)
        #self.tv.column('Dep', minwidth=0, width=60)
        self.tv.heading('ID', text='ID')
        self.tv.heading('Livro', text='Nome Livro')
        self.tv.heading('Autor', text='Autor')
        self.tv.heading('Valor', text='Valor')
        #self.tv.heading('Bonus', text='Bonus')
        #self.tv.heading('Meses', text='M. Trabalhados')
        #self.tv.heading('Dias', text='Dias/Férias')
        #self.tv.heading('Dep', text='Dependentes')
        self.tv.pack(fill='both', expand='yes', padx=10, pady=10)
        search_Frame = LabelFrame(self.Tela_Lista_Apartir, text='Listar:')
        search_Frame.pack(fill='both', expand='yes', padx=10, pady=10)
        lbl_Valor = Label(search_Frame,text='Valor:')
        lbl_Valor.pack(side=LEFT, padx=5, pady=5)
        self.txt_valor_apartir = Entry(search_Frame)
        self.txt_valor_apartir.pack(side=LEFT, padx=5, pady=5)
        btn_Cancelar = Button(search_Frame, text='Cancelar', command=self.Tela_Lista_Apartir.destroy)
        btn_Cancelar.pack(side=RIGHT, padx=5, pady=5)
        btn_Listar = Button(search_Frame, text='Listar', command=lambda: self.liste_livros_apartir(self.txt_valor_apartir.get()))
        btn_Listar.pack(side=RIGHT, padx=5, pady=5)
        self.valor = askstring('Livros', 'Você gostaria de listar livros à partir de que valor?: ')
        self.txt_valor_apartir.focus_set()
        #print(self.valor)
        if self.valor == None:
            messagebox.showinfo('Erro','Você deve inserir um valor, não pode ser em branco.')
            self.txt_valor_apartir.delete(first=0, last='end')
            self.Tela_Lista_Apartir.focus()
            self.txt_valor_apartir.focus_set()

        else:
            self.liste_livros_apartir(self.valor)
        
    def liste_livros_apartir(self, valor): 
        try:
            cursor=self.BD.conexao.cursor()
            cursor.execute('SELECT Livros.codigo, Livros.Nome, Autores.Nome, Livros.Preco FROM Livros, Autores, Autorias WHERE Livros.Preco >= ' + valor + ' AND Livros.Codigo=Autorias.Codigo AND Autorias.Id=Autores.Id ORDER BY Livros.Preco ASC')
            linha = cursor.fetchone()
            if not linha:
                messagebox.showinfo('Livros', 'Não há Livros cadastrados')
                self.Tela_Lista_Apartir.destroy()
                return
        except cx_Oracle.DataError as err:
            messagebox.showerror('Erro DB','DataBase error: '+\
                + str((err))+', ' +str(sys.exc_info()[0]))
            self.Tela_Lista_Apartir.focus()
        except cx_Oracle.DatabaseError as err:
            error, = err.args
            messagebox.showerror('Erro DB','Oracle-Error-Code:'+\
                 str(error.code))
            messagebox.showerror('Erro DB','Oracle-Error-Message:'+\
                str(error.message))
            #messagebox.showerror('Erro DB','DataBase error: {0}.
            # format('+str(err)+'))' + str(sys.exc_info()[0]))
            if error.code == 1400:
                messagebox.showerror('Erro DB','Você deve inserir um nome '+\
                    'para o Livro, não pode ser em branco. Local: ' \
                        +str(stack[0].function)+', '+ str(stack[1].function))
                self.Tela_Lista_Ate.focus()
                return
            elif error.code == 1:
                messagebox.showerror('Erro DB','Livro já cadastrado')
                self.Tela_Lista_Ate.focus()
                return
            elif error.code == 936:
                messagebox.showerror('Erro DB','Erro de Sintax, ou campo'+\
                 'em branco favor verificar código' + str(stack[0].function))
                self.txt_valor_apartir.delete(first=0, last='end')
                self.Tela_Lista_Apartir.focus()
                self.txt_valor_apartir.focus_set()

            elif error.code == 933:
                messagebox.showerror('Erro DB','Favor usar "." ao invés de'+\
                    ' "," nos valores numéricos decimais')
                self.Tela_Lista_Ate.focus()
                self.Tela_Lista_Ate.destroy()
            elif error.code == 904:
                messagebox.showerror('Erro DB','Campo não encontrado na'+\
                    ' tabela')
                self.Tela_Lista_Ate.focus()
        except KeyError:
            messagebox.showerror('Erro DB','Erro de Sintax, favor verificar código'+str(stack[1].function))
            self.Tela_Lista_Ate.focus()
        except:
            raise
            messagebox.showerror('Erro DB','DataBase error: ' + str(sys.exc_info()[0]))
            self.Tela_Lista_Ate.focus()
        else:
            liv = 0
            aut=0
            val=8
            self.tv.delete(*self.tv.get_children())
            
            cursor.scroll(mode='first')
            linha = cursor.fetchone()
            #print('|',end=''),print(' LIVRO '.center(liv,'*') + '|' + ' AUTOR '.center(aut,'*') + '|' +' VALOR '.center(val,'*'),end=''), print('|')
            while linha:
                #print('|', end=''), print (linha[0].center(liv,' ')+'|'+linha[1].center(aut,' ')+'|'+str(linha[2]).center(val,' '),end=''), print('|')
                self.tv.insert('','end', values=linha)
                linha = cursor.fetchone()
              
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
        self.Tela_Prin.iconphoto(True, tk.PhotoImage(file=ICO))
        #self.Tela_Prin.iconbitmap(True, ico)
        self.Tela_Prin.title('Livraria - PROGRAMA PARA PARA CADASTRAR LIVROS E SEUS AUTORES')
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
        Menu_Rem.add_command(label='Autor', command=Remov_Autor)
        Menu_Rem.add_command(label='Livro', command=Remov_Livro) 
        #Menu_Cad.add_separator()  
        #Menu_Cad.add_command(label="Sair", command=_quit)  
        MenuBar.add_cascade(label='Remover', menu=Menu_Rem)

        #====================================================================
        #Menu Listagem 
        Menu_Lis= Menu(MenuBar, tearoff=0)  
        Menu_Lis.add_command(label='Autores', command=Listar_Aut)
        MenuBar.add_cascade(label="Listagem", menu=Menu_Lis)
        Menu_Lis1 = Menu(Menu_Lis, tearoff=0)
        Menu_Lis1.add_command(label='Listar Todos os Livros', command=Listar_Livros)
        Menu_Lis1.add_command(label='LISTAR - Livros até valor', command=Listar_Livros_Ate)
        Menu_Lis1.add_command(label='LISTAR - Livros entre valores', command=Listar_Livros_Entre)
        Menu_Lis1.add_command(label='LISTAR - Livros acima valor', command=Listar_Livros_Apartir)
        Menu_Lis.add_cascade(label='Livros', menu=Menu_Lis1)
        #=====================================================================
        #Menu Sair
        Menu_Sair= Menu(MenuBar, tearoff=0)  
        #Menu_Cad.add_command(label='Autor')
        #Menu_Cad.add_command(label='Livro') 
        #Menu_Cad.add_separator()  
        Menu_Sair.add_command(label="Sair", command=self._quit)  
        MenuBar.add_cascade(label='Sair', menu=Menu_Sair)
        #=====================================================================

        meio_frame = Frame(self.Tela_Prin)
        meio_frame.pack(fill='both', expand='yes', padx=10, pady=10)
        #load = Image.open(IMG)
        test = ImageTk.PhotoImage(Image.open(IMG))
        imagem = Label(meio_frame, image=test)
        imagem.image = test
        imagem.pack(fill=BOTH)
        #=====================================================================

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

##############################################################################
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