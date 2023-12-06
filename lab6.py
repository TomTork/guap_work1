# Написать программу для переименования файлов в каталоге по
# определенному шаблону. Вывести в текстовом файле иерархию каталогов, изменённые файлы выделить

import os

path = input(r'Введите файл к каталогу: ')
name_file = input(r'Введите имя файла, который нужно переименовать: ')

new_name_file = input('Имя нового файла с расширением: ')
os.rename(os.path.join(path, name_file), os.path.join(path, new_name_file))

f = open('answer', 'w', encoding='utf-8')
f.write(f'{path}\{name_file.upper()}')
f.write('\n')
f.write(f'{path}\{new_name_file.upper()}')
f.close()

