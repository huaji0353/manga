from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

from .plugins.language_CN import *

from .gallery import MangaView

class AppWindow(QWidget):
    '''main window'''

    def __init__(self):
        super(AppWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel(about)
        self.layout.addWidget(self.label)