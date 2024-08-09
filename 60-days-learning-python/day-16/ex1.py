import PySimpleGUI as sg

feet_text = sg.Text('Enter Feet:')
feet_input = sg.Input()

inches_text = sg.Text('Enter Inches:')
inches_input = sg.Input()

convert_button = sg.Button('Convert')

window = sg.Window('Converter', layout=[[feet_text, feet_input], [inches_text, inches_input], [convert_button]])

window.read()
window.close()

