from PyQt5.QtWidgets import QMessageBox

class Action(object):
    def __init__(self):
        pass

    def __init__(self, dict):
        """使用字典构造"""

        try:
            self.name = dict['name']
            self.type = dict['type']
            self.shortcut = dict['shortcut']
            self.shortcut_type = dict['shortcut_type']
            self.desc = dict['desc']
            self.target = dict['target']
        except KeyError:
            message_box = QMessageBox()
            message_box.setWindowTitle("错误")
            message_box.setText("配置文件异常，请检查配置文件的内容！")
            message_box.setIcon(QMessageBox.Critical)
            response = message_box.exec_()
            exit(response)
            pass
        pass