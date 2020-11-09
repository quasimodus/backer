# coding:utf8
# создание архива директории  с помощью модуля zipfile
# --------------------------------------------------------------------

import os
import time
import zipfile
import zlib


# def arhivator(source, target_dir):
#     # source = "C:\\TEST_1C\\1C\\"
#     #
#     # target_dir = 'E:\\BACKUP'  # Подставьте тот путь, который вы будете использовать.
#
#     if not os.path.exists(target_dir):
#         os.mkdir(target_dir)  # создание каталога
#         print('Каталог успешно создан', target_dir)
#
#     today = target_dir + os.sep + time.strftime('%Y%m%d')
#
#     now = time.strftime('%H%M%S')
#
#     target = today + os.sep + now + '.zip'
#
#     if not os.path.exists(today):
#         os.mkdir(today)  # создание каталога
#         print('Каталог успешно создан', today)
#     mode = zipfile.ZIP_DEFLATED
#     zipp = zipfile.ZipFile(target, 'w', mode)  # создание архива
#     for root, dirs, files in os.walk(source):  # получаем адрес каталога и имена подкатологов и файлов
#         for file in files:
#             zipp.write(os.path.join(root, file))  # пишем файлы в архив
#
#     zipp.close()
