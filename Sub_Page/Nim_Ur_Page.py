from typing import List
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QListWidget
from MainWindow_UI import Ui_MainWindow
from PyQt5.QtWidgets import *
import data_process as dp

 # 0 : create window
 # 1 : refresh
def nimportant_urgent_page_ui(self):
    nimportant_urgent_page = QtWidgets.QWidget()
    nimportant_urgent_page.setObjectName("nimportant_urgent_page")

    listwidget = QListWidget(nimportant_urgent_page)
    listwidget.setGeometry(QtCore.QRect(4, 5, 530, 600))

    dp.get_display_data(listwidget, 0, 1)
    
    self.stackedWidget.addWidget(nimportant_urgent_page)
