# manga
read &amp; mgr your manga in online/download/offline , it was implement by pyqt5

启发与大量代码来自happypanda, thanks

# 开发
UI（带日志跟踪）：展示本子的list和图片画廊table控件，带菜单的主窗口

MVC模型：<todo>

网络栈：浏览器客户端，爬虫

插件模块：解析用的插件，UI的语言设定

风格自定义：对app的参数进行解耦

more？：抄更多happypanda的代码过来 拿来解耦拆模块
decouples happypanda code 轻量化更易开发与diy

# mvc
delegate=控制器 view model
将数据存储的方式与呈现给用户的方式分开，但是基于相同的原则提供了一个更简单的框架。
这种分离使得在几个不同的视图中显示相同的数据成为可能，并且在不改变底层数据结构的情况下实现新的视图类型。
为了允许灵活地处理用户输入，我们引入了委托的概念。在此框架中拥有委托的好处是，它允许定制呈现和编辑数据项的方式。

通常控制器负责从视图读取数据，控制用户输入，并向模型发送数据。

M=C=V M和C无关，不需要注册任何消息

http://www.omegaxyz.com/2019/03/03/pyqt5_mvc/

## 思考
QTableView 显示表
QAbstractTableModel 模型类



# pyqt5 debug
def dbg():
    qtcore
    pyqtRemoveInputHook()
    __import__('pdb').set_trace()
    pyqtRestoreInputHook()

## 相关
happypanda

https://github.com/RicterZ/nhentai/