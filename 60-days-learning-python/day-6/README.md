With the file open, I could use argument "a" to append the string to the file. This will add the string to the end of the file.

I don't know why the use of the read command, if I delete the file, it doesn't work.

Some documentation from ChatGPT:

Sure! Here's a simple documentation for opening, reading, and writing files in Python, using your provided code as an example.

## File Operations in Python

Python provides several built-in functions for performing file operations. This documentation will cover the basics of opening, reading, and writing files.

### Opening Files

To open a file in Python, use the `open()` function. The `open()` function takes two parameters:
1. The name of the file.
2. The mode in which the file should be opened.

Common modes include:
- `'r'`: Read (default mode). Opens a file for reading.
- `'w'`: Write. Opens a file for writing (creates a new file if it doesn't exist or truncates the file if it exists).
- `'a'`: Append. Opens a file for appending (creates a new file if it doesn't exist).

Example:
```python
file = open("todos.txt", "r")
```

### Reading Files

To read the contents of a file, you can use the `read()`, `readline()`, or `readlines()` methods.
- `read()`: Reads the entire file as a single string.
- `readline()`: Reads a single line from the file.
- `readlines()`: Reads all the lines in a file and returns them as a list of strings.

Example:
```python
file = open("todos.txt", "r")
todos = file.readlines()
file.close()
```

### Writing to Files

To write to a file, you can use the `write()` or `writelines()` methods.
- `write()`: Writes a string to the file.
- `writelines()`: Writes a list of strings to the file.

Example:
```python
todos.append(f"{todo.capitalize()}\n")
file = open("todos.txt", "w")
file.writelines(todos)
file.close()
```

### Full Example

Here is the full example based on your provided code:

```python
# Case: Add a TODO
case = "add"

if case == "add":
    todo = input("Enter a TODO: ")
    
    # Open the file in read mode and read all lines
    file = open("todos.txt", "r")
    todos = file.readlines()
    file.close()
    
    # Add the new TODO to the list and capitalize it
    todos.append(f"{todo.capitalize()}\n")
    
    # Open the file in write mode and write the updated TODOs back to the file
    file = open("todos.txt", "w")
    file.writelines(todos)
    file.close()
```

### Using the `with` Statement

Using the `with` statement to open files is a good practice because it ensures that the file is properly closed after its suite finishes, even if an exception is raised.

Example:
```python
with open("todos.txt", "r") as file:
    todos = file.readlines()

todos.append(f"{todo.capitalize()}\n")

with open("todos.txt", "w") as file:
    file.writelines(todos)
```

This is a safer and more concise way to handle file operations in Python.

### Summary

- Use `open()` to open a file.
- Use `read()`, `readline()`, or `readlines()` to read a file.
- Use `write()` or `writelines()` to write to a file.
- Use the `with` statement for better resource management.

By following these guidelines, you can effectively manage file operations in Python.

To use especial characters in a string such as the path to a file, we can use _r"path to\something\todos.txt"_