import PySimpleGUI as sg

sg.theme('Black')

def calc(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    meters = round(meters, 2)
    return meters


def first_row(text_label, input_label):
    return sg.Text(text_label), sg.InputText(input_label, key='feet')


def second_row(text_label, input_label):
    return sg.Text(text_label), sg.InputText(input_label, key='inches')


layout = [
    *[first_row('Feet:', '')],
    *[second_row('Inches', '')],
    [sg.Button('Convert')], [sg.Text(key='output')],
    [sg.Button('Exit')]
]

window = sg.Window('Calculate feet and inches to meters', layout)

while True:
    event, values = window.read()
    print(event, values)
    feet = values['feet']
    inches = values['inches']
    match event:
        case 'Convert':
            if feet == '' or inches == '':
                sg.Popup('Please provide two numbers!')
            else:
                window['output'].update(value=calc(int(feet), int(inches)))
        case 'Exit':
            break
        case sg.WINDOW_CLOSED:
            break

window.close()
