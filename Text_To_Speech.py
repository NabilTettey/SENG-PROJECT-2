import PySimpleGUI as sg
import pyttsx3

engine = pyttsx3.init()

layout = [ 
    [sg.InputText(key="-INPUT-"),sg.Button("Speak",button_color=('yellow','black'))],
     [sg.Text('Select Voice Type:',text_color='black'),sg.Radio("Male", "RADIO", default=True, key="-MALE-",background_color='gray'),sg.Radio("Female", "RADIO", key="-FEMALE-",background_color='grey')], 
    [sg.Text('Adjust Speed:',text_color='black'), sg.Slider(range=(0, 400), default_value=150, orientation='h', size=(10, 15), key='-SPEED-')]
]

window = sg.Window("Text to Speech App", layout,background_color='lightblue')

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    voices=engine.getProperty('voices')

    if event == "Speak":
        input_text = values["-INPUT-"]
        if values["-MALE-"]:
            engine.setProperty('voice', voices[0].id)  
        elif values["-FEMALE-"]:
            engine.setProperty('voice', voices[1].id)  
        rate = values['-SPEED-']
        engine.setProperty('rate', rate)
        engine.say(input_text)
        engine.runAndWait()
window.close()
