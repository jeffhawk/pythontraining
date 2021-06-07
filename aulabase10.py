#Declaração de variáveis globais
Arq = "biblios.txt"
Py = 'PySimpleGUI'
Oracx = 'cx_Oracle'
biblio = False
biblios = ['PySimpleGUI','cx_Oracle','os','ctypes','sys','string','pip','subprocess','system']
#python -m pip install cx_Oracle
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
except ImportError:
    #print (len(biblios))
    #system('cls')
    print('Erro ao tentar importar bibliotecas necessárias!!')
    for i in biblios:
        print(i)

    print('Erro ao tentar importar bibliotecas')
    atua = input('Deseja instalar as bibliotecas necessárias? - S/N: ')
    if atua == 's' or atua == 'S':
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', Py])
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', Oracx])
        '''if not Py in sys.modules.keys():
            pip.main(['install', Py])
        if not Oracx in sys.modules.keys():
            pip.main(['install', Oracx])'''
        print('Instalação efetuada!')
        biblio = True
    else:
        print('Bibliotecas não  instaladas!')
        biblio = False


#Subs, Módulos e Classes
    
    
def Main():
    if biblio == True:
        print('Entrou no sistema, OK!')
    else:
        print('Decidiu não instalar e saiu!')





Main()