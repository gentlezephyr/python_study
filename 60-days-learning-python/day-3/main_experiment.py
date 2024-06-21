todos = []

while True:
    user_prompt = input("Type add, show or exit to continue: ")
    user_prompt = user_prompt.strip().lower()

    match user_prompt:
        case "add":
           todo = input("Enter a TODO: ")
           todos.append(todo.capitalize())
        case "show" | "display": # Bitwise OR operator in Python
            for item in todos:
                print(item)
        case "exit":
            print("Bye!")
            break
        case _:
            print("Invalid input")