#from PyQt5.QtGui import *
#from PyQt5.QtCore import *
from PyQt5.QtWidgets import QListView

import logging

log = logging.getLogger(__name__)

class MangaView(QListView):
    ''' 列表list view '''
    def __init__(self, parent=None):
        super(MangaView, self).__init__()
        log.debug('本子展示区初始化')
