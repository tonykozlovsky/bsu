#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QPen
from PyQt5.QtWidgets import QWidget

from src import *


class DrawArea(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setToolTip('This is a Draw Area!')
        self.points = []
        self.figures = []
        self.last_point = None
        self.drawling = False
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_points(qp)
        self.draw_figures(qp)
        qp.end()

    def draw_points(self, qp):
        pen = QPen(Qt.red)
        pen.setCapStyle(Qt.RoundCap)
        pen.setWidth(5)
        qp.setPen(pen)

        for point in self.points:
            qp.drawPoint(point)

    def draw_figures(self, qp):
        for fig in self.figures:
            fig.render(qp)

    def mousePressEvent(self, event):
        if self.parent.get_active() == None:
            return

        border_color = self.parent.border_color
        bg_color = self.parent.bg_color

        if not self.drawling:
            self.points = []
            self.update()
            self.drawling = True

        self.points.append(event.pos())
        if len(self.points) > 2 and self.parent.get_active() == PolyLine.name():
            if len(self.points) <= self.parent.get_num():
                self.figures[-1].add_segment(LineSegment(self.points[-2], self.points[-1], border_color))
            if len(self.points) == self.parent.get_num():
                self.drawling = False
        elif (len(self.points) - 1) * 2 == self.parent.get_num():
            if self.parent.get_active() == SymmetricShape.name():
                self.figures.append(
                    SymmetricShape(self.points[0], self.points[1:], self.parent.get_num(), border_color, bg_color))
            else:
                self.update()
                return
            self.drawling = False
        elif len(self.points) == 2:
            if self.parent.get_active() == LineSegment.name():
                self.figures.append(LineSegment(*self.points, border_color))
            elif self.parent.get_active() == Ray.name():
                self.figures.append(Ray(*self.points, border_color))
            elif self.parent.get_active() == Line.name():
                self.figures.append(Line(*self.points, self.geometry(), border_color))
            elif self.parent.get_active() == Circle.name():
                self.figures.append(Circle(*self.points, border_color, bg_color))
            elif self.parent.get_active() == RegularShape.name():
                self.figures.append(
                    RegularShape(self.points[0], [self.points[1]], self.parent.get_num(), border_color, bg_color))
            elif self.parent.get_active() == PolyLine.name():
                self.figures.append(PolyLine([LineSegment(*self.points, border_color)]))
                self.update()
                return
            else:
                self.update()
                return
            self.drawling = False
        elif len(self.points) == 3:
            if self.parent.get_active() == Ellipse.name():
                self.figures.append(Ellipse(*self.points, border_color, bg_color))
            else:
                self.update()
                return
            self.drawling = False
        if len(self.points) >= self.parent.get_num():
            if self.parent.get_active() == AsymmetricShape.name():
                self.figures.append(AsymmetricShape(self.points, border_color, bg_color))
            else:
                self.update()
                return
            self.drawling = False

        self.update()
