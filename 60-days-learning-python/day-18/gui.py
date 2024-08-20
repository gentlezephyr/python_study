import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

sg.theme('Black')


def gui_row(input_text, button_add):
    return sg.InputText(input_text, tooltip='Enter a todo', key='todo'), sg.Button(button_add, key='Add', tooltip='Add a to do!', mouseover_colors='black')


def second_row(button_edit, complete_button):
    return sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True,
                      size=(45, 10)), sg.Button(button_edit), sg.Button(complete_button, key='Complete', tooltip='Complete to do!')


layout = [
    [sg.Text('', key='clock')],
    [sg.Text('Type in a to-do')],
    *[gui_row((), 'Add')],
    *[second_row('Edit', 'Complete')],
    [sg.Button('Exit')]

    # sg.InputText(tooltip='Enter a to-do')
]

window = sg.Window('My To-do App', layout, font=('Helvetica', 10))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %H:%M:%S / %p"))
    print(event)
    print(values)
    match event:
        case 'Add':
            if values['todo'] == '':
                sg.Popup('Write something!')
            else:
                todo = functions.get_todos()
                todo.append(values['todo'] + '\n')
                functions.write_todos(todo)
                window['todos'].update(values=todo)
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_to_do = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_to_do
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.Popup('Select an item first!')
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.Popup('Select an item first!')
        case 'todos':
            if values['todos'] and values['todos'][0] != '':
                window['todo'].update(value=values['todos'][0])
            else:
                sg.Popup("There's nothing here!")
        case 'Exit':
            break
        case sg.WINDOW_CLOSED:
            break

window.close()
