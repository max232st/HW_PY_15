import os
import logging
from collections import namedtuple

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])


def directory_info(directory_path):
    logging.basicConfig(filename='directory_info.log', level=logging.INFO)

    if not os.path.isdir(directory_path):
        logging.error("Указанный путь не является директорией")
        return

    file_info_list = []
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        name, extension = os.path.splitext(item)
        is_directory = os.path.isdir(item_path)
        parent_directory = os.path.basename(directory_path)
        file_info = FileInfo(name, extension, is_directory, parent_directory)
        file_info_list.append(file_info)

        logging.info(
            f"Файл: {item_path}, Расширение: {extension}, Флаг каталога: {is_directory}, Родительский каталог: \n"
            f"{parent_directory}"
        )

    with open('directory_info.txt', 'w') as file:
        for file_info in file_info_list:
            file.write(
                f"Имя файла: {file_info.name}, Расширение: {file_info.extension}, "
                f"Флаг каталога: {file_info.is_directory}, Родительский каталог: {file_info.parent_directory}\n"
            )


if __name__ == "__main__":
    directory_info(r'D:\pythonDZ')
