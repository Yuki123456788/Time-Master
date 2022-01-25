from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import QChart, QChartView, QValueAxis, QBarCategoryAxis, QBarSet, QBarSeries
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPainter
from numpy import fabs
import pyqtgraph as pg
import json
import time
import data_process as dp

def day_page_ui(self):
    day_tab = QtWidgets.QWidget()
    day_tab.setObjectName("day_tab")
    self.addTab(day_tab, "")
    self.setTabText(self.indexOf(day_tab),"Day")

    pg.setConfigOptions(leftButtonPan=False, background='w') 
    plot=pg.plot()
    # plot.setRange(yRange=[0, 24])

    # create list for y-axis
    y1 = dp.get_total_data(0)
    # create horizontal list i.e x-axis
    x = [1, 2, 3, 4]
    x_label = [(1, 'im_ur'), (2, 'im_nur'), (3, 'nim_ur'), (4, 'nim_nur')]

    # create pyqt5graph bar graph item
    # with width = 0.6
    # with bar colors = green
    bargraph = pg.BarGraphItem(x = x, height = y1, width = 0.6, labels=x_label, brush ='r')
    ax=plot.getAxis('bottom')
    ax.setTicks([x_label])

    # add item to plot window
    # adding bargraph item to the plot window
    plot.addItem(bargraph)
    # layout=QtWidgets.QVBoxLayout()
    # layout.addWidget(plot)
    # day_tab.setLayout(layout)
    layout=QtWidgets.QGridLayout()
    day_tab.setLayout(layout)

    layout.addWidget(plot, 0, 0, 3, 1)