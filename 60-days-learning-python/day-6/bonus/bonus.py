contents = ["This is a test",
            "This is another test",
            "This another one!"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", "w")
    file.write(content)

teste = ("My string is "
         "here")
