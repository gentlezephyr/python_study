import functions
import PySimpleGUI as sg


def gui_row(input_text, button_add):
    return sg.InputText(input_text, tooltip='Enter a todo', key='todo'), sg.Button(button_add)


def second_row(button_edit):
    return sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True,
                      size=(45, 10)), sg.Button(button_edit)


layout = [
    [sg.Text('Type in a to-do')],
    *[gui_row((), 'Add')],
    *[second_row('Edit')]

    # sg.InputText(tooltip='Enter a to-do')
]

window = sg.Window('My To-do App', layout, font=('Helvetica', 10))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todo = functions.get_todos()
            todo.append(values['todo'] + '\n')
            functions.write_todos(todo)
            window['todos'].update(values=todo)
        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_to_do = values['todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_to_do
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WINDOW_CLOSED:
            break

window.close()
