# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
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
        self.ui.toolButton.clicked.connect(self.get_puth)
        self.ui.toolButton_2.clicked.connect(self.get_puth)
        self.ui.toolButton_3.clicked.connect(self.get_puth)

    def get_puth(self):
        # input_currency = self.ui.lineEdit.text()
        # # output_currency = self.ui.output_currency.text()
        # p = check_ping(input_currency)
        # self.ui.textEdit.setText(p)

        wb_patch = QtWidgets.QFileDialog.getOpenFileName()[0]
        print(wb_patch)


app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()

sys.exit(app.exec())

