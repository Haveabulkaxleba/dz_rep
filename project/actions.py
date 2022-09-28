def view_data():
    with open('project\my_file.txt', 'r', encoding='utf-8') as mf:
        read = mf.read()
    return read


def add_data(data):
    with open('project\my_file.txt', 'a', encoding='utf-8') as mf:
        write = mf.write(f'\n{data}')


def import_data(data):
    with open(f'project\{data}', 'r', encoding='utf-8') as mf:
        read = mf.read()
        new = read.replace(', ', '\n')
    with open('project\my_file.txt', 'a', encoding='utf-8') as mf:
        write = mf.write(f'\n{new}\n')


def export_data(data):
    with open('project\my_file.txt', 'r', encoding='utf-8') as mf:
        read = mf.read()
    with open(f'project\{data}', 'a', encoding='utf-8') as mf:
        write = mf.write(f'\n{read}\n')


def export_with_commas(data):
    with open('project\my_file.txt', 'r', encoding='utf-8') as mf:
        lst = mf.readlines()
    s = ''
    for i, elem in enumerate(lst):
        if elem != '\n':
            s += elem.strip()+', '
        else:
            with open(f'project\{data}', 'a', encoding='utf-8') as mf:
                mf.write(s + '\n')
            s = ''