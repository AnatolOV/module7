import os
import  time
# path_to_dir = os.getcwd()
# # print(path_to_dir)
# filename = 'module_7_5.py'
# path_to_file = os.path.join(path_to_dir, filename)
# print(path_to_file)
# print(os.path.getmtime(path_to_dir))
# print(os.listdir('.'))

for root, dirs, files in os.walk('.'):
  for file in files:
    filepath = os.path.join(root, file)
    filetime = os.path.getmtime(filepath)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize(filepath)
    parent_dir = os.path.dirname(filepath)
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

# with open('products.txt', 'a', encoding='utf-8') as file:
#     file.write(' 55553')
# with open('products.txt', 'r', encoding='utf-8') as file:
#     data = file.read()
#     print(data)


