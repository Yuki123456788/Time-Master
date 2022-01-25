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

def year_page_ui(self):
    year_tab = QtWidgets.QWidget()
    year_tab.setObjectName("year_tab")
    self.addTab(year_tab, "")
    self.setTabText(self.indexOf(year_tab),"Year")

    pg.setConfigOptions(leftButtonPan=False, background='w')

    plot_year=pg.plot()
    # plot_year.setRange(yRange=[0, 24])

    y = dp.get_specific_data(3)

    x_w = np.arange(12)
    x_w_label = [(0, 'Jan'), (1, 'Feb'), (2, 'Mar'), (3, 'Apr'), (4, 'May'), (5, 'Jun'), (6, 'Jul'), (7, 'Aug'), (8, 'Sep'), (9, 'Oct'), (10, 'Nom'), (11, 'Dec')]

    im_ur_bar = pg.BarGraphItem(x = x_w-0.3, height = y[0], width = 0.2, labels=x_w_label, brush ='r')
    im_nur_bar = pg.BarGraphItem(x = x_w-0.1, height = y[1], width = 0.2, labels=x_w_label, brush ='g')
    nim_ur_bar = pg.BarGraphItem(x = x_w+0.1, height = y[2], width = 0.2, labels=x_w_label, brush ='b')
    nim_nur_bar = pg.BarGraphItem(x = x_w+0.3, height = y[3], width = 0.2, labels=x_w_label, brush ='y')

    ax=plot_year.getAxis('bottom')
    ax.setTicks([x_w_label])

    # add item to plot window
    # adding bargraph item to the plot window
    plot_year.addItem(im_ur_bar)
    plot_year.addItem(im_nur_bar)
    plot_year.addItem(nim_ur_bar)
    plot_year.addItem(nim_nur_bar)
# ---------------------------------------------------
    plot_total=pg.plot()
    # create list for y-axis
    y_t = dp.get_total_data(3)

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
    layout.addWidget(plot_year)
    layout.addWidget(plot_total)
    year_tab.setLayout(layout)