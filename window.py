# hello_world.py

from os import name
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Button, DEFAULT_BASE64_LOADING_GIF, OK

layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK",key='vai')]]

#window = sg.Window(title="Hello World", layout=layout, margins=(600, 400)).read()

window = sg.Window("Demo", layout, margins=(600,400))


countar = 0
while True:
    if countar == 0:
        for i in range(1,1000):
            #sg.PopupAnimated(image_source=DEFAULT_BASE64_LOADING_GIF, time_between_frames=100)
            sg.one_line_progress_meter('Teste', i+1, 1000,'contador', orientation='h')
            #sg.time.sleep(3)
        sg.one_line_progress_meter(None)
        sg.PopupAnimated(None)
        countar = 1
    #print(countar)

    event, values = window.read()
    #sg.popup_non_blocking(event, values)
    #print(event, values)
    # show a splash screen with an animated gif (loading.gif)
    #for i in range(100):
    
    #window.disappear()
    
    
    
    #window.reappear()

    
    if event == sg.WIN_CLOSED:           # always,  always give a way out!
        #sg.PopupAnimated(None)
        break
       
window.close()
