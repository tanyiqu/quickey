from PyQt5.QtWidgets import QMessageBox
import json
import R
from Action import Action



def loadConfig():
    print('loading config')
    CONFIG_PATH = 'userdata/config.json'
    data = ''
    try:
        with open(CONFIG_PATH, 'r', encoding='utf8') as f:
            data = json.load(f)
    except FileNotFoundError:
        message_box = QMessageBox()
        message_box.setWindowTitle("错误")
        message_box.setText("配置文件不存在！")
        message_box.setIcon(QMessageBox.Critical)
        response = message_box.exec_()
        exit(response)
    for action_dict in data['actions']:
        R.Actions.append(Action(action_dict))
        pass

    pass
