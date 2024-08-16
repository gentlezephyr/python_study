# import os
#
#
# def get_todos():
#     file_check = 'todos.txt'
#     folder_path = 'files'
#     folder = os.listdir(folder_path)
#     if file_check in folder:
#         file_path = os.path.join(folder_path, file_check)
#         with open(file_path, "r") as file_local:
#             todos_local = file_local.readlines()
#             return todos_local

FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """Read the text file from the filepath"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todos_local, filepath=FILEPATH):
    """Write the to-do in the text file from the filepath"""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_local)


# print('Rice is good')

if __name__ == '__main__':
    print('Rice is not good')
