from PyQt5.QtGui import QPainter, QColor 
from PyQt5.QtCore import Qt, QDir, QModelIndex, QAbstractTableModel, QPointF, QPoint, QSize, QRectF
from PyQt5.QtWidgets import (QTableView, QListView, QFileSystemModel, QStyledItemDelegate)

from .res import *

import logging

log = logging.getLogger(__name__)

class Manga:
    def __init__(self, name = None, picobj = None):
        self.name = name
        self.picobj = picobj

# 单元格子paint图片
class GridDelegate(QStyledItemDelegate):
    ''' table grid delegate '''
    def __init__(self, app, parent):
        super().__init__(parent)

    def paint(self, painter, option, index):
        rec = option.rect.getRect()
        x = rec[0]
        y = rec[1]
        w = rec[2]
        h = rec[3]
        gallery = index.data(Qt.UserRole)
        #painter.setPen(QColor(164,164,164,200))
        painter.drawImage(QRectF(x,y,w,h),gallery.picobj)
        #painter.drawLine(QPointF(x,y),QPointF(x+w,y+h))

    def sizeHint(self, option, index):
        # 重设大小
        return QSize(140, 200)

# 表table模型gallery
class MangaModel(QAbstractTableModel):
    ''' model table 
        cover
    '''
    def __init__(self, view, parent=None):
        super().__init__(parent)
        self.view = view
        self._data = []

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
        return 1

    def appendRow(self, item):
        self._data.append(item)
        self.view.update()
        

    # def headerData(self, section, orientation, role=Qt.DisplayRole):
    #     # 数据表头
    #     if orientation == Qt.Horizontal:


# 表view
class MangaTableView(QListView):
    ''' view '''
    def __init__(self, parent=None):
        super().__init__(parent)
        #self.setShowGrid(False)
        self.setViewMode(self.IconMode)
        self.setResizeMode(self.Adjust)

        self.setWrapping(True)
        self.setSpacing(10)
        
        self.setIconSize(QSize(W_png,H_png))
        self.setFlow(self.LeftToRight)

        def print_clicked(a):
            print(f'{a.data(Qt.UserRole + 1).name}')

        self.clicked.connect(print_clicked)
        #self.update()

    

class MangaView:
    def __init__(self, parent):        
        self.view = MangaTableView(parent)
        self.model = MangaModel(self.view)
        self.delegate = GridDelegate(parent, self.view)

        parent.layout.addWidget(self.view)

        log.debug('本子展示区被父窗口layout')

        self.view.setModel(self.model)
        self.view.setSelectionRectVisible(True)
        self.view.setItemDelegate(self.delegate)

        self.getimamge()

    def getimamge(self):
        for i in range(22):
            if i %2 :
                self.model.appendRow(Manga('c_png',c_png))
            else:
                self.model.appendRow(Manga('bw_png',bw_png))

    def show(self):
        log.debug('show()')
        self.view.show()