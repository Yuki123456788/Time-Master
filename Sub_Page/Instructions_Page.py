from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from MainWindow_UI import Ui_MainWindow

def instructions_page_ui(self):
    instructions_page = QtWidgets.QWidget()
    instructions_page.setObjectName("instructions_page")

    instructions_label = QtWidgets.QLabel(instructions_page)
    instructions_label.setGeometry(QtCore.QRect(40, 60, 400, 200))
    instructions_label.setObjectName("instructions_label")

    instructions_label.setText("Time Master 是一個能幫你把待辦事項分類\n讓你知道現在做什麼事最恰當的簡易程式\n\n執行 Main2.py 來 ”新增事項“ 或 “計時做一件事”\n執行 start.py 來看事項分類跟統計圖表的UI介面")
    self.stackedWidget.addWidget(instructions_page)
