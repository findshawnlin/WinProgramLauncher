import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import subprocess

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.sub_buttons_main = []  # 存储主按钮下的子按钮的列表
        self.sub_buttons_main2 = []  # 存储主按钮2下的子按钮的列表
        self.is_main_button_expanded = False  # 记录主按钮的展开状态
        self.is_main_button2_expanded = False  # 记录主按钮2的展开状态
        self.initUI()

    # 初始化界面
    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('PyQt5 示例')

        # 创建主按钮并连接槽函数
        self.main_button = QPushButton(self)
        self.setupButton(self.main_button, '主按钮', self.toggleSubButtonsMain, '#4CAF50')  # 绿色

        # 创建主按钮2并连接槽函数
        self.main_button2 = QPushButton(self)
        self.setupButton(self.main_button2, '主按钮2', self.toggleSubButtonsMain2, '#2196F3')  # 蓝色

        # 创建垂直布局
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.main_button)  # 将主按钮添加到布局中
        self.vbox.addWidget(self.main_button2)  # 将主按钮2添加到布局中

        # 设置布局
        self.setLayout(self.vbox)

    # 设置按钮属性和样式
    def setupButton(self, button, text, slot, color):
        button.setText(text)
        button.setIcon(QIcon('icon.png'))  # 请替换 'icon.png' 为你的图标文件路径
        button.setIconSize(button.sizeHint() / 2)
        button.clicked.connect(slot)

        # 设置按钮样式
        button.setStyleSheet(f'''
            QPushButton {{
                background-color: {color};
                color: white;
                border: 2px solid {color};
                border-radius: 5px;
                padding: 5px;
                margin: 2px;
                text-align: center;
                font-size: 12px;
            }}

            QPushButton:hover {{
                background-color: #1E88E5; /* 深蓝色 */
            }}
        ''')

    # 切换主按钮下的子按钮的显示状态
    def toggleSubButtonsMain(self):
        if not self.is_main_button_expanded:
            self.showSubButtonsMain()
        else:
            self.hideSubButtonsMain()

    # 切换主按钮2下的子按钮的显示状态
    def toggleSubButtonsMain2(self):
        if not self.is_main_button2_expanded:
            self.showSubButtonsMain2()
        else:
            self.hideSubButtonsMain2()

    # 显示主按钮下的子按钮
    def showSubButtonsMain(self):
        # 移除所有按钮
        self.clearButtons()

        # 创建四个子按钮并连接槽函数
        sub_button1 = QPushButton(self)
        self.setupButton(sub_button1, '子按钮1', lambda: self.openExecutable('path/to/executable1'), '#FFC107')  # 黄色

        sub_button2 = QPushButton(self)
        self.setupButton(sub_button2, '子按钮2', lambda: self.openExecutable('path/to/executable2'), '#FF5722')  # 橙色

        sub_button3 = QPushButton(self)
        self.setupButton(sub_button3, '子按钮3', lambda: self.openExecutable('path/to/executable3'), '#E91E63')  # 粉红色

        sub_button4 = QPushButton(self)
        self.setupButton(sub_button4, '子按钮4', lambda: self.openExecutable('path/to/executable4'), '#795548')  # 棕色

        # 将子按钮添加到列表中，方便后续管理
        self.sub_buttons_main.extend([sub_button1, sub_button2, sub_button3, sub_button4])

        # 将所有按钮重新添加到布局中
        self.addButtons()

        # 更新展开状态
        self.is_main_button_expanded = True

    # 显示主按钮2下的子按钮
    def showSubButtonsMain2(self):
        # 移除所有按钮
        self.clearButtons()

        # 创建一个子按钮并连接槽函数
        sub_button_main2 = QPushButton(self)
        self.setupButton(sub_button_main2, '主按钮2下的子按钮', lambda: self.openExecutable('path/to/executable_main2'), '#9C27B0')  # 紫色

        # 创建另一个子按钮
        sub_button2 = QPushButton(self)
        self.setupButton(sub_button2, '额外的子按钮1', lambda: self.openExecutable("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"), '#009688')  # 青色

        sub_button3 = QPushButton(self)
        self.setupButton(sub_button3, '额外的子按钮2', lambda: self.openExecutable("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"), '#607D8B')  # 灰色

        # 将子按钮添加到列表中，方便后续管理
        self.sub_buttons_main2.extend([sub_button_main2, sub_button2, sub_button3])

        # 将所有按钮重新添加到布局中
        self.addButtons()

        # 更新展开状态
        self.is_main_button2_expanded = True

    # 隐藏主按钮下的子按钮
    def hideSubButtonsMain(self):
        for sub_button in reversed(self.sub_buttons_main):
            sub_button.hide()

        # 更新展开状态
        self.is_main_button_expanded = False

    # 隐藏主按钮2下的子按钮
    def hideSubButtonsMain2(self):
        for sub_button in reversed(self.sub_buttons_main2):
            sub_button.hide()

        # 更新展开状态
        self.is_main_button2_expanded = False

    # 清除所有按钮
    def clearButtons(self):
        for sub_button in self.sub_buttons_main + self.sub_buttons_main2:
            sub_button.setParent(None)

    # 将所有按钮重新添加到布局中
    def addButtons(self):
        # 获取主按钮的索引
        main_button_index = self.vbox.indexOf(self.main_button)

        # 添加主按钮下的子按钮
        for sub_button in self.sub_buttons_main:
            main_button_index += 1
            self.vbox.insertWidget(main_button_index, sub_button)

        # 获取主按钮2的索引
        main_button2_index = self.vbox.indexOf(self.main_button2)

        # 添加主按钮2下的子按钮
        for sub_button in self.sub_buttons_main2:
            main_button2_index += 1
            self.vbox.insertWidget(main_button2_index, sub_button)

    # 打开可执行文件
    def openExecutable(self, executable_path):
        try:
            subprocess.Popen([executable_path])
        except Exception as e:
            print(f"Error opening executable: {e}")

# 主程序入口
if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_widget = MyWidget()
    my_widget.show()
    sys.exit(app.exec_())
