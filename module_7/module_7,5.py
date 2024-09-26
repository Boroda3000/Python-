import os
import time

def display_file_info(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            filetime = os.path.getmtime(file_path)
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            file_size = os.path.getsize(file_path)
            parent_directory = os.path.dirname(file_path)
            print(f"Файл: {file}")
            print(f"Полный путь: {file_path}")
            print(f"Родительская директория: {parent_directory}")
            print(f"Последнее изменение: {formatted_time}")
            print(f"Размер: {file_size} байт")
            print('--------------')


directory = '.'
display_file_info(directory)