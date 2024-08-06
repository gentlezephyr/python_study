import glob

lfiles = glob.glob('**/*.txt', recursive=True)

for file in lfiles:
    with open(file, 'r') as file_open:
        text_from = file_open.readlines()
        print(text_from)

