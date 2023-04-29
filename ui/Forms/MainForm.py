from PyQt5.QtWidgets import QWidget
from ui.Forms.pyuic.Ui_MainForm import Ui_Form
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QPoint, QRectF
from PyQt5.QtGui import QMouseEvent, QColor, QPainter, QPainterPath, QBrush
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction, QWidget, QAbstractItemView, QTableWidgetItem, QHeaderView
from ui.Forms.OpenFileWidget import OpenFileWidget
import LoadConfig
import LoadActions


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
        self.tray_icon.setToolTip('quickey')

        # 创建右键菜单
        self.menu = QMenu(self)
        show_action = QAction('显示窗口', self)
        show_action.triggered.connect(self.show_window)
        quit_action = QAction('退出', self)
        quit_action.triggered.connect(lambda: exit(0))
        self.menu.addAction(show_action)
        self.menu.addAction(quit_action)

        # 点击图标显示主窗口
        self.tray_icon.activated.connect(self.onTrayActivated)

        # 将右键菜单设置为托盘对象的菜单
        self.tray_icon.setContextMenu(self.menu)

        # 将窗口隐藏到系统托盘中
        self.hide()
        self.tray_icon.show()

        self.mainTable()

        # 添加菜单
        menu = QMenu(self)
        action1 = QAction('运行程序或打开文件', self)
        action2 = QAction('执行命令', self)
        action3 = QAction('运行Python脚本', self)
        menu.addAction(action1)
        menu.addAction(action2)
        menu.addAction(action3)

        # 连接QAction对象的triggered信号到槽函数
        action1.triggered.connect(self.onAction1Clicked)
        action2.triggered.connect(self.onAction2Clicked)

        # 将菜单与按钮关联
        self.mainForm.btnAdd.setMenu(menu)

        LoadConfig.loadConfig()
        LoadActions.loadActions()
        pass

    def onAction1Clicked(self):
        self.openFileWidget = OpenFileWidget(self)
        # widget.setGeometry(100, 100, 200, 100)
        self.openFileWidget.setWindowModality(2)
        self.openFileWidget.show()

        print(1)
        pass

    def onAction2Clicked(self):
        print(2)
        pass

    def mainTable(self):
        # 设置表格
        self.mainForm.actionTable.setRowCount(1)
        self.mainForm.actionTable.setColumnCount(4)

        # 设置表头
        self.mainForm.actionTable.setHorizontalHeaderLabels(
            ['名称', '快捷键', '功能', '备注'])

        # item1 = QTableWidgetItem('Alice')
        item1 = QTableWidgetItem(
            'AliceAliceAliceAliceAliceAliceAliceAliceAliceAliceAliceAliceAliceAlice')
        item2 = QTableWidgetItem('25')
        self.mainForm.actionTable.setItem(0, 0, item1)
        self.mainForm.actionTable.setItem(0, 1, item2)

        # 设置列宽自适应
        # self.mainForm.actionTable.horizontalHeader(
        # ).setSectionResizeMode(QHeaderView.Stretch)

        # self.mainForm.actionTable.setHorizontalScrollBarPolicy(
        #     Qt.ScrollBarAlwaysOn)

        # 设置列宽自适应
        self.mainForm.actionTable.horizontalHeader(
        ).setSectionResizeMode(QHeaderView.Stretch)

        # 设置表格的最小宽度为所有列的总宽度
        # self.mainForm.actionTable.setMinimumWidth(self.mainForm.actionTable.horizontalHeader().length())

        # 启用水平滚动条
        self.mainForm.actionTable.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOn)

        # 设置表头居左
        self.mainForm.actionTable.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)

        # 不显示序号和框线
        self.mainForm.actionTable.verticalHeader().setVisible(False)
        self.mainForm.actionTable.setShowGrid(False)

        # 设置点击时选中整行
        self.mainForm.actionTable.setSelectionBehavior(
            QAbstractItemView.SelectRows)
        pass

    def show_window(self):
        """将窗口从系统托盘中恢复并显示在屏幕上"""
        self.showNormal()
        self.activateWindow()

    # 点击图标显示主窗口
    def onTrayActivated(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            if not self.isVisible():
                self.show()
        pass

    def closeEvent(self, event):
        # 将关闭事件改为最小化
        # event.ignore()
        # self.hide()
        exit()

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
