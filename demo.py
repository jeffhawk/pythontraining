from threading import Timer
import PySimpleGUI as sg
import time

from PySimpleGUI.PySimpleGUI import DEFAULT_BASE64_LOADING_GIF, DEFAULT_PROGRESS_BAR_COLOR_OFFICIAL
# show a splash screen with an animated gif (loading.gif)
'''sg.PopupAutoClose('Teste')
sg.popup_auto_close('Teste1')
sg.popup_no_buttons('Teste2')
time.sleep(10)
sg.popup_no_buttons() > None
'''
sg.popup("SONASCAN is starting...", font=('Helvetica', 100), icon=None, button_type=sg.POPUP_BUTTONS_NO_BUTTONS, background_color='#00bdd4', auto_close=True, auto_close_duration=5, title="SONASCAN is starting...")
'''
# first show how to use PopupAnimated using built-in GIF image
for i in range(3000):
    sg.PopupAnimated(sg.DEFAULT_BASE64_LOADING_GIF, background_color='white', time_between_frames=100)
sg.PopupAnimated(None)      # close all Animated Popups

while True:
    sg.Window('Teste',layout=None,icon=DEFAULT_BASE64_LOADING_GIF)

'''
