while True:
    user_prompt = input("Type add, show, edit, complete or exit to continue: ")
    user_prompt = user_prompt.strip().lower()

    match user_prompt:
        case "add":
            todo = input("Enter a TODO: ")  # + "\n" Could be used.
            file = open("files/todos.txt", "r")
            todos = file.readlines()
            file.close() # Testing purposes.

            todos.append(f"{todo.capitalize()}\n")

            file = open("files/todos.txt", "w")  # Overwrite the file with the new TODOs. We can use "a" argument too.
            file.writelines(todos)  # \n is used to add a new line.
            file.close()
        case "show":
            file = open("files/todos.txt", "r")
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                row = f"{index + 1}. {item}"
                print(row)
        case "edit":
            number = int(input("Enter the number of the TODO you want to edit: "))
            number -= 1
            new_todo = input("Enter the new TODO: ")
            todos[number] = new_todo.capitalize()
        case "complete":
            number = int(input("Enter the number of the TODO you want to complete: "))
            todos.pop(number - 1)
        case "exit":
            print("Bye!")
            break

#006