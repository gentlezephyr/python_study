list_of_hello = ['hello', 'world', 'python', 'code']

filenames = ['hello.txt', 'world.txt', 'python.txt', 'code.txt']

for list_of_hello, filename in zip(list_of_hello, filenames):
    file = open(f"files/{filename}", "w")
    file.write(list_of_hello)
    file.close()
