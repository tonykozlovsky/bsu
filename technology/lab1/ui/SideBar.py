#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import QInputDialog, QHBoxLayout, QSpinBox
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

from src import *
from ui.PictureRadioButton import PictureRadioButton
from ui.QColorButton import QColorButton


class SideBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.set_bg_color(QColor('lightgray'))
        self.figures = self.get_buttons()

        for figure in self.figures:
            figure.figureWasSelected.connect(self.setActiveFigure)

        self.num_spin = QSpinBox()
        self.num_spin.setValue(self.parent.get_num())
        self.num_spin.valueChanged.connect(self.num_changed)
        self.num_spin.setMinimum(3)
        self.parent.numChanged.connect(self.num_changed_from_parent)

        self.border_color_btn = QColorButton()
        self.border_color_btn.colorChanged.connect(lambda: self.colorChanged('Border color'))
        self.bg_color_btn = QColorButton()
        self.bg_color_btn.colorChanged.connect(lambda: self.colorChanged('Backgound color'))
        self.parent.figureChanged.connect(self.setSideBarFigure)

        self.render_buttons()
        self.show()

    def setSideBarFigure(self):
        PictureRadioButton.setActiveButton(self.parent.get_active())

    def setActiveFigure(self):
        if PictureRadioButton.selectedFigure != self.parent.get_active():
            print(PictureRadioButton.selectedFigure)
            self.parent.set_active(PictureRadioButton.selectedFigure)

    def num_changed(self):
        if self.num_spin.value() != self.parent.get_num():
            self.parent.set_num(self.num_spin.value())

    def num_changed_from_parent(self):
        if self.num_spin.value() != self.parent.get_num():
            self.num_spin.setValue(self.parent.get_num())

    def colorChanged(self, setting):
        if setting == 'Border color':
            self.parent.border_color = self.border_color_btn.color()
        elif setting == 'Backgound color':
            self.parent.bg_color = self.bg_color_btn.color()


    @staticmethod
    def get_buttons():
        segment = PictureRadioButton();
        segment.setText('Line Segment')
        segment.setPictureIcon(QIcon('Icons\LineSegment.png'))

        line = PictureRadioButton();
        line.setText('Line')
        line.setPictureIcon(QIcon('Icons\Line.png'))

        ray = PictureRadioButton();
        ray.setText('Ray')
        ray.setPictureIcon(QIcon('Icons\Ray.png'))

        polyline = PictureRadioButton();
        polyline.setText('Poly Line')
        polyline.setPictureIcon(QIcon('Icons\Polyline.png'))

        asym = PictureRadioButton();
        asym.setText('Asymmetric Shape')
        asym.setPictureIcon(QIcon('Icons\AsymmetricShape.png'))

        reg = PictureRadioButton();
        reg.setText('Regular Shape')
        reg.setPictureIcon(QIcon('Icons\RegularShape.png'))

        sym = PictureRadioButton();
        sym.setText('Symmetric Shape')
        sym.setPictureIcon(QIcon('Icons\SymmetricShape.png'))

        circle = PictureRadioButton();
        circle.setText('Circle')
        circle.setPictureIcon(QIcon('Icons\Circle.png'))

        ellipse = PictureRadioButton();
        ellipse.setText('Ellipse')
        ellipse.setPictureIcon(QIcon('Icons\Ellipse.png'))

        return [segment, ray, line, polyline, asym, reg, sym, circle, ellipse]

    def render_buttons(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(5, 0, 5, 0)
        layout.setSpacing(0)


        for figure in self.figures:
            figure.setBackground('lightgray')
            layout.addWidget(figure)

        layout.addStretch(0)
        layout.addWidget(QLabel('  Set number of figure points:  ', self))
        layout.addWidget(self.num_spin)
        layout.addWidget(QLabel('  Border color:  ', self))
        layout.addWidget(self.border_color_btn)
        layout.addWidget(QLabel('  Background color:  ', self))
        layout.addWidget(self.bg_color_btn)

        self.setLayout(layout)

    def on_select(self, btn):
        if btn.isChecked():
            self.show_dialog(btn.text())
            self.parent.set_active(btn.text())

    def set_bg_color(self, color):
        p = self.palette()
        p.setColor(self.backgroundRole(), color)
        self.setPalette(p)
        self.setAutoFillBackground(True)

    def show_dialog(self, active_name):
        ok, min, step = False, 3, 1
        if active_name in [PolyLine.name(), AsymmetricShape.name(), RegularShape.name(), SymmetricShape.name()]:
            if active_name == SymmetricShape.name():
                min, step = 4, 2
            num, ok = QInputDialog.getInt(self, 'points dialog', 'enter a number of points', min=min, step=step)
        if not ok:
            num = 3
        self.parent.set_num(num)
        self.num_spin.setValue(num)
