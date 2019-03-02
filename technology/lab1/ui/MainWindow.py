#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QWidget

from ui.DrawArea import DrawArea
from ui.MenuBar import MenuBar
from ui.SideBar import SideBar


class MainWindow(QMainWindow):
    numChanged = pyqtSignal()
    figureChanged = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._active = None
        self.setWindowIcon(QIcon('Icons\Window.ico'))
        self._num = 3
        self.border_color = QColor(0, 0, 0)
        self.bg_color = QColor(250, 15, 15)
        self.menubar = MenuBar(self)
        self.sidebar = SideBar(self)
        self.draw_area = DrawArea(self)

        self.init_widgets()

    def get_num(self):
        return self._num

    def set_num(self, number):
        if self._num != number:
            self._num = number
            self.numChanged.emit()

    def get_active(self):
        return self._active

    def set_active(self, value):
        if self._active != value:
            self._active = value
            self.figureChanged.emit()


    def init_widgets(self):
        self.setWindowTitle('Paint')
        self.setGeometry(150, 100, 900, 600)
        self.setFixedSize(self.size())

        self.sidebar.resize(self.width(), 50)
        self.sidebar.move(0, self.menubar.height())

        self.draw_area.move(0, 50 + self.menubar.height())
        self.draw_area.resize(self.size())

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
