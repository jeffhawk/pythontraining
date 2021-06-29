#==========================
'''PROJETO FINAL - SISTEMA DE RH - "Gute Arbeit Sistema de RH"
Software/Programa desenvolvido aplicando os conhecimentos obtidos em sala de aula para obtenção de nota final na PONTIFÍCIA UNIVERSIDADE CATÓLICA DE CAMPINAS - PUC-CAMPINAS,
no CENTRO DE CIÊNCIAS EXATAS, AMBIENTAIS E DE TECNOLOGIA para o curso de SISTEMAS DE INFORMAÇÃO.

JEFFERSON EDUARDO LUIZ
RA 19568823

Foi empregado todo o conhecimento obtido em sala de aula e acrescentado algumas funcionalidades aprendida de forma autônoma ao curso.

'''
#==========================
#Importando Bibliotecas internas do Python
from tkinter import *
import tkinter
from tkinter import font, messagebox, Entry, ttk
from tkinter.font import BOLD, Font
from tkinter.simpledialog import askstring
import sys
import os, ctypes, sys
from os import system
import inspect
from functools import partial
import string
import subprocess
import time
import inspect

from win32api import MessageBox, MessageBoxEx

#Declaração de variáveis globais
global biblio
global caminho
global tentativa

biblios = ['pip','cx_Oracle','setuptools','pywin32']
atua = ''
i=0
biblio = False #variável de controle para saber se está tudo ok e seguir com a execução
#caminho = 'InstantClient'
fonte_Normal = ("Verdana", "8",'bold')
fonte_Titulo = ('Arial', 16, 'bold')
fonte_Texto = ('Times New Roman', 12)
caminho = 'InstantClient'
tentativa = 0

#Inicia as importações

while not biblio: #Aqui decidi deixar tudo em um laço(While) pois na verificação tem a opção da instalação das Bibliotecas
    try:
        # Importando as bibliotecas
        # Verifica se existe as bibliotecas, caso contrário pergunta se quer instala-las
        import cx_Oracle
        import win32api
        from win32api import GetSystemMetrics
        import setuptools
        import pip
        os.chdir(caminho) #Aqui estou usando a funcionalidade da biblioteca 'os' para setar o caminho do instantclient
        biblio = True
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
                break                
            except ImportError as errorimp:
                messagebox.showerror('Erro Bibliotecas','Error: '+ str(errorimp))
                break
            except OSError as oserror:
                messagebox.showerror('Erro OS', 'OS error: ' + str(oserror))
                if not os.path.exists(caminho):
                    #messagebox.showinfo(biblio)
                    messagebox.showerror('OS Erro','Diretório não encontrado ou não existe',)
                    caminho = askstring('OS Error:', 'Entre com o caminho do Instant Client: ')
                    #os.chdir(caminho)
                    import win32api
                    from win32api import GetSystemMetrics
                    import setuptools
                    import cx_Oracle
                    import inspect
                    biblio=True
                    break
                else:
                    import win32api
                    from win32api import GetSystemMetrics
                    import setuptools
                    import cx_Oracle
                    import inspect
                    #os.chdir('C:\\Courses\\instantclient-basic-windows.x64-19.6.0.0.0dbru\\instantclient_19_6')
            except:
                messagebox.showerror('Erro','Unexpected error:', sys.exc_info()[0])
                raise
        else:
            messagebox.showerror('Erro', 'Bibliotecas não  instaladas!')
            biblio = False
            break
    except OSError as err:
        messagebox.showerror('Erro OS', 'OS error: ' + str(err))
        if not os.path.exists(caminho):
            messagebox.showerror('OS Erro','Diretório não encontrado ou não existe',)
            caminho = askstring('OS Error:', 'Entre com o caminho do Instant Client: ')
            os.chdir(caminho)
            #programa()
            biblio=True
            break
        #else:
        #    os.chdir('C:\Courses\instantclient-basic-windows.x64-19.6.0.0.0dbru\instantclient_19_6')  
    except:
        messagebox.showerror('Error', 'Unexpected error:', sys.exc_info()[0])
        raise
    else:
        # Cláusula 'else' do 'try/except',  só é executada se
        # não ocorreu nenhum erro
        import win32api
        from win32api import GetSystemMetrics
        import setuptools
        import cx_Oracle
        import inspect
        biblio=True
        break  # Este comando encerra o 'while True'
if biblio == FALSE:
    system('python gasrh.py')

def connection():
    global conexao
    servidor = 'localhost/xe'
    usuario  = 'system'
    senha    = 'oracle'
    #os.chdir(caminho)
    try:
        conexao = cx_Oracle.connect(dsn=servidor,user=usuario,password=senha)
        cursor  = conexao.cursor()
    except cx_Oracle.DataError as err:
                messagebox.showerror('Erro','DataBase error: ' + str(err))
    except cx_Oracle.DatabaseError as err:
        error, = err.args
        messagebox.showerror('DB Erro','Oracle-Error-Code: '+ str(error.code))
        messagebox.showerror('DB Erro','Oracle-Error-Message:' + str(error.message))
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
    except cx_Oracle.DatabaseError:
        messagebox.showerror('DB Error', 'Erro de conexão com o BD')
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
        cursor.execute('CREATE SEQUENCE seqUsers START WITH 1 INCREMENT BY 1 MINVALUE 1 MAXVALUE 999 NOCACHE CYCLE')
        conexao.commit()
    except cx_Oracle.DataError as err:
            messagebox.showerror('Erro','DataBase error: ' + str(err))
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


    try:
        cursor.execute("CREATE TABLE logins (Id NUMBER(3) PRIMARY KEY, users NVARCHAR2(12) UNIQUE NOT NULL, pass NVARCHAR2(8) NOT NULL)")
        conexao.commit()
    except cx_Oracle.DataError as err:
                messagebox.showerror('Erro','DataBase error: ' + str(err))
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

    try:
        cursor.execute("CREATE SEQUENCE seqFunc START WITH 1 INCREMENT BY 1 MAXVALUE 999 NOCACHE CYCLE")
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a tabela já existe

    try:
        cursor.execute("CREATE SEQUENCE seqInss START WITH 1 INCREMENT BY 1 MAXVALUE 999 NOCACHE CYCLE")
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a tabela já existe

    try:
        cursor.execute('CREATE TABLE inss (Id_Inss NUMBER(5) PRIMARY KEY, Sal_Cont NVARCHAR2(50) UNIQUE NOT NULL, Aliquota NUMBER(5,2), Parc_Dedu NUMBER(6,2) )')
        conexao.commit()
    except cx_Oracle.DatabaseError as err:
        error, = err.args
        #print('Oracle-Error-Code:', error.code)
        #print('Oracle-Error-Message:', error.message)
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
            pass # ignora, pois a tabela já existe

    try:
        cursor.execute("CREATE SEQUENCE seqIrrf START WITH 1 INCREMENT BY 1 MAXVALUE 999 NOCACHE CYCLE")
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a tabela já existe

    try:
        cursor.execute('CREATE TABLE irrf (Id_Irrf NUMBER(5) PRIMARY KEY, Sal_Cont NVARCHAR2(50) UNIQUE NOT NULL, Aliquota NUMBER(5,2), Parc_Dedu NUMBER(6,2) )')
        conexao.commit()
    except cx_Oracle.DatabaseError as err:
        error, = err.args
        #print('Oracle-Error-Code:', error.code)
        #print('Oracle-Error-Message:', error.message)
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
            pass # ignora, pois a tabela já existe

    '''try:
        cursor.execute('CREATE TABLE Setor (Id_Setor NUMBER(5) PRIMARY KEY, Nome_Setor NVARCHAR2(50) UNIQUE NOT NULL)')
        conexao.commit()
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
            pass # ignora, pois a tabela já existe'''

    try:
        cursor.execute("CREATE TABLE Funcionarios (Id_Func NUMBER(5) PRIMARY KEY, Nome_Func NVARCHAR2(50) UNIQUE NOT NULL, Nome_Setor NVARCHAR2(50) NOT NULL, Salario_Bruto NUMBER(6,2) NOT NULL, Bonus NUMBER(6,2), Meses_Trab NUMBER(3), Dias_Ferias NUMBER(3), Dep NUMBER(2))")
        conexao.commit()
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

def logar(user, password):
    try:
        global tentativa
        user1 = user.get()
        pass1 = password.get()
        cursor = conexao.cursor()
        entra = 0
        
        if not user1:
            messagebox.showinfo('Alerta','Você deve inserir um nome para Logar, não pode ser em branco!')
            tentativa += 1
            return
        cursor.execute("SELECT * FROM logins WHERE logins.users='"+user1+"' AND logins.pass='"+pass1+"'")
        conexao.commit ()
        linha = cursor.fetchone()
        if not linha:
            messagebox.showinfo('Informação','Usuário ou senha incorreta, tente outra vez')
            entra = 0
            tentativa += 1
        else:
            #messagebox.showinfo('Logando...','Entrando')
            entra = 1
        if tentativa > 3 :
            cad = messagebox.askyesno('Teste', 'Gostaria de cadastrar um usuário de acesso?')
            if cad == YES:
                #Login_Tela.destroy()
                CadUser()

    except cx_Oracle.DataError as err:
        messagebox.showerror('DB Error: ' + str(err),'DataBase error: {0}'.format(err), sys.exc_info()[0])
    except cx_Oracle.DatabaseError as err:
        error, = err.args
        #messagebox.showerror('DB Error: ' + str(error.code), 'Oracle-Error-Code: '+ str(error.code))
        #messagebox.showerror('DB Error: ' + str(error.code),'Oracle-Error-Message:' + str(error.message))
        if error.code == 1400:
            messagebox.showerror(error.code,'Você deve inserir um nome para o Autor, não pode ser em branco')
            return
        elif error.code == 1:
            messagebox.showerror(error.code,'Autor repetido')
            return
        elif error.code == 936:
            stack = inspect.stack()
            messagebox.showerror(error.code,'Erro de Sintax, favor verificar código' + stack[1].function)
        elif error.code == 933:
            messagebox.showerror(error.code,'Favor usar "." ao invés de "," nos valores numéricos decimais')
        elif error.code == 2292:
            messagebox.showerror(error.code,'O autor tem livros cadastrados, favor remover os livros primeiro!')
        elif error.code == 904:
            messagebox.showerror(error.code,'Campo não encontrado na tabela')
        elif error.code == 955:
            pass
    if entra == 1:
        Login_Tela.destroy()
        programa()

def CadUser ():
        global Tela_Cad_User, txt_Nome_User, txt_Senha_User
        Tela_Cad_User = Tk()
        Tela_Cad_User.title('Cadastro de Usuários')
        centralizar_window(Tela_Cad_User)
        Tela_Cad_User.config()
        Tela_Cad_User.geometry('250x100')

        Frame_Titulo_User = Frame(Tela_Cad_User)
        Frame_Titulo_User.pack(side=TOP)
        lblCadser = Label(Frame_Titulo_User, text='Cadastro de Usuários', font=fonte_Titulo, fg='blue')
        lblCadser.pack(side=TOP)
        Frame_Dados_User = Frame(Tela_Cad_User)
        Frame_Dados_User.pack()
        lbl_Nome_User = Label(Frame_Dados_User, text='Usuário: ', font=fonte_Normal)
        lbl_Nome_User.grid(row=0)
        txt_Nome_User = Entry(Frame_Dados_User, font=fonte_Normal)
        txt_Nome_User.grid(row=0, column=1)
        lbl_Pass_User = Label(Frame_Dados_User, text='Senha: ', font=fonte_Normal)
        lbl_Pass_User.grid(row=1)
        txt_Senha_User = Entry(Frame_Dados_User, font=fonte_Normal, show='*')
        txt_Senha_User.grid(row=1, column=1)
        txt_Nome_User.focus()
    

        Frame_Btn_Cad_user = Frame(Tela_Cad_User)
        Frame_Btn_Cad_user.pack(side=BOTTOM)
        btn_Cad_User = Button(Frame_Btn_Cad_user, text='Cadastrar', command=lambda:Cadastrar_User(txt_Nome_User.get(), txt_Senha_User.get()), fg='blue', font=fonte_Normal)
        #btn_Entrar.bind('<Button-1>', logar)
        btn_Cad_User.pack(side=LEFT)
        btn_Sair_Cad = Button(Frame_Btn_Cad_user, text='Cancelar', fg='blue', command=Tela_Cad_User.destroy, font=fonte_Normal)
        btn_Sair_Cad.pack(side=RIGHT)

def Cadastrar_User(nome, senha):
    try:
        connection()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO Logins (Id,users,pass) VALUES (seqUsers.nextval,'"+nome+"','"+senha+"')")
        conexao.commit()
    except cx_Oracle.DataError as err:
        messagebox.showerror('DB Error: ' + str(err),'DataBase error1: ' + err)
    except cx_Oracle.DatabaseError as err:
        error, = err.args
        #messagebox.showerror('DB Error: ' + str(error.code), 'Oracle-Error-Code: '+ str(error.code))
        #messagebox.showerror('DB Error: ' + str(error.code),'Oracle-Error-Message:' + str(error.message))
        if error.code == 1400:
            messagebox.showerror(error.code,'Nome e senha não pode ser em branco')
            Tela_Cad_User.lift()
            txt_Nome_User.focus()
            return
        elif error.code == 1:
            messagebox.showerror(error.code,'Autor repetido')
            return
        elif error.code == 936:
            stack = inspect.stack()
            messagebox.showerror(error.code,'Erro de Sintax, favor verificar código' + stack[1].function)
        elif error.code == 933:
            messagebox.showerror(error.code,'Favor usar "." ao invés de "," nos valores numéricos decimais')
        elif error.code == 2292:
            messagebox.showerror(error.code,'O autor tem livros cadastrados, favor remover os livros primeiro!')
        elif error.code == 904:
            messagebox.showerror(error.code,'Campo não encontrado na tabela')
        elif error.code == 955:
            pass
    except KeyError:
        messagebox.showerror('Erro','Erro de Sintax, favor verificar código')
    #except:
        #messagebox.showerror('Erro','DataBase error: ')
    else:
        messagebox.showinfo('Cadastro','User cadastrado com sucesso')
        op = messagebox.askyesno('Cadastro', 'Deseja cadastrar outro usuário?')
        Tela_Cad_User.lift()
        if op == YES:
            txt_Nome_User.delete(0, END)
            txt_Senha_User.delete(0, END)
            return
        elif op == NO:
            Tela_Cad_User.destroy()
            txt_Id_Usuario.delete(0,END)
            txt_Pass.delete(0,END)
            txt_Id_Usuario.focus()
            pass

def ListaUser():
    global Tela_Lista_User, tv
    Tela_Lista_User = Tk()
    Tela_Lista_User.title('Listar Usuários')
    #centralizar_window(Tela_Lista_Func)
    
    Frame_user = LabelFrame(Tela_Lista_User, text='Usuários:')
    Frame_user.pack(fill='both', expand='yes', padx=10, pady=10)

    tv = ttk.Treeview(Frame_user, columns=('ID', 'Nome'), show='headings')
    tv.column('ID', minwidth=0, width=30)
    tv.column('Nome', minwidth=0, width=250)
    tv.heading('ID', text='ID')
    tv.heading('Nome', text='Nome')
    tv.pack()
    listarUser()

def listarUser():
    try:
        connection()
        cursor=conexao.cursor()
        cursor.execute("SELECT * FROM logins ORDER BY Id")   
        linha = cursor.fetchone() # linha(1,'Arthur')
        if not linha:
            messagebox.showwarning ('Alerta','Não há Usuários cadastrados')
            return
        aut=0
        tv.delete(*tv.get_children())
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
            tv.insert('','end', values=linha)
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

def Fechar_Tela_Cad():
    if tentativa > 3:
        Tela_Cad_User.destroy()
        Tela_Login()
    else:
        Tela_Cad_User.destroy()

def BuscarFun (funcio):
    try:
        global valores
        connection()
        cursor=conexao.cursor()
        cursor.execute("SELECT * FROM funcionarios WHERE Nome_Func='"+funcio+"' ORDER BY Nome_Func")   
        linha = cursor.fetchone() # linha(1,'Arthur')
        if not linha:
            messagebox.showwarning ('Alerta','Não há Usuários cadastrados')
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
        #print('|',end=''),print(' AUTOR '.center(aut,'*'),end=''), print('|')
        while linha:
            #print('|', end=''), print (linha[1].center(aut,' '),end=''), print('|')
            tv.insert('','end', values=linha)
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

def removerUser (conexao):
    try:
        cursor = conexao.cursor()
        user   = input('\nNome do autor? ')
        if not user:
            print('Você deve inserir um nome para o Autor, não pode ser em branco')
            return
        cursor.execute("SELECT Id FROM Autores WHERE Nome='"+user+"'")
        conexao.commit ()
        linha = cursor.fetchone()
        if not linha:
            print('Autor inexistente')
        else:
            cursor.execute("DELETE FROM Autores WHERE Nome='"+user+"'")
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

def CadFunc():
    global Tela_Cadastro_Func, txt_Nome_Func, txt_Setor_Func, txt_SalB_Func, txt_Bonus_Func, txt_Meses_Func, txt_Dias_Func
    Tela_Cadastro_Func = Tk()
    Tela_Cadastro_Func.title('Cadastro de Funcionários')
    Tela_Cadastro_Func.config()
    centralizar_window(Tela_Cadastro_Func)
    #Tela_Cadastro_Func.geometry('250x100')
    Tela_Cadastro_Func.lift()

    Frame_Titulo_Func = Frame(Tela_Cadastro_Func)
    Frame_Titulo_Func.pack(side=TOP)
    lblCadser = Label(Frame_Titulo_Func, text='Cadastro de Usuários', font=fonte_Titulo, fg='blue')
    lblCadser.pack(side=TOP)
    Frame_Dados_Func = Frame(Tela_Cadastro_Func)
    Frame_Dados_Func.pack()
    lbl_Nome_Func = Label(Frame_Dados_Func, text='Funcionário: ', font=fonte_Normal)
    lbl_Nome_Func.grid(row=0)
    txt_Nome_Func = Entry(Frame_Dados_Func, font=fonte_Normal)
    txt_Nome_Func.grid(row=0, column=1)
    lbl_Setor_Func = Label(Frame_Dados_Func, text='Setor: ', font=fonte_Normal)
    lbl_Setor_Func.grid(row=0, column=2)
    txt_Setor_Func = Entry(Frame_Dados_Func, font=fonte_Normal)
    txt_Setor_Func.grid(row=0, column=3)
    lbl_SalB_Func = Label(Frame_Dados_Func, text='Salário Bruto: ', font=fonte_Normal)
    lbl_SalB_Func.grid(row=1)
    txt_SalB_Func = Entry(Frame_Dados_Func, font=fonte_Normal)
    txt_SalB_Func.grid(row=1, column=1)
    lbl_Bonus_Func = Label(Frame_Dados_Func, text='Bônus: ', font=fonte_Normal)
    lbl_Bonus_Func.grid(row=1, column=2)
    txt_Bonus_Func = Entry(Frame_Dados_Func, font=fonte_Normal)
    txt_Bonus_Func.grid(row=1, column=3)
    lbl_Meses_Func = Label(Frame_Dados_Func, text='Meses Trabalhados: ', font=fonte_Normal)
    lbl_Meses_Func.grid(row=2, column=0)
    txt_Meses_Func = Entry(Frame_Dados_Func, font=fonte_Normal)
    txt_Meses_Func.grid(row=2, column=1)
    lbl_Dias_Func = Label(Frame_Dados_Func, text='Dias de férias: ', font=fonte_Normal)
    lbl_Dias_Func.grid(row=2, column=2)
    txt_Dias_Func = Entry(Frame_Dados_Func, font=fonte_Normal)
    txt_Dias_Func.grid(row=2, column=3)
    lbl_Dep_Func = Label(Frame_Dados_Func, text='Dependentes: ', font=fonte_Normal)
    lbl_Dep_Func.grid(row=3, column=0)
    txt_Dep_Func = Entry(Frame_Dados_Func, font=fonte_Normal)
    txt_Dep_Func.grid(row=3, column=1)
    txt_Nome_Func.focus()
    Frame_Btn_Cad_func = Frame(Tela_Cadastro_Func)
    Frame_Btn_Cad_func.pack(side=BOTTOM)
    if txt_Nome_Func.get() == "" or txt_Setor_Func.get() == "" or txt_SalB_Func.get() == "" or txt_Bonus_Func.get() == "" or txt_Meses_Func.get() == "" or txt_Dias_Func.get() == "":
        messagebox.showwarning('Atenção','Todos os campos devem ser preenchidos')
        Tela_Cadastro_Func.lift()
        txt_Nome_Func.focus()
    btn_Cad_Func = Button(Frame_Btn_Cad_func, text='Cadastrar', command=lambda: cadastrarFunc(txt_Nome_Func.get(), txt_Setor_Func.get(), txt_SalB_Func.get(), txt_Bonus_Func.get(), txt_Meses_Func.get(), txt_Dias_Func.get(), txt_Dep_Func.get()), fg='blue', font=fonte_Normal)
    #btn_Entrar.bind('<Button-1>', logar)
    btn_Cad_Func.pack(side=LEFT)
    btn_Sair_Func = Button(Frame_Btn_Cad_func, text='Cancelar', fg='blue', command=Tela_Cadastro_Func.destroy, font=fonte_Normal)
    btn_Sair_Func.pack(side=RIGHT)

def cadastrarFunc (func, setor, salb, bonus, mes, dias, dep):
    try:
        connection()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO Funcionarios (Id_Func, Nome_Func, Nome_Setor, Salario_Bruto, Bonus, Meses_Trab, Dias_Ferias, Dep) VALUES (seqUsers.nextval,'"+func+"','"+setor+"','"+salb+"','"+bonus+"','"+mes+"','"+dias+"','"+dep+"')")
        conexao.commit()
    except cx_Oracle.DataError as err:
        messagebox.showerror('DB Error: ' + str(err),'DataBase error1: ' + err)
    except cx_Oracle.DatabaseError as err:
        error, = err.args
        #messagebox.showerror('DB Error: ' + str(error.code), 'Oracle-Error-Code: '+ str(error.code))
        #messagebox.showerror('DB Error: ' + str(error.code),'Oracle-Error-Message:' + str(error.message))
        if error.code == 1400:
            messagebox.showerror(error.code,'Todos os campos devem ser preenchidos')
            Tela_Cadastro_Func.lift()
            txt_Nome_Func.focus()         
            return
        elif error.code == 1:
            messagebox.showerror(error.code,'Autor repetido')
            Tela_Cadastro_Func.lift()
            txt_Nome_Func.focus()
            return
        elif error.code == 936:
            stack = inspect.stack()
            messagebox.showerror(error.code,'Erro de Sintax, favor verificar código' + stack[1].function)
            Tela_Cadastro_Func.lift()
            txt_Nome_Func.focus()
        elif error.code == 933:
            messagebox.showerror(error.code,'Favor usar "." ao invés de "," nos valores numéricos decimais')
            Tela_Cadastro_Func.lift()
            txt_Nome_Func.focus()
        elif error.code == 2292:
            messagebox.showerror(error.code,'O autor tem livros cadastrados, favor remover os livros primeiro!')
            Tela_Cadastro_Func.lift()
            txt_Nome_Func.focus()
        elif error.code == 904:
            messagebox.showerror(error.code,'Campo não encontrado na tabela')
            Tela_Cadastro_Func.lift()
            txt_Nome_Func.focus()
        elif error.code == 955:
            pass
    except KeyError:
        messagebox.showerror('Erro','Erro de Sintax, favor verificar código')
    #except:
        #messagebox.showerror('Erro','DataBase error: ')
    else:
        messagebox.showinfo('Cadastro','Funcionário cadastrado com sucesso')
        op = messagebox.askyesno('Cadastro', 'Deseja cadastrar outro Funcionário?')
        
        if op == YES:
            txt_Nome_Func.delete(0, END)
            txt_Setor_Func.delete(0, END)
            txt_SalB_Func.delete(0, END)
            txt_Bonus_Func.delete(0, END)
            txt_Meses_Func.delete(0, END)
            txt_Dias_Func.delete(0, END)
            Tela_Cadastro_Func.lift()
            txt_Nome_Func.focus()
            txt_Nome_Func.focus()
            return
        elif op == NO:
            Tela_Cadastro_Func.destroy()
            pass
    
    
    '''try:
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
        print('Autor cadastrado com sucesso')'''

def ListaFun():
    global Tela_Lista_Func, tv
    Tela_Lista_Func = Tk()
    Tela_Lista_Func.title('Listar Funcionários')
    #centralizar_window(Tela_Lista_Func)
    
    Frame_func = LabelFrame(Tela_Lista_Func, text='Funcionários:')
    Frame_func.pack(fill='both', expand='yes', padx=10, pady=10)

    tv = ttk.Treeview(Frame_func, columns=('ID', 'Nome', 'Setor', 'Salario_Bruto', 'Bonus', 'Meses', 'Dias','Dep'), show='headings')
    tv.column('ID', minwidth=0, width=30)
    tv.column('Nome', minwidth=0, width=250)
    tv.column('Setor', minwidth=0, width=150)
    tv.column('Salario_Bruto', minwidth=0, width=70)
    tv.column('Bonus', minwidth=0, width=50)
    tv.column('Meses', minwidth=0, width=80)
    tv.column('Dias', minwidth=0, width=60)
    tv.column('Dep', minwidth=0, width=60)
    tv.heading('ID', text='ID')
    tv.heading('Nome', text='Nome')
    tv.heading('Setor', text='Setor')
    tv.heading('Salario_Bruto', text='Sal. Bruto')
    tv.heading('Bonus', text='Bonus')
    tv.heading('Meses', text='M. Trabalhados')
    tv.heading('Dias', text='Dias/Férias')
    tv.heading('Dep', text='Dependentes')
    tv.pack()
    listarFunc()

def listarFunc():
    try:
        connection()
        cursor=conexao.cursor()
        cursor.execute("SELECT * FROM Funcionarios ORDER BY Id_func")   
        linha = cursor.fetchone() # linha(1,'Arthur')
        if not linha:
            messagebox.showwarning ('Alerta','Não há Funcionários cadastrados')
            return
        aut=0
        tv.delete(*tv.get_children())
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
            tv.insert('','end', values=linha)
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

def ListaINSS():
    global Tela_Lista_INSS, tv
    Tela_Lista_INSS = Tk()
    Tela_Lista_INSS.title('Listar Funcionários')
    #centralizar_window(Tela_Lista_Func)
    
    Frame_INSS = LabelFrame(Tela_Lista_INSS, text='Tabela INSS:')
    Frame_INSS.pack(fill='both', expand='yes', padx=10, pady=10)

    tv = ttk.Treeview(Frame_INSS, columns=('ID', 'SalCont', 'Aliq', 'Parc_Dedu'), show='headings')
    tv.column('ID', minwidth=0, width=30)
    tv.column('SalCont', minwidth=0, width=250)
    tv.column('Aliq', minwidth=0, width=150)
    tv.column('Parc_Dedu', minwidth=0, width=70)
    tv.heading('ID', text='ID')
    tv.heading('SalCont', text='Salário Contribuição')
    tv.heading('Aliq', text='Alíquota %')
    tv.heading('Parc_Dedu', text='Parcela a Deduzir')
    tv.pack()
    listarINSS()

def listarINSS():
    try:
        connection()
        cursor=conexao.cursor()
        cursor.execute("SELECT * FROM inss ORDER BY Id_inss")   
        linha = cursor.fetchone() # linha(1,'Arthur')
        if not linha:
            messagebox.showwarning ('Alerta','Não há Funcionários cadastrados')
            return
        aut=0
        tv.delete(*tv.get_children())
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
            tv.insert('','end', values=linha)
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

def ListaIRRF():
    global Tela_Lista_IRFF, tv
    Tela_Lista_IRFF = Tk()
    Tela_Lista_IRFF.title('Listar Funcionários')
    #centralizar_window(Tela_Lista_Func)
    
    Frame_IRRF = LabelFrame(Tela_Lista_IRFF, text='Tabela IRRF:')
    Frame_IRRF.pack(fill='both', expand='yes', padx=10, pady=10)

    tv = ttk.Treeview(Frame_IRRF, columns=('ID', 'SalCont', 'Aliq', 'Parc_Dedu'), show='headings')
    tv.column('ID', minwidth=0, width=30)
    tv.column('SalCont', minwidth=0, width=250)
    tv.column('Aliq', minwidth=0, width=150)
    tv.column('Parc_Dedu', minwidth=0, width=70)
    tv.heading('ID', text='ID')
    tv.heading('SalCont', text='Salário Contribuição')
    tv.heading('Aliq', text='Alíquota %')
    tv.heading('Parc_Dedu', text='Dedução')
    tv.pack()
    listarIRRF()

    Frame_Dep = LabelFrame(Tela_Lista_IRFF, text='Parcela Dedução Dependes:')
    Frame_Dep.pack(fill='both', expand='yes', padx=10, pady=10)
    lbl_Dep_valor = Label(Frame_Dep,text='Valor: RS189,59')
    lbl_Dep_valor.pack(fill='both', expand='yes', padx=10, pady=10)

def listarIRRF():
    try:
        connection()
        cursor=conexao.cursor()
        cursor.execute("SELECT * FROM irrf ORDER BY Id_irrf")   
        linha = cursor.fetchone() # linha(1,'Arthur')
        if not linha:
            messagebox.showwarning ('Alerta','Não há Funcionários cadastrados')
            return
        aut=0
        tv.delete(*tv.get_children())
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
            tv.insert('','end', values=linha)
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

def Calculo():
    global Tela_Calculo, tv
    sal_bruto = 0
    Tela_Calculo = Tk()
    Tela_Calculo.title('Cálculos Trabalhistas')
    #centralizar_window(Tela_Lista_Func)
    
    Frame_Busca_Func = LabelFrame(Tela_Calculo, text='Funcionário:')
    Frame_Busca_Func.pack(fill='both', expand='yes', padx=10, pady=10)
    func = Entry(Frame_Busca_Func)
    func.pack(side=LEFT, padx=10)
    busca = Button(Frame_Busca_Func, text='Buscar', command=lambda: BuscarFun(func.get()))
    busca.pack(side=RIGHT, padx=10)

    Frame_Lis = LabelFrame(Tela_Calculo, text='Dados:')
    Frame_Lis.pack(fill='both', expand='yes', padx=10, pady=10)
    tv = ttk.Treeview(Frame_Lis, columns=('ID', 'Nome', 'Setor', 'Salario_Bruto', 'Bonus', 'Meses', 'Dias','Dep'), show='headings')
    tv.column('ID', minwidth=0, width=30)
    tv.column('Nome', minwidth=0, width=250)
    tv.column('Setor', minwidth=0, width=150)
    tv.column('Salario_Bruto', minwidth=0, width=70)
    tv.column('Bonus', minwidth=0, width=50)
    tv.column('Meses', minwidth=0, width=80)
    tv.column('Dias', minwidth=0, width=60)
    tv.column('Dep', minwidth=0, width=60)
    tv.heading('ID', text='ID')
    tv.heading('Nome', text='Nome')
    tv.heading('Setor', text='Setor')
    tv.heading('Salario_Bruto', text='Sal. Bruto')
    tv.heading('Bonus', text='Bonus')
    tv.heading('Meses', text='M. Trabalhados')
    tv.heading('Dias', text='Dias/Férias')
    tv.heading('Dep', text='Dependentes')
    tv.pack()
    
    

    Frame_Calc = LabelFrame(Tela_Calculo, text='Cálculos:')
    Frame_Calc.pack(fill='both', expand='yes', padx=10, pady=10)
    btn = Button(Frame_Calc, text='Calcular', command=getval)
    btn.pack()
    lbl_Sal_Mensal = Label(Frame_Calc,text='Salário Mensal:')
    lbl_Sal_Mensal.pack(side=LEFT)
    lbl_Resul_Sal_Mensal = Label(Frame_Calc, textvariable=sal_bruto )
    lbl_Resul_Sal_Mensal.pack(side=RIGHT)

def getval():
    global valores, sal_bruto, inss, parc_inss
    selec = tv.selection()[0]
    valores = tv.item(selec, 'values')
    sal_bruto = float(valores[3]) + float(valores[4])
    if sal_bruto <= 1100:
        inss = (sal_bruto * 7.5)/100
        parc_inss = 0
    elif sal_bruto >= 1100.01 or sal_bruto <= 2203.48:
        inss = (sal_bruto * 9)/100
        parc_inss = 16.5
    elif sal_bruto >= 2203.49 or sal_bruto <= 3305.22:
        inss = (sal_bruto * 12)/100
        parc_inss = 82.6
    elif sal_bruto >= 3305.23 or sal_bruto <= 6433.57:
        inss = (sal_bruto * 14)/100
        parc_inss = 148.71

def centralizar_window(window):
    windowWidth =  window.winfo_reqwidth()
    windowHeight = window.winfo_reqheight()
    #messagebox.showinfo('Teste', 'Width' + str(windowWidth) + 'Height' + str(windowHeight))
    # Gets both half the screen width/height and window width/height
    positionRight = int(window.winfo_screenwidth()/2 - windowWidth/1.5)
    positionDown = int(window.winfo_screenheight()/2 - windowHeight/3.5)
    # Positions the window in the center of the page.
    window.geometry("+{}+{}".format(positionRight, positionDown))
    '''print(windowWidth)
    print(windowHeight)
    print(window.winfo_screenwidth())
    print(window.winfo_screenheight())
    print(positionRight)
    print(positionDown)
    print('-------')'''

def splash():
    global Splash_Screen
    connection()
    #Tela de apresentação
    Splash_Screen = Tk()
    centralizar_window(Splash_Screen)
    #splash_Screen.eval('tk::PlaceWindow . center')
    #Definindo o tamanho 
    #splash_Screen.geometry('250x100')
    #Removendo as bordas
    Splash_Screen.overrideredirect(True)
    Splash_Screen.config()
    Label1 = Label(Splash_Screen, text='Bem vindo ao Gute Arbeit', fg='blue', font=fonte_Titulo).pack()
    #TesteImage1(splash_Screen)
    imagem = PhotoImage(file= sys.path[0] + '\images\GA1.png')
    #img = imagem.subsample(1,1)
    w = Label(Splash_Screen, image=imagem)
    w.imagem = imagem
    w.pack()
    
    #Label2 = Label(splash_Screen, text='Carregando bibliotecas necessárias...', fg= "green", font=fonte_Normal).pack(side=BOTTOM)

#Tela de login
def Tela_Login():
    global txt_Id_Usuario, txt_Pass, Login_Tela
    #Fecha a janela de splash
    if tentativa <= 3:
        Splash_Screen.destroy()
    

    #Criando a tela de login
    Login_Tela = Tk()
    #login_Tela.geometry('400x150')
    centralizar_window(Login_Tela)
    Login_Tela.title('Login')
    #login_Tela.eval('tk::PlaceWindow . center')
    #login_Tela.iconbitmap('./images/GA4.png')
    Login_Tela.config()

    #Criado o frame do título
    Frame_Login_titulo = Frame(Login_Tela).pack(side=TOP)

    lbl_Titulo_Login = Label(Frame_Login_titulo, text='LOGIN', font=fonte_Titulo)
    lbl_Titulo_Login.pack()

    #criando o frame de entrada de dados
    Frame_Dados_Login = Frame(Login_Tela)
    Frame_Dados_Login.pack()
    
    lbl_User = Label(Frame_Dados_Login, text='Usuário:', font=fonte_Normal, width=10, fg='blue')
    lbl_User.grid(row=0)
    txt_Id_Usuario = Entry(Frame_Dados_Login, width=20, font=fonte_Texto)
    txt_Id_Usuario.grid(row=0, column=1)
    txt_Id_Usuario.focus()
    label_Pass = Label(Frame_Dados_Login, text='Senha:', font=fonte_Normal, width=10, fg='blue')
    label_Pass.grid(row=1)
    txt_Pass = Entry(Frame_Dados_Login, width=20, font=fonte_Texto, show='*')
    txt_Pass.grid(row=1, column=1)
    

    #Criando o frame dos botões
    Frame_Btn = Frame(Login_Tela).pack(side=BOTTOM)
    img_Sair = PhotoImage(file= sys.path[0] + './images/exit (2).png')
    img_Sair = img_Sair.subsample(3,3)
    img_log = PhotoImage(file= sys.path[0] + './images/user1.png')
    img_log = img_log.subsample(3,3)
    btn_Entrar=Button(Frame_Btn, text='Login', fg='blue', width=55, height=25, command=lambda: logar(txt_Id_Usuario, txt_Pass), image=img_log, compound=LEFT, font=fonte_Normal)
    #btn_Entrar.bind('<Button-1>', logar)
    btn_Entrar.imagem = img_log
    btn_Entrar.pack(side=LEFT)
    btn_Sair=Button(Frame_Btn, text='', fg='blue', command=Login_Tela.destroy, compound=LEFT, width=55, height=25, image=img_Sair, font=fonte_Normal)
    btn_Sair.imagem = img_Sair
    btn_Sair.pack(side=RIGHT)

    
    



    #login_Tela.mainloop()
 
#Função Sair  
def _quit():  
   Janela.quit()  
   Janela.destroy()  
   exit()  

#Iniciando o Layout da janela, como tamanho, posição, tema, botões, caixas de texto e etc.
def programa():
    global Janela 
    connection()   
    #Criação e Janela propriamente dita, definindo o objeto.
    Janela = Tk()
    Janela.title('Gute Arbeit Sistema de RH')
    centralizar_window(Janela)
    Janela.geometry('660x480+400+150')
    #--- Criando o Menu
    MenuBar = Menu(Janela)
    Janela.config(menu=MenuBar)
    
    #---
    #btn_Sair=Button(Janela, text='Sair', fg='blue', command=_quit)
    #btn_Sair.pack(side=BOTTOM)

    
    #Menu Arquivo  
    Menu_Arq= Menu(MenuBar, tearoff=0)  
    #Menu_Arq.add_command(label="New")  
    #Menu_Arq.add_separator()  
    Menu_Arq.add_command(label="Sair", command=_quit)  
    MenuBar.add_cascade(label="Arquivo", menu=Menu_Arq)
    #Menu Cadastro  
    Menu_Cad= Menu(MenuBar, tearoff=0)  
    Menu_Cad.add_command(label="Funcionário", command=CadFunc)
    Menu_Cad.add_separator()  
    Menu_Cad.add_command(label="Usuário Sistema", command=CadUser)  
    MenuBar.add_cascade(label="Cadastrar", menu=Menu_Cad)
    #Menu Listagem  
    Menu_Lis= Menu(MenuBar, tearoff=0)  
    Menu_Lis.add_command(label="Funcionário", command=ListaFun)
    Menu_Lis.add_separator()
    Menu_Lis.add_command(label="Tabela INSS", command=ListaINSS)
    Menu_Lis.add_command(label="Tabela IRRF", command=ListaIRRF)
    Menu_Lis.add_separator()  
    Menu_Lis.add_command(label="Usuário Sistema", command=ListaUser)  
    MenuBar.add_cascade(label="Listar", menu=Menu_Lis)

    #Menu Calculos
    Menu_Calc = Menu(MenuBar, tearoff=0)
    Menu_Calc.add_command(label="Cálculos", command=Calculo)
    MenuBar.add_cascade(label='Cálculos', menu=Menu_Calc)

    #Painel Superior
    PainelSuperior = Frame(Janela)
    PainelSuperior["pady"] = 5
    PainelSuperior.pack()

    #Título do Painel Superior
    Titulo = Label(PainelSuperior, text="Güte Arbeit Sistema de RH", justify='center', font=fonte_Titulo, fg='blue')
    #titulo["font"] = ("Arial", "16", "bold")
    Titulo.pack()

    #Painel Central
    Painel_Central = Frame(Janela)
    Painel_Central.pack()

    #



    #janela.mainloop()




splash()
Splash_Screen.after(2000,Tela_Login)


mainloop()
