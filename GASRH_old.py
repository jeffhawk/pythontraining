"""PROJETO FINAL - SISTEMA DE RH - "Gute Arbeit Sistema de RH"
Software/Programa desenvolvido aplicando os conhecimentos obtidos em sala de aula para obtenção de nota final na PONTIFÍCIA UNIVERSIDADE CATÓLICA DE CAMPINAS - PUC-CAMPINAS,
no CENTRO DE CIÊNCIAS EXATAS, AMBIENTAIS E DE TECNOLOGIA para o curso de SISTEMAS DE INFORMAÇÃO.

JEFFERSON EDUARDO LUIZ
RA 19568823

Foi empregado todo o conhecimento obtido em sala de aula e acrescentado algumas funcionalidades aprendida de forma autônoma ao curso.

"""
# Iniciando com a importação das bibliotecas utilizadas
# Bibliotecas
import os
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import (
    Button,
    DEFAULT_BASE64_LOADING_GIF,
    OK,
    POPUP_BUTTONS_NO_BUTTONS,
    popup,
)

# Iniciando o Layout da janela, como tamanho, posição, tema, botões, caixas de texto e etc.
sg.theme("Reddit")
layout = [
    [sg.Text("Usuário:"), sg.Input(key="usuario", size=(20, 1))],
    [sg.Text("Senha..:"), sg.Input(key="senha", password_char="*", size=(20, 1))],
    [sg.Checkbox("Salvar Login?")],
    [sg.Button("Entrar"), sg.Button("Sair")],
]

# Criação e Janela propriamente dita, definindo o objeto.
janela = sg.Window("Tela de Login", layout)

# Declaração de variáveis
countar = 0


# Ler os eventos
while True:
    if countar == 0:
        sg.popup(
            "Teste.....",
            title="Teste",
            button_type=POPUP_BUTTONS_NO_BUTTONS,
            no_titlebar=True,
            auto_close=True,
            auto_close_duration=5,
        )
        for i in range(1000):
            sg.PopupAnimated(
                image_source=DEFAULT_BASE64_LOADING_GIF,
                time_between_frames=100,
                background_color="yellow",
                message="Teste",
            )
            # sg.time.sleep(3)
        sg.PopupAnimated(None)
    eventos, valores = janela.read()
    if eventos in (sg.WINDOW_CLOSED, "Sair"):
        break
    if eventos == "Entrar":
        if valores["usuario"] == "jeff" and valores["senha"] == "1234":
            sg.theme("Reddit")
            layout_msgbox = [
                [sg.Text("Bem vindo")],
            ]
