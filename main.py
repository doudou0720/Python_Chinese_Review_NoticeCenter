import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer,QDateTime ,Qt
from Notice_ui import Ui_MainWindow

screen_height = 0
screen_width = 0
is_open=True
is_processing = False
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.init()
        
        # 初始化各种功能
    def init(self):
        global screen_height,screen_width
        # 创建一个QTimer对象
        self.send_time = QTimer(self)
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        screen_height = self.screenRect.height()
        screen_width = self.screenRect.width()
        self.setGeometry(screen_width,0,250,350)
        # self.pushButton_start.clicked.connect(self.beginShowTime)
        self.send_time.start(100)
        # 给QTimer设定一个时间，每到达这个时间一次就会调用一次该方法
        self.send_time.timeout.connect(self.showTime)

    '''方法实现区'''

    # 显示时间的方法
    def showTime(self):
        global screen_width,is_open,is_processing
        # 获取系统当前时间
        time_get = QDateTime.currentDateTime()
        # 设置系统时间的显示格式
        time_get = (time_get.toString('hh:mm:ss')).split(":")
        hour = int(time_get[0])
        minute = int(time_get[1])
        second = int(time_get[2])
        # 在标签上显示时间
        self.h.display(hour)
        self.m.display(minute)
        self.s.display(second)
        if is_open and not is_processing:
            is_processing = True
            for i in range(500):
                self.setGeometry(screen_width-(i//2)-1,0,250,350)
            is_open = False
            is_processing = False
        if self.time_left.value() <= 0 :
            if not is_processing:
                is_processing = True
                for i in range(500):
                    self.setGeometry(screen_width+(i//2)+1-250,0,250,350)
                is_processing = False
                self.close()
        else:
            self.time_left.setValue(self.time_left.value() - 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
