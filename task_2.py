# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.

import os
import logging
from collections import namedtuple

logging.basicConfig(filename='log.txt', level=logging.INFO)

ContentItem = namedtuple('ContentItem', ['is_directory', 'name', 'extension', 'path_dir'])

def dir_pro(dir_path):
    content = os.listdir(dir_path)
    for item in content:
        item_path = os.path.join(dir_path, item)
        is_directory = os.path.isdir(item_path)
        name, extension = os.path.splitext(item)

        content_item = ContentItem(name, extension, is_directory, dir_path)
        logging.info(content_item)

        if is_directory:
            dir_pro(item_path)


if __name__ == '__main__':

    path_dir = input('Введите путь до директории: ')

    if not os.path.isdir(path_dir):
        print('Такой директории не существует.')
    else:

        dir_pro(path_dir)