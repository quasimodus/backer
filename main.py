# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_backer import Ui_Dialog
# from to_arhiv import *
from to_arhiv import arhivator


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

    def get_source(self):
        # input_currency = self.ui.lineEdit.text()
        # # output_currency = self.ui.output_currency.text()
        # p = check_ping(input_currency)

        source = QtWidgets.QFileDialog.getExistingDirectory()
        self.ui.lineEdit_1.setText(source)
        # print("Путь к файлу : " + wb_patch)

        # target_dir = QtWidgets.QFileDialog.getExistingDirectory()
        target_dir = "D:\\_____BACKUP"
        return source

    def get_target(self):
        # input_currency = self.ui.lineEdit.text()
        # # output_currency = self.ui.output_currency.text()
        # p = check_ping(input_currency)

        target_dir = QtWidgets.QFileDialog.getExistingDirectory()
        self.ui.lineEdit_1.setText(target_dir)
        # print("Путь к файлу : " + wb_patch)

        # target_dir = QtWidgets.QFileDialog.getExistingDirectory()
        # target_dir = "D:\\_____BACKUP"
        return target_dir

    arhivator(get_source, get_target) # не работает тут


app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()

sys.exit(app.exec())
