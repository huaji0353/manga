#from PyQt5.QtGui import *
#from PyQt5.QtCore import *
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout,
                             QLabel, QPushButton)

from .plugins.language_CN import *

from .gallery import MangaView

import logging
log = logging.getLogger(__name__)

class AppWindow(QWidget):
    '''main window'''

    def __init__(self):
        super(AppWindow, self).__init__()
        self.initUI()

    def initUI(self):
        # 主窗口layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        log.debug('主窗体布局设定完成')

        # 放菜单控件，设置layout
        memu = QWidget()
        memu_layout = QHBoxLayout()
        memu.setLayout(memu_layout)
        log.debug('菜单布局设定完成')
        self.layout.addWidget(memu)

        label = QLabel(test)
        # 测试标签
        memu_layout.addWidget(label)

        self.btn = QPushButton(test)
        # 测试退出按钮
        memu_layout.addWidget(self.btn)
        self.btn.clicked.connect(lambda:print('btn1 按下'))

        # 放画廊的listview
        self.view = MangaView()
        self.layout.addWidget(self.view)
        
        log.debug('主窗体初始化')