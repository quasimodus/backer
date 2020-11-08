# -*- coding: utf-8 -*-
import sys
import time
import zipfile

from ui_backer import Ui_Dialog
from to_arhiv import *


class CurrencyConv(QtWidgets.QDialog):

    def __init__(self):
        super(CurrencyConv, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle("backer_tool")
        self.ui.toolButton_1.clicked.connect(self.get_source)

    def get_source(self):
        # input_currency = self.ui.lineEdit.text()
        # # output_currency = self.ui.output_currency.text()
        # p = check_ping(input_currency)

        source = QtWidgets.QFileDialog.getExistingDirectory()
        self.ui.lineEdit_1.setText(source)
        # print("Путь к файлу : " + wb_patch)
        # source = "C:\\TEST_1C\\1C\\"

        target_dir = 'D:\\__BACKUP__'

        if not os.path.exists(target_dir):
            os.mkdir(target_dir)  # создание каталога
            print('Каталог успешно создан', target_dir)

        today = target_dir + os.sep + time.strftime('%Y%m%d')
        now = time.strftime('%H%M%S')
        target = today + os.sep + now + '.zip'

        if not os.path.exists(today):
            os.mkdir(today)  # создание каталога
            print('Каталог успешно создан', today)
        mode = zipfile.ZIP_DEFLATED
        zipp = zipfile.ZipFile(target, 'w', mode)  # создание архива
        for root, dirs, files in os.walk(source):  # получаем адрес каталога и имена подкатологов и файлов
            for file in files:
                zipp.write(os.path.join(root, file))  # пишем файлы в архив

        zipp.close()


app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()

sys.exit(app.exec())
