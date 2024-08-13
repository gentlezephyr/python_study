import PySimpleGUI as sg  # PySimpleGUI-4-foss
import zip_function


def first_row(label_text, input_box, button_fb):
    return sg.Text(label_text), sg.Input(input_box), sg.FilesBrowse(button_fb, key='files')


def second_row(label_text, input_box, button_fb):
    return sg.Text(label_text), sg.Input(input_box), sg.FolderBrowse(button_fb, key='folders')


def third_row(compress_button, text_output):
    return sg.Button(compress_button), sg.Text(text_output, key='output', text_color='green')


layout = [
    *[first_row('Select Files', '', 'Choose')],
    *[second_row('Select Destination', '', 'Choose')],
    *[third_row('Compress', '')]
]

window = sg.Window('Compressor', layout)

while True:
    event, values = window.read()
    print(event)
    print(values)
    filepaths = values['files'].split(";")
    folders = values['folders']
    zip_function.archive_zip(filepaths, 'teste2.zip', folders)
    window['output'].update(value="Done")

window.close()
