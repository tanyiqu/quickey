
from re import S
from PyQt5.QtWidgets import QWidget
from ui.Forms.Ui_MainForm import Ui_Form
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QPoint, QRectF
from PyQt5.QtGui import QMouseEvent, QColor, QPainter, QPainterPath, QBrush

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction, QWidget


class MainForm(QWidget):
    # 在此定义变量

    def __init__(self, parent=None):
        # super().__init__()
        super(MainForm, self).__init__(parent)
        self.mainForm = Ui_Form()
        self.mainForm.setupUi(self)
        self.border_width = 8
        # 初始化外观
        self.init_appearance()
        # 功能操作
        self.init_func()
        # self.resize(300,300)

        # 创建系统托盘对象
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon('resource/imgs/b.png'))
        self.tray_icon.setToolTip('My Application')

        # 创建右键菜单
        self.menu = QMenu(self)
        show_action = QAction('显示窗口', self)
        show_action.triggered.connect(self.show_window)
        quit_action = QAction('退出', self)
        quit_action.triggered.connect(lambda: exit(0))
        self.menu.addAction(show_action)
        self.menu.addAction(quit_action)

        # 将右键菜单设置为托盘对象的菜单
        self.tray_icon.setContextMenu(self.menu)

        # 将窗口隐藏到系统托盘中
        self.hide()
        self.tray_icon.show()

        pass

    def show_window(self):
        """将窗口从系统托盘中恢复并显示在屏幕上"""
        self.showNormal()
        self.activateWindow()

    # 设置窗口样式
    def init_appearance(self):
        # 设置窗口无边框
        # self.setAttribute(Qt.WA_TranslucentBackground)
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)

        pass

    # 设置窗口的功能
    def init_func(self):

        # 实现窗口拖动
        self.set_move()

        pass

    # ##### 实现窗口拖动  ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    _startPos = None
    _endPos = None
    _isTracking = False

    def set_move(self):
        # self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框
        self.show()

    def mouseMoveEvent(self, e: QMouseEvent):
        if (self._startPos is None) or (e.pos() is None):
            return
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None

    # ##### 实现窗口拖动  ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

    pass
