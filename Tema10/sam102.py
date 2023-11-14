import os


def print_file(file):
    with open(file) as f:
        if os.stat(file).st_size == 0:
            raise Exception(f"Файл '{file}' пустой")
        print(f.readline())


try:
    print_file('empty_file.txt')
except Exception as e:
    print(e)

try:
    print_file('not_empty_file.txt')
except Exception as e:
    print(e)
