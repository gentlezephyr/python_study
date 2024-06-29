filenames = "a.txt", "b.txt", "c.txt"

for filename in filenames:
    file = open(filename, "r")
    filenames = file.read()
    print(f"{filenames}")
