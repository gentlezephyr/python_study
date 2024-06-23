todos = []

while True:
    user_prompt = input("Type add, show, edit or exit to continue: ")
    user_prompt = user_prompt.strip().lower()

    match user_prompt:
        case "add":
           todo = input("Enter a TODO: ")
           todos.append(todo.capitalize())
        case "show":
            for item in todos:
                print(item)
        case "edit":
            number = int(input("Enter the number of the TODO you want to edit: "))
            number -= 1
            new_todo = input("Enter the new TODO: ")
            todos[number] = new_todo.capitalize()
        case "exit":
            print("Bye!")
            break