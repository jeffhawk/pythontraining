'''PROJETO FINAL - SISTEMA DE RH - "Gute Arbeit Sistema de RH"
Software/Programa desenvolvido aplicando os conhecimentos obtidos em sala de aula para obtenção de nota final na PONTIFÍCIA UNIVERSIDADE CATÓLICA DE CAMPINAS - PUC-CAMPINAS,
no CENTRO DE CIÊNCIAS EXATAS, AMBIENTAIS E DE TECNOLOGIA para o curso de SISTEMAS DE INFORMAÇÃO.

JEFFERSON EDUARDO LUIZ
RA 19568823

Foi empregado todo o conhecimento obtido em sala de aula e acrescentado algumas funcionalidades aprendida de forma autônoma ao curso.

'''
#Iniciando com a importação das bibliotecas utilizadas
#Bibliotecas
import os
import PySimpleGUI as sg


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
            
