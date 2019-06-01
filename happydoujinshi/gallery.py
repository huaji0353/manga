#from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QDir, QModelIndex, QAbstractTableModel
from PyQt5.QtWidgets import QTableView, QFileSystemModel, QStyledItemDelegate

import logging

log = logging.getLogger(__name__)

# 单元格子paint图片
class GridDelegate(QStyledItemDelegate):
    ''' table grid delegate '''
    def __init__(self, app, parent):
        super().__init__(parent)

    def paint(self, painter, option, index):
        pass

# 表table模型gallery
class MangaModel(QAbstractTableModel):
    ''' model table 
        cover
    '''
    def __init__(self, data, parent=None):
        super().__init__(parent)

        self._data = data

    def data(self, index, role=Qt.DisplayRole):

        _row = index.row()
        #_gallery = self._data[_row]
        _column = index.column()

        return f'row{_row},col{_column}'

    def rowCount(self, index=QModelIndex()):
        return 8

    def columnCount(self, parent=QModelIndex()):
        return 12

# 表view
class MangaTableView(QTableView):
    ''' view '''
    def __init__(self, parent=None):
        super().__init__(parent)

    def initUI(self):
        pass

class MangaView:
    def __init__(self, parent):
        self.view = MangaTableView(parent)
        self.model = MangaModel([])
        self.delegate = GridDelegate(parent, self.view)

        parent.layout.addWidget(self.view)
        '''
        log.debug('本子展示区初始化，文件系统测试')
        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.currentPath())

        self.view.setModel(self.model)
        self.view.setRootIndex(self.model.index(QDir.currentPath()))
        '''
        self.view.setModel(self.model)
        #self.view.setItemDelegate(self.delegate)

    def show(self):
        log.debug('show()')
        self.view.show()