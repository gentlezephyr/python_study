import pathlib
import zipfile
from pathlib import Path


def archive_zip(filepaths, file_name, folder_dest):
    dest_path = Path(folder_dest) / file_name
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


if __name__ == '__main__':
    archive_zip(filepaths=['bonus.py', 'gui.py'], file_name='naruto.zip')
