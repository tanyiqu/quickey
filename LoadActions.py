import R
from Action import Action
import subprocess
from PyQt5.QtWidgets import QMessageBox
import keyboard


def loadActions():
    print('loading actions')
    for action_item in R.Actions:
        loadActionItem(action_item)
        pass

    pass


def loadActionItem(action_item: Action):
    # print(action_item)
    if action_item.type == 1:
        loadActionItem1(action_item)
    elif action_item.type == 2:
        loadActionItem2(action_item)
    elif action_item.type == 3:
        loadActionItem3(action_item)
    pass

# 运行程序或打开文件


def loadActionItem1(action_item: Action):
    keyboard.add_hotkey(action_item.shortcut,
                        lambda: runFile(action_item.target))
    pass


def loadActionItem2(action_item: Action):
    # subprocess.Popen('start cmd /k', shell=True)
    keyboard.add_hotkey(action_item.shortcut,
                        lambda: subprocess.Popen(action_item.target, shell=True))
    pass


def loadActionItem3(action_item: Action):
    pass


def runFile(file_path):
    print('运行文件：', file_path)
    try:
        subprocess.Popen(file_path)
        pass
    except OSError:
        # raise OSError
        # message_box = QMessageBox()
        # message_box.setWindowTitle("错误")

        # errMessage = "快捷指令错误\n快捷操作：%s\n快捷键：%s\n错误原因：指定的文件不存在" % (
        #     action_item.name, action_item.shortcut)

        # message_box.setText(errMessage)
        # message_box.setIcon(QMessageBox.Critical)
        # response = message_box.exec_()
        pass
    pass
