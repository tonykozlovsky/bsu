#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QInputDialog, QAction, QColorDialog
from PyQt5.QtWidgets import QWidget

from src import *

class MenuBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.menu_items = {}
        self.menuBar = self.parent.menuBar()

        self.menu_items['Choose figure'] = self.menuBar.addMenu("&Choose figure")
        self.menu_items['Settings'] = self.menuBar.addMenu("&Settings")

        self.figures_actions = self.get_figures_menu_items()
        for figure in self.figures_actions:
            self.menu_items['Choose figure'].addAction(figure)

        self.settings_actions = self.get_settings_menu_items()
        for setting in self.settings_actions:
            self.menu_items['Settings'].addAction(setting)

        self.parent.active = None

    def get_settings_menu_items(self):
        border = QAction(QIcon('Icons\LineSegment.png'), "&Set border color", self)
        border.triggered.connect(lambda: self.color_picker('Set border color'))

        bg = QAction(QIcon('Icons\Line.png'), "&Set background color", self)
        bg.triggered.connect(lambda: self.color_picker('Set background color'))

        num_of_points = QAction(QIcon('Icons\Line.png'), "&Number of figure points", self)
        num_of_points.triggered.connect(lambda: self.show_dialog(self.parent.active))

        return [border, bg, num_of_points]

    def get_figures_menu_items(self):
        segment = QAction(QIcon('Icons\LineSegment.png'),"&Line segment", self)
        segment.triggered.connect(lambda: self.on_select(LineSegment.name()))

        line = QAction(QIcon('Icons\Line.png'),"&Line", self)
        line.triggered.connect(lambda: self.on_select(Line.name()))

        ray = QAction(QIcon('Icons\Ray.png'),"&Ray", self)
        ray.triggered.connect(lambda: self.on_select(Ray.name()))

        polyline = QAction(QIcon('Icons\Polyline.png'),"&Polyline", self)
        polyline.triggered.connect(lambda: self.on_select(PolyLine.name()))

        asym = QAction(QIcon('Icons\AsymmetricShape.png'),"&Asymmetric shape", self)
        asym.triggered.connect(lambda: self.on_select(AsymmetricShape.name()))

        reg = QAction(QIcon('Icons\RegularShape.png'),"&Regular shape", self)
        reg.triggered.connect(lambda: self.on_select(RegularShape.name()))

        sym = QAction(QIcon('Icons\SymmetricShape.png'),"&Symmetric shape", self)
        sym.triggered.connect(lambda: self.on_select(SymmetricShape.name()))

        circle = QAction(QIcon('Icons\Circle.png'), "&Circle", self)
        circle.triggered.connect(lambda: self.on_select(Circle.name()))

        ellipse = QAction(QIcon('Icons\Ellipse.png'),"&Ellipse", self)
        ellipse.triggered.connect(lambda: self.on_select(Ellipse.name()))

        return [segment, ray, line, polyline, asym, reg, sym, circle, ellipse]

    def color_picker(self, setting):
        color = QColorDialog().getColor()
        if setting == 'Set border color':
            self.parent.border_color = color
        elif setting == 'Set background color':
            self.parent.bg_color = color
        print(color)

    def on_select(self, figure_name):
        self.parent.set_active(figure_name)
        self.show_dialog(figure_name)

    def show_dialog(self, active_name):
        ok, min, step = False, 3, 1
        if active_name in [PolyLine.name(), AsymmetricShape.name(), RegularShape.name(), SymmetricShape.name()]:
            if active_name == SymmetricShape.name():
                min, step = 4, 2
            num, ok = QInputDialog.getInt(self, 'Set number of points', 'Enter a number of figure points', min=min, step=step)
        if not ok:
            num = 3
        self.parent.set_num(num)

    def height(self):
        return self.menuBar.height()
