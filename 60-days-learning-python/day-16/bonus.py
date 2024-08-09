import PySimpleGUI as sg  # PySimpleGUI-4-foss


def first_row(label_text, input_box, button_fb):
    return sg.Text(label_text), sg.Input(input_box), sg.FilesBrowse(button_fb)


def second_row(label_text, input_box, button_fb):
    return sg.Text(label_text), sg.Input(input_box), sg.FolderBrowse(button_fb)


layout = [
    *[first_row('Select Files', '', 'Choose')],
    *[second_row('Select Destination', '', 'Choose')],
    [sg.Button('Compress')]
]

window = sg.Window('Compressor', layout)

window.read()
window.close()
