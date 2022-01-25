from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow_UI import Ui_MainWindow
from Sub_Page import Im_Ur_Page as imurp
from Sub_Page import Im_Nur_Page as imnurp
from Sub_Page import Nim_Ur_Page as nimurp
from Sub_Page import Nim_Nur_Page as nimnurp
from Sub_Page import Chart_Page as cp
from Sub_Page import Instructions_Page as ip
import data_process as dp
import sys

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow_controller, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        imurp.important_urgent_page_ui(self.ui)
        imnurp.important_nurgent_page_ui(self.ui)
        nimurp.nimportant_urgent_page_ui(self.ui)
        nimnurp.nimportant_nurgent_page_ui(self.ui)
        cp.chart_page_ui(self.ui)
        ip.instructions_page_ui(self.ui)
        self.setup_control()

    # def setup_each_ui():
        
    def setup_control(self):
        # print("+")
        # TODO
        self.ui.im_ur_but.clicked.connect(self.frameController)
        self.ui.im_nur_but.clicked.connect(self.frameController)
        self.ui.nim_ur_but.clicked.connect(self.frameController)
        self.ui.nim_nur_but.clicked.connect(self.frameController)
        self.ui.analysis_but.clicked.connect(self.frameController)
        self.ui.instructions_but.clicked.connect(self.frameController)
        self.ui.stackedWidget.setCurrentIndex(0)
        # self.ui.refresh_but.clicked.connect(self.refreshController)

    def frameController(self):
        sender = self.sender().objectName() # 獲取當前信號 sender
        index = {
        "im_ur_but": 0,
        "im_nur_but": 1,
        "nim_ur_but": 2,
        "nim_nur_but": 3,
        "analysis_but": 4,
        "instructions_but": 5,
        }
        self.ui.stackedWidget.setCurrentIndex(index[sender]) # 根據信號 index 設置所顯示的頁面

'''
    def refreshController(self):
        dp.get_display_data(Ui_MainWindow.stackedWidget.widget(0).listWidget, 1, 1)
'''
'''
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)

    window.show()
    sys.exit(app.exec_())
'''