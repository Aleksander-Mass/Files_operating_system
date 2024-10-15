import os
import time

# Указываем путь к каталогу (в данном случае текущий каталог)
directory = "."

# Обход всех подкаталогов и файлов в указанной директории
for root, dirs, files in os.walk(directory):
    for file in files:
        # Формируем полный путь к файлу
        filepath = os.path.join(root, file)

        # Получаем время последнего изменения файла
        filetime = os.path.getmtime(filepath)

        # Форматируем время в нужном формате
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        # Получаем размер файла
        filesize = os.path.getsize(filepath)

        # Получаем родительскую директорию
        parent_dir = os.path.dirname(filepath)

        # Выводим информацию о файле
        #print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
         #     f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

# Вывод на консоль:
# => Обнаружен файл: pythonw.exe, Путь: .\.venv\Scripts\pythonw.exe, Размер: 258840 байт, Время изменения: 10.10.2024 10:51,
# Родительская директория: .\.venv\Scripts