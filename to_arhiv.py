import os
import tkinter
from PyQt5 import QtCore, QtGui, QtWidgets


def check_ping(hostname, status=None):
    if not hostname:
        status = 'Введите адрес хоста в поле слева'
        return status

    else:
        # hostname = "8.8.8.8"
        response = os.system("ping -n 1 " + hostname)

        if response == 0:
            print(hostname, ' - Хост доступен!')
            status = hostname + ' -- доступен!'
        else:
            print(hostname, '  Хост не доступен!')
            status = hostname + ' -- не доступен!'

        return status
