import sys
from PyQt5.QtWidgets import QApplication
from .app import AppWindow

import logging

log_handlers = []
log_handlers.append(logging.StreamHandler())
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)-8s %(levelname)-6s %(name)-6s %(message)s',
                datefmt='%d-%m %H:%M',
                handlers=tuple(log_handlers))

app = QApplication([])

# main app window
appwin = AppWindow()
appwin.show()

# close app when user closes window
sys.exit(app.exec_())