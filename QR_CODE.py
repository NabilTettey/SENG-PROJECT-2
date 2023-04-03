import PySimpleGUI as sg
import qrcode
import io
import threading

def generate_qr_code(input_value):
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(input_value)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    bio = io.BytesIO()
    img.save(bio, format='PNG')
    img_bytes = bio.getvalue()

    window['-IMAGE-'].update(data=img_bytes)

    global saved_img_bytes
    saved_img_bytes = img_bytes

def save_image():
    file_path = sg.popup_get_file('Save Image', save_as=True, file_types=(('PNG', '*.png'),))

    if file_path:
        with open(file_path, 'wb') as file:
            file.write(saved_img_bytes)
            sg.popup(f'Saved image to {file_path}')

def main():
    layout = [[sg.Text('Enter input:'), sg.InputText(key='-INPUT-')],
              [sg.Button('Generate QR Code', key='-GENERATE-',button_color=('black','lightblue'))],
              [sg.Image(key='-IMAGE-')],
              [sg.Button('Save Image', key='-SAVE-', disabled=True,button_color=('black','lightblue'))]]
    global window
    window = sg.Window('QR Code Generator', layout,background_color='grey')

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break
        if event == '-GENERATE-':
            input_value = values['-INPUT-']
        if not input_value:
                sg.popup_error('Abeg type something in there ah!')
        else:
            threading.Thread(target=generate_qr_code, args=(input_value,)).start()

            window['-SAVE-'].update(disabled=False)
        if event == '-SAVE-':
            save_image()

    window.close()

if __name__ == '__main__':
    main()
