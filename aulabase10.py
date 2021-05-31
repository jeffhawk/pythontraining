#Declaração de variáveis globais
Arq = "biblios.txt"
Py = 'PySimpleGUI'
Oracx = 'cx_Oracle'
biblio = False
#python -m pip install cx_Oracle
atua = ''

#Importando as bibliotecas
# #Verifica se existe as bibliotecas, caso contrário pergunta se quer instala-las 
try:
    import os
    import PySimpleGUI as psg
    import cx_Oracle
    biblio = True
except ImportError:
    import sys
    import pip
    import subprocess
    for i in sys.modules.keys():
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