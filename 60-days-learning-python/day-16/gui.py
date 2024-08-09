import functions
import PySimpleGUI as sg


def gui_row(input_text, button_add):
    return sg.InputText(input_text, tooltip='Enter a todo'), sg.Button(button_add)


layout = [
    [sg.Text('Type in a to-do')],
    *[gui_row((), 'Add')],
    # sg.InputText(tooltip='Enter a to-do')
]

window = sg.Window('My To-do App', layout)

window.read()
print('Naruto')
window.close()
