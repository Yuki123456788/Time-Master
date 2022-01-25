from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
#  from MainWindow_UI import Ui_MainWindow
from Sub_Page.Tab_Page import Day_Page as dp
from Sub_Page.Tab_Page import Week_Page as wp
from Sub_Page.Tab_Page import Month_Page as mp
from Sub_Page.Tab_Page import Year_Page as yp

def chart_page_ui(self):
    chart_page = QtWidgets.QWidget()
    chart_page.setObjectName("chart_page")

    tabWidget = QtWidgets.QTabWidget(chart_page)
    tabWidget.setGeometry(QtCore.QRect(10, 20, 521, 571))
    tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
    tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
    tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
    tabWidget.setElideMode(QtCore.Qt.ElideRight)
    tabWidget.setMovable(False)
    tabWidget.setTabBarAutoHide(False)
    tabWidget.setObjectName("tabWidget")

    # setup tab_page
    dp.day_page_ui(tabWidget)
    wp.week_page_ui(tabWidget)
    mp.month_page_ui(tabWidget)
    yp.year_page_ui(tabWidget)

    self.stackedWidget.addWidget(chart_page)

    tabWidget.setCurrentIndex(0)