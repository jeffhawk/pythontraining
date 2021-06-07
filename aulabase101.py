#Declaração de variáveis globais
Arq = "biblios.txt"
Py = 'PySimpleGUI'
Oracx = 'cx_Oracle'
biblio = False
biblios = ['PySimpleGUI','cx_Oracle','pip','termcolor']
caminho = 'C:\\Courses\\instantclient-basic-windows.x64-19.6.0.0.0dbru\\instantclient_19_6'
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
    import subprocess
    from os import system
    biblio = True
    os.chdir("C:\\Courses1\\instantclient-basic-windows.x64-19.6.0.0.0dbru\\instantclient_19_6")
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
        os.chdir("C:\\Courses\\instantclient-basic-windows.x64-19.6.0.0.0dbru\\instantclient_19_6")  
except:
    raise


#Subs, Módulos e Classes
    
    
def Main():
    if biblio == True:
        print('Entrou no sistema, OK!')
    else:
        print('Decidiu não instalar e saiu!')





Main()