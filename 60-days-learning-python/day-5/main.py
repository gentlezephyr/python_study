todos = []

while True:
    user_prompt = input("Type add, show, edit, complete or exit to continue: ")
    user_prompt = user_prompt.strip().lower()

    match user_prompt:
        case "add":
           todo = input("Enter a TODO: ")
           todos.append(todo.capitalize())
        case "show":
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