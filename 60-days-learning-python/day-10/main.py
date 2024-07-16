while True:

    user_prompt = input("Type add, show, edit, complete or exit to continue: ")
    user_prompt = user_prompt.strip().lower()

    if user_prompt.startswith('add'):

        todo = user_prompt[4:]

        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(f"{todo.capitalize()}\n")

        with open("files/todos.txt", "w") as file:
            file.writelines(todos)

    elif user_prompt.startswith('show'):

        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}. {item}"
            print(row)

    elif user_prompt.startswith('edit'):
        try:
            number = int(user_prompt[5:])
            number -= 1

            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            new_todo = input("Enter the new TODO: ")
            todos[number] = new_todo.capitalize() + "\n"

            with open("files/todos.txt", "w") as file:
                file.writelines(todos)
        except ValueError:
            print("Command not recognized. Please try again.")
            continue

    elif user_prompt.startswith('complete'):
        try:
            number = int(user_prompt[9:])
            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            to_complete = todos[number - 1].strip("\n")

            todos.pop(number - 1)

            with open("files/todos.txt", "w") as file:
                file.writelines(todos)

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

        #Will this work?
