import zipfile
from pathlib import Path


def extract_zip(filepath, folder_dest):
    dest_path = Path(folder_dest)
    with zipfile.ZipFile(filepath, 'r') as file:
        file.extractall(dest_path)


if __name__ == '__main__':
    extract_zip(r"C:\Users\Elara\Documents\Projects\python_study\60-days-learning-python\day-18\todos.zip",
                r"C:\Users\Elara\Documents\Projects\python_study\60-days-learning-python\day-18")
