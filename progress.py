"""
    Demo Program - Progress Meter using a Text Element
    This program was written by @jason990420
    This is a clever use of a Text Element to create the same look
    and feel of a progress bar in PySimpleGUI using only a Text Element.
    Copyright 2020 PySimpleGUI.org
"""

from tkinter.constants import BOTTOM, TRUE
from webbrowser import BackgroundBrowser
import PySimpleGUI as sg

sg.theme('Reddit')


   
layout = [
    [sg.Text('', size=(50, 1), relief='sunken', font=('Courier', 11), text_color='orange', background_color='black',key='-TEXT-', metadata=0)],
    [sg.Text('', size=(6, 1), justification='center', font=('Courier', 11), text_color='light green', key='-label-', metadata=0, background_color='black')]
]

window = sg.Window('Title', layout, size=(500,70), finalize=True, element_justification='center', background_color='black', no_titlebar=TRUE, transparent_color='black')

text = window['-TEXT-']
text1 = window['-label-']

while True:

    event, values = window.read(timeout=100)

    if event == sg.WINDOW_CLOSED:
        break
    text.metadata = (text.metadata + 1) % 51
    text.update('█' * text.metadata)
    text1.update(str(text.metadata * 2) + '%')

    if text.metadata >= 50:
        break


window.close()