#from PyQt5.QtGui import *
#from PyQt5.QtCore import *
from PyQt5.QtWidgets import (QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
                             QLabel, QPushButton)

from .plugins.language_CN import *

from .gallery import MangaView

import logging
log = logging.getLogger(__name__)

class AppWindow(QMainWindow):
    '''main window'''

    def __init__(self):
        super(AppWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.center = QWidget()
        self.layout = QHBoxLayout(self.center)
        #self.layout.setSpacing(0)
        self.setCentralWidget(self.center)
        self.layout.setContentsMargins(0,0,0,0)
        # 主窗口layout
        #self.layout = QVBoxLayout()
        #self.setLayout(self.layout)
        log.debug('主窗体设定')

        '''
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
        '''
        # 放画廊的listview
        self.view = MangaView(self)
        self.view.show()

        
        log.debug('主窗体初始化')