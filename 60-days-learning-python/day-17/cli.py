# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %H:%M:%S / %p")
print(now)

while True:

    user_prompt = input("Type add, show, edit, complete or exit to continue: ")
    user_prompt = user_prompt.strip().lower()

    if user_prompt.startswith('add'):

        todo = user_prompt[4:]

        todos = functions.get_todos()

        todos.append(f"{todo.capitalize()}\n")

        functions.write_todos(todos)

    elif user_prompt.startswith('show'):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}. {item}"
            print(row)

    elif user_prompt.startswith('edit'):
        try:
            number = int(user_prompt[5:])
            number -= 1

            todos = functions.get_todos()

            new_todo = input("Enter the new TODO: ")
            todos[number] = new_todo.capitalize() + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("Command not recognized. Please try again.")
            continue

    elif user_prompt.startswith('complete'):
        try:
            number = int(user_prompt[9:])
            todos = functions.get_todos()

            to_complete = todos[number - 1].strip("\n")

            todos.pop(number - 1)

            functions.write_todos(todos)

            message = f"The TODO {to_complete} has been completed!"
            print(message)
        except IndexError:
            print("Number not recognized. Please try again.")
            continue

    elif user_prompt.startswith('exit'):
        print("Bye!")
        break
    else:
        print("Command not recognized. Please try again.")
