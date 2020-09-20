## Title: UI.py
## Name : UI
## @author : Rahul Manna
## Created on : 2020-09-06 20:53:11
## Description : 

import sys
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber, QGridLayout

class calculator_UI(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400,500)
        self.setWindowTitle("Calculator - ManR")
        self.setWindowIcon(QtGui.QIcon("./icon.png"))

        self.initUI()
        self.show()

    def initUI(self):
        self.b0 = QPushButton("0")
        self.b1 = QPushButton("1")
        self.b2 = QPushButton("2")
        self.b3 = QPushButton("3")
        self.b4 = QPushButton("4")
        self.b5 = QPushButton("5")
        self.b6 = QPushButton("6")
        self.b7 = QPushButton("7")
        self.b8 = QPushButton("8")
        self.b9 = QPushButton("9")
        self.b_equal = QPushButton("=")
        self.b_dot = QPushButton(".")
        self.b_div = QPushButton("÷")
        self.b_mul = QPushButton("×")
        self.b_sub = QPushButton("−")
        self.b_add = QPushButton("+")
        self.b_percent = QPushButton("%")
        self.b_clr = QPushButton("Clr")

        self.lcd = QLCDNumber()
        #self.lcd.setNumDigits(9)

        self.all_buttons = [self.b0, self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9, 
                        self.b_equal, self.b_dot, self.b_div, self.b_mul, self.b_sub, self.b_add, self.b_percent, self.b_clr]
        
        for btn in self.all_buttons:
            btn.setSizePolicy(QtWidgets.QSizePolicy.Preferred,QtWidgets.QSizePolicy.Preferred)

        #Layout

        self.grid = QGridLayout()
        self.grid.addWidget(self.lcd,0,0,2,4)
        self.grid.addWidget(self.b_clr,2,0,1,1)
        self.grid.addWidget(self.b_percent,2,1,1,1)
        self.grid.addWidget(self.b_div,2,2,1,1)
        self.grid.addWidget(self.b_mul,2,3,1,1)
        self.grid.addWidget(self.b7,3,0,1,1)
        self.grid.addWidget(self.b8,3,1,1,1)
        self.grid.addWidget(self.b9,3,2,1,1)
        self.grid.addWidget(self.b_sub,3,3,1,1)
        self.grid.addWidget(self.b4,4,0,1,1)
        self.grid.addWidget(self.b5,4,1,1,1)
        self.grid.addWidget(self.b6,4,2,1,1)
        self.grid.addWidget(self.b_add,4,3,1,1)
        self.grid.addWidget(self.b1,5,0,1,1)
        self.grid.addWidget(self.b2,5,1,1,1)
        self.grid.addWidget(self.b3,5,2,1,1)
        self.grid.addWidget(self.b_equal,5,3,2,1)
        self.grid.addWidget(self.b0,6,0,1,2)
        self.grid.addWidget(self.b_dot,6,2,1,1)

        self.grid.setSpacing(12)

        self.setLayout(self.grid)

        #Stylesheet

        self.b_add.setObjectName("operator")
        self.b_sub.setObjectName("operator")
        self.b_mul.setObjectName("operator")
        self.b_div.setObjectName("operator")
        self.b_percent.setObjectName("operator")

        self.b_equal.setObjectName("equal")
        self.b_clr.setObjectName("clear")
        with open("style.qss","r") as f:
            self.setStyleSheet(f.read())