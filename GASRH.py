'''PROJETO FINAL - SISTEMA DE RH - "Gute Arbeit Sistema de RH"
Software/Programa desenvolvido aplicando os conhecimentos obtidos em sala de aula para obtenção de nota final na PONTIFÍCIA UNIVERSIDADE CATÓLICA DE CAMPINAS - PUC-CAMPINAS,
no CENTRO DE CIÊNCIAS EXATAS, AMBIENTAIS E DE TECNOLOGIA para o curso de SISTEMAS DE INFORMAÇÃO.

JEFFERSON EDUARDO LUIZ
RA 19568823

Foi empregado todo o conhecimento obtido em sala de aula e acrescentado algumas funcionalidades aprendida de forma autônoma ao curso.

'''
#Declaração de variáveis globais
Arq = "biblios.txt"
Py = 'PySimpleGUI'
Oracx = 'cx_Oracle'
biblio = False
#python -m pip install cx_Oracle
atua = ''

#Iniciando com a importação das bibliotecas utilizadas
#Bibliotecas
# #Verifica se existe as bibliotecas, caso contrário pergunta se quer instala-las 
try:
    import os
    import PySimpleGUI as sg
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





#Iniciando o Layout da janela, como tamanho, posição, tema, botões, caixas de texto e etc.
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário:'), sg.Input(key='usuario', size=(20,1))],
    [sg.Text('Senha..:'), sg.Input(key='senha', password_char='*', size=(20,1))],
    [sg.Checkbox('Salvar Login?')],
    [sg.Button('Entrar'), sg.Button('Sair')]
]

#Criação e Janela propriamente dita, definindo o objeto.
janela = sg.Window('Tela de Login', layout)

#Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos in (sg.WINDOW_CLOSED, 'Sair'):
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'jeff' and valores['senha'] == '1234':
            sg.theme('Reddit')
            layout_msgbox = [
                [sg.Text('Bem vindo')],

            ]
            
