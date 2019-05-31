import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout


class AppWindow(QMainWindow):
    '''main window'''

    def __init__(self):
        super(AppWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
