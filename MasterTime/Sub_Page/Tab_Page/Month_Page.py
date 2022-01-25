from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import QChart, QChartView, QValueAxis, QBarCategoryAxis, QBarSet, QBarSeries
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPainter
from numpy import fabs
import pyqtgraph as pg
import numpy as np
import json
import time
import data_process as dp

def month_page_ui(self):
    month_tab = QtWidgets.QWidget()
    month_tab.setObjectName("month_tab")
    self.addTab(month_tab, "")
    self.setTabText(self.indexOf(month_tab),"Month")

    pg.setConfigOptions(leftButtonPan=False, background='w')

    plot_month=pg.plot()
    # plot_month.setRange(yRange=[0, 24])

    y = dp.get_specific_data(2)

    x_w = np.arange(4)
    x_w_label = [(0, 'Week1'), (1, 'Week2'), (2, 'Week3'), (3, 'Week4')]

    im_ur_bar = pg.BarGraphItem(x = x_w-0.3, height = y[0], width = 0.2, labels=x_w_label, brush ='r')
    im_nur_bar = pg.BarGraphItem(x = x_w-0.1, height = y[1], width = 0.2, labels=x_w_label, brush ='g')
    nim_ur_bar = pg.BarGraphItem(x = x_w+0.1, height = y[2], width = 0.2, labels=x_w_label, brush ='b')
    nim_nur_bar = pg.BarGraphItem(x = x_w+0.3, height = y[3], width = 0.2, labels=x_w_label, brush ='y')

    ax=plot_month.getAxis('bottom')
    ax.setTicks([x_w_label])

    # add item to plot window
    # adding bargraph item to the plot window
    plot_month.addItem(im_ur_bar)
    plot_month.addItem(im_nur_bar)
    plot_month.addItem(nim_ur_bar)
    plot_month.addItem(nim_nur_bar)
# ---------------------------------------------------
    plot_total=pg.plot()
    # create list for y-axis
    y_t = dp.get_total_data(2)

    # create horizontal list i.e x-axis
    x_t = [1, 2, 3, 4]
    x_t_label = [(1, 'im_ur'), (2, 'im_nur'), (3, 'nim_ur'), (4, 'nim_nur')]

    # create pyqt5graph bar graph item
    # with width = 0.6
    bargraph = pg.BarGraphItem(x = x_t, height = y_t, width = 0.6, labels=x_t_label, brush ='r')
    ax=plot_total.getAxis('bottom')
    ax.setTicks([x_t_label])

    # add item to plot window
    # adding bargraph item to the plot window
    plot_total.addItem(bargraph)


    layout=QtWidgets.QVBoxLayout()
    layout.addWidget(plot_month)
    layout.addWidget(plot_total)
    month_tab.setLayout(layout)