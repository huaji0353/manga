import sys
from PyQt5.QtWidgets import QApplication
from .app import AppWindow

app = QApplication([])

# main app window
appwin = AppWindow()
appwin.show()

# close app when user closes window
sys.exit(app.exec_())