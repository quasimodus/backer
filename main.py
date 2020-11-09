# -*- coding: utf-8 -*-
import os
import sys
import time
import zipfile

from PyQt5 import QtCore, QtGui, QtWidgets
from ui_backer import Ui_Dialog


# from to_arhiv import *
# from to_arhiv import arhivator


class CurrencyConv(QtWidgets.QDialog):

    def __init__(self):
        super(CurrencyConv, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle("backer_tool")
        self.ui.toolButton_1.clicked.connect(self.get_source)
        self.ui.toolButton_2.clicked.connect(self.get_target)
        self.ui.pushButton_1.clicked.connect(self.arhivator)

    def get_source(self):
        # input_currency = self.ui.lineEdit.text()
        # # output_currency = self.ui.output_currency.text()
        # p = check_ping(input_currency)

        source = QtWidgets.QFileDialog.getExistingDirectory()
        self.ui.lineEdit_1.setText(source)
        # print("Путь к файлу : " + wb_patch)

        # source = QtWidgets.QFileDialog.getExistingDirectory()
        # target_dir = "D:\\_____BACKUP"
        print('source run')
        return source

    def get_target(self):
        # input_currency = self.ui.lineEdit.text()
        # # output_currency = self.ui.output_currency.text()
        # p = check_ping(input_currency)

        target_dir = QtWidgets.QFileDialog.getExistingDirectory()
        self.ui.lineEdit_2.setText(target_dir)
        # print("Путь к файлу : " + wb_patch)

        # target_dir = QtWidgets.QFileDialog.getExistingDirectory()
        # target_dir = "D:\\_____BACKUP"

        print('target run')
        return target_dir

    # source = "D:\\test"
    # target_dir = "D:\\_____BACKUP"

    def arhivator(self):

        if not os.path.exists(self.get_target()):
            os.mkdir(self.get_target())  # создание каталога
            print('Каталог успешно создан', self.get_target())

        today = self.get_target() + os.sep + time.strftime('%Y%m%d')

        now = time.strftime('%H%M%S')

        target = today + os.sep + now + '.zip'

        if not os.path.exists(today):
            os.mkdir(today)  # создание каталога
            print('Каталог успешно создан', today)
        mode = zipfile.ZIP_DEFLATED
        zipp = zipfile.ZipFile(target, 'w', mode)  # создание архива
        for root, dirs, files in os.walk(self.get_source()):  # получаем адрес каталога и имена подкатологов и файлов
            for file in files:
                zipp.write(os.path.join(root, file))  # пишем файлы в архив

        zipp.close()
        print(self.get_target() + '\n' + self.get_source())


app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()

sys.exit(app.exec())
