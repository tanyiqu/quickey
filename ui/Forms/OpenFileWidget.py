from PyQt5.QtWidgets import QWidget

from ui.Forms.pyuic.Ui_OpenFileWidget import Ui_OpenFileWidget
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QKeySequenceEdit, QVBoxLayout
from PyQt5.QtGui import QKeySequence


class OpenFileWidget(QWidget):
    def __init__(self, parent=None):

        # super(OpenFileWidget, self).__init__(parent)

        super().__init__()
        self.parent = parent

        # super().__init__(parent)
        self.mainWidget = Ui_OpenFileWidget()
        self.mainWidget.setupUi(self)

        # 创建一个QKeySequenceEdit对象，并将其与QLineEdit对象关联
        keyedit = QKeySequenceEdit(self)
        keyedit.setKeySequence(QKeySequence())
        keyedit.keySequenceChanged.connect(self.onKeySequenceChanged)
        keyedit.setParent(self.mainWidget.lineEdit_2)

        pass

    def onKeySequenceChanged(self, keyseq):
        # 将用户输入的快捷键作为文本填入QLineEdit对象
        text = keyseq.toString()
        self.mainWidget.lineEdit_2.setText(text)

    pass
