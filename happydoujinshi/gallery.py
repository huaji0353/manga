from PyQt5.QtGui import QPainter, QColor 
from PyQt5.QtCore import Qt, QDir, QModelIndex, QAbstractTableModel, QPointF, QPoint, QSize
from PyQt5.QtWidgets import (QTableView, QFileSystemModel, QStyledItemDelegate)

from .res import *

import logging

log = logging.getLogger(__name__)

# 单元格子paint图片
class GridDelegate(QStyledItemDelegate):
    ''' table grid delegate '''
    def __init__(self, app, parent):
        super().__init__(parent)

    # def paint(self, painter, option, index):
    #     assert isinstance(painter, QPainter)
    #     rec = option.rect.getRect()
    #     x = rec[0]
    #     y = rec[1]
    #     w = rec[2]
    #     h = rec[3]
    #     gallery = index.data(Qt.UserRole)
    #     #painter.setPen(QColor(164,164,164,200))
    #     #painter.drawLine(QPointF(x-10,y-10),QPointF(x+w,y+h))
    #     painter.drawImage((x+w//2),(y+h//2),gallery)

    def sizeHint(self, option, index):
        # 重设大小
        return QSize(140, 200)

# 表table模型gallery
class MangaModel(QAbstractTableModel):
    ''' model table 
        cover
    '''
    def __init__(self, data, parent=None):
        super().__init__(parent)

        self._data = []
        for row in range(1,5):
            for col in range(1,4):
                if row % 2:
                    self._data.append(c_png)
                else:
                    self._data.append(bw_png)

    def data(self, index, role=Qt.DisplayRole):
        # 根据index与role输入获取数据

        _row = index.row()
        _gallery = self._data[_row]
        _column = index.column()

        return _gallery

    def rowCount(self, index=QModelIndex()):
        # 有多少行
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        # 有多少列
        return 6

    # def headerData(self, section, orientation, role=Qt.DisplayRole):
    #     # 数据表头
    #     if orientation == Qt.Horizontal:


# 表view
class MangaTableView(QTableView):
    ''' view '''
    def __init__(self, parent=None):
        super().__init__(parent)
        #self.setShowGrid(False)

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
        self.view.setItemDelegate(self.delegate)

    def show(self):
        log.debug('show()')
        self.view.show()