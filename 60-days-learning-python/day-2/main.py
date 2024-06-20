user_prompt = "Enter a TODO: "

todos = []

while True:
    todo = input(user_prompt)
    todos.append(todo.title())
    print(todos)