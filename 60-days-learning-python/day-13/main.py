# import os
#
#
# def get_todos():
#     file_check = 'todos.txt'
#     folder_path = 'files'
#     folder = os.listdir(folder_path)
#     if file_check in folder:
#         file_path = os.path.join(folder_path, file_check)
#         with open(file_path, "r") as file_local:
#             todos_local = file_local.readlines()
#             return todos_local

def get_todos(filepath="files/todos.txt"):
    """Read the text file from the filepath"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todos_local, filepath="files/todos.txt"):
    """Write the to-do in the text file from the filepath"""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_local)


while True:

    user_prompt = input("Type add, show, edit, complete or exit to continue: ")
    user_prompt = user_prompt.strip().lower()

    if user_prompt.startswith('add'):

        todo = user_prompt[4:]

        todos = get_todos()

        todos.append(f"{todo.capitalize()}\n")

        write_todos(todos)

    elif user_prompt.startswith('show'):

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}. {item}"
            print(row)

    elif user_prompt.startswith('edit'):
        try:
            number = int(user_prompt[5:])
            number -= 1

            todos = get_todos()

            new_todo = input("Enter the new TODO: ")
            todos[number] = new_todo.capitalize() + "\n"

            write_todos(todos)
        except ValueError:
            print("Command not recognized. Please try again.")
            continue

    elif user_prompt.startswith('complete'):
        try:
            number = int(user_prompt[9:])
            todos = get_todos()

            to_complete = todos[number - 1].strip("\n")

            todos.pop(number - 1)

            write_todos(todos)

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
