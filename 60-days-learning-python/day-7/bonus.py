filenames = ["1.doc", "1.report", "1.representation"]

filenames = [f"{filename.replace('.', '-')}" + ".txt" for filename in filenames]

print(filenames)
