while True:

    user_prompt = input("Type add, show, edit, complete or exit to continue: ")
    user_prompt = user_prompt.strip().lower()

    match user_prompt:
        case "add":

            todo = input("Enter a TODO: ")

            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(f"{todo.capitalize()}\n")

            with open("files/todos.txt", "w") as file:
                file.writelines(todos)

        case "show":

            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index + 1}. {item}"
                print(row)

        case "edit":

            number = int(input("Enter the number of the TODO you want to edit: "))
            number -= 1

            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            new_todo = input("Enter the new TODO: ")
            todos[number] = new_todo.capitalize() + "\n"

            with open("files/todos.txt", "w") as file:
                file.writelines(todos)

        case "complete":

            number = int(input("Enter the number of the TODO you want to complete: "))
            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            to_complete = todos[number - 1].strip("\n")

            todos.pop(number - 1)

            with open("files/todos.txt", "w") as file:
                file.writelines(todos)

            message = f"The TODO {to_complete} has been completed!"
            print(message)

        case "exit":
            print("Bye!")
            break
