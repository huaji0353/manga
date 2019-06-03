import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow

from PyQt5.QtGui import QPainter, QColor,QPixmap
from PyQt5.QtCore import Qt, QDir, QModelIndex, QAbstractTableModel, QPointF, QPoint, QSize, QRectF
from PyQt5.QtWidgets import (QTableView, QListView, QFileSystemModel, QStyledItemDelegate)

import requests
from bs4 import BeautifulSoup

import threading
from queue import Queue

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

class Manga:
    def __init__(self, name=None, picobj=None):
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
        # painter.setPen(QColor(164,164,164,200))
        painter.drawPixmap(x,y ,140, 200, gallery.picobj)
        # painter.drawLine(QPointF(x,y),QPointF(x+w,y+h))

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

class Appwin(QMainWindow, Ui_MainWindow):

    picget = pyqtSignal()

    def __init__(self, parent=None):
        super(Appwin, self).__init__(parent)
        self.setupUi(self)
        self.lineEdit.setText('http://list.pptv.com/category/type_3_sort_score_area_8_ft_2.html')

        self.initlistview()
        self.initmvc()

    def getnetpic(self, l):
        pic = QPixmap()
        pic.loadFromData(requests.get(l[1], headers=headers).content)
        self.model.appendRow(Manga(l[0], pic))

    def getpic(self):
        reqs = requests.get(self.lineEdit.text(), headers=headers)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        list = []
        for li in soup.find_all('li'):
            try:
                name = li.a.attrs['title']
                picurl = li.a.p.img.attrs['data-src2']
                list.append((name, picurl))
            except:
                pass
        list = list[:28]
        for l in list:
            t = threading.Thread(target=self.getnetpic, args=(l,))
            t.start()
        self.lineEdit.clear()

    def initlistview(self):
        self.listView.setViewMode(self.listView.IconMode)
        self.listView.setResizeMode(self.listView.Adjust)
        self.listView.setSpacing(10)
        self.listView.setFlow(self.listView.LeftToRight)

        def print_clicked(a):
            print(f'{a.data(Qt.UserRole + 1).name}')

        self.listView.clicked.connect(print_clicked)

    def initmvc(self):
        self.model = MangaModel(self.listView)
        self.delegate = GridDelegate(self, self.listView)

        self.listView.setModel(self.model)
        self.listView.setItemDelegate(self.delegate)

if __name__ == "__main__":
    app = QApplication([])

    appwin = Appwin()
    appwin.show()

    sys.exit(app.exec_())
