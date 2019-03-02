#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QColorDialog, QButtonGroup
from PyQt5.QtWidgets import QPushButton


class PictureRadioButton(QPushButton):
    colorChanged = pyqtSignal()
    figureWasSelected = pyqtSignal()

    selectedFigure = None
    buttonGroup = QButtonGroup()

    nextId = 0

    def __init__(self, *args, **kwargs):
        super(PictureRadioButton, self).__init__(*args, **kwargs)
        self.id = PictureRadioButton.nextId

        PictureRadioButton.buttonGroup.addButton(self)
        self.setCheckable(True)
        self.pressed.connect(self.onSelect)
        PictureRadioButton.nextId += 1

    def onSelect(self):
        self.setChecked(True)
        PictureRadioButton.selectedFigure = self.text
        self.figureWasSelected.emit()

    def setPictureIcon(self, qIcon):
        self.setIcon(qIcon)

    def setText(self, name):
        self.text = name

    def setBackground(self, color):
        self.setStyleSheet("background-color: " + color)
        # p.setColor(self.backgroundRole(), color)
        #self.setPalette(p)
        #self.setAutoFillBackground(True)

    @staticmethod
    def setActiveButton(name):
        for figure in PictureRadioButton.buttonGroup.buttons():
            if figure.text == name:
                figure.onSelect()
                break
