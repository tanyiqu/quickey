from textwrap import indent
import R
from Action import Action
import subprocess
from PyQt5.QtWidgets import QMessageBox
import keyboard
import time


def loadActions():
    print('loading actions')
    for action_item in R.Actions:
        loadActionItem(action_item)
        pass

    # 处理双击按键事件
    deal_double_click()
    pass


# 按下快捷键组合
def loadActionItemshortcutType1(action_item: Action):

    # 运行程序或打开文件
    if action_item.type == 1:
        keyboard.add_hotkey(action_item.shortcut,
                            lambda: runFile(action_item.target))
    # 执行命令
    elif action_item.type == 2:
        keyboard.add_hotkey(action_item.shortcut,
                            lambda: subprocess.Popen(action_item.target, shell=True))
        pass
    pass


double_clicks_count = 0
double_clicks_action = []
double_clicks = []
last_click_time = None
last_click_key = None


# 双击某按键
def loadActionItemshortcutType2(action_item: Action):
    # 将按键添加至按键数组中
    global double_clicks
    global double_clicks_action
    action_item.shortcut = action_item.shortcut.lower()
    double_clicks.append(action_item.shortcut)
    double_clicks_action.append(action_item)
    pass


def loadActionItem(action_item: Action):
    # if action_item.type == 1:
    #     loadActionItem1(action_item)
    # elif action_item.type == 2:
    #     loadActionItem2(action_item)

    if action_item.shortcut_type == 1:
        loadActionItemshortcutType1(action_item)
    elif action_item.shortcut_type == 2:
        loadActionItemshortcutType2(action_item)

    pass

# 运行程序或打开文件


def deal_double_click():
    global double_clicks
    print(double_clicks)

    keyboard.on_press(on_press)
    pass


# 键盘点击事件
def on_press(event):
    global double_clicks_count
    global double_clicks
    global double_clicks_action
    global last_click_time
    global last_click_key

    current_key = ''
    # 判断按下的按键是否在数组列表中
    if event.name not in double_clicks:
        return

    # 获取按下的快捷键的数组下标
    index = double_clicks.index(event.name)
    print(index)

    current_key = event.name
    current_time = time.time()

    if double_clicks_count == 0:
        last_click_key = current_key
        last_click_time = current_time
        pass

    double_clicks_count += 1

    if double_clicks_count >= 2 and current_time - last_click_time < 1 and current_key == last_click_key:
        print('double', current_key)
        # 执行对应的操作
        # loadActionItemshortcutType1(double_clicks_action[index])
        action_item = double_clicks_action[index]
        # 运行程序或打开文件
        if action_item.type == 1:
            runFile(action_item.target)
        # 执行命令
        elif action_item.type == 2:
            subprocess.Popen(action_item.target, shell=True)
        pass

        # 重置计数器
        double_clicks_count = 0
        last_click_time = None
        last_click_key = None
        pass

    # 其他特殊情况，重置计数器
    elif double_clicks_count >= 2:
        double_clicks_count = 0
        last_click_time = None
        last_click_key = None

    return

    # 如果按下了某键s
    if event.name == action_item.shortcut.lower():
        print('按下', action_item.shortcut.lower(),
              'double_clicks_count', double_clicks_count)
        # print()
        # 获取当前时间戳
        current_time = time.time()
        # 如果是第一次按下 Ctrl 键，则更新 last_ctrl_time 的值
        if double_clicks_count == 0:
            last_click_time = current_time
        # 计数器加 1
        double_clicks_count += 1
        # 如果计数器为 2，则表示连续按下了两次键
        if double_clicks_count >= 2 and current_time - last_click_time < 1:
            # 执行相应操作
            subprocess.Popen(
                action_item.target, shell=True)
            # 重置计数器和 last_ctrl_time 的值
            double_clicks_count = 0
            last_click_time = None
        # 其他特殊情况，重置计数器
        elif double_clicks_count >= 2:
            double_clicks_count = 0
            last_click_time = None
    else:
        # 如果没有按下 Ctrl 键，则将计数器重置为 0，并将 last_ctrl_time 设置为 None
        double_clicks_count = 0
        last_click_time = None


# 运行程序或打开文件
# def loadActionItem1(action_item: Action):
#     # 判断款快捷键类型
#     if action_item.shortcut_type == 1:
#         keyboard.add_hotkey(action_item.shortcut,
#                             lambda: runFile(action_item.target))
#         pass
#     elif action_item.shortcut_type == 2:
#         keyboard.on_press(
#             lambda event, arg=action_item: on_press(event, arg))
#         pass
#     pass


# 执行命令
# def loadActionItem2(action_item: Action):
#     # subprocess.Popen('start cmd /k', shell=True)
#     keyboard.add_hotkey(action_item.shortcut,
#                         lambda: subprocess.Popen(action_item.target, shell=True))
#     pass


# 运行文件
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
