from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtWidgets import *
import sys

from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
from PyQt5.QtCore import QTimer
import numpy as np
from random import randint
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QTabWidget, \
                            QGridLayout, QVBoxLayout

# dati
ax = [2, 4, 7, 6, 2, 0, -4, -5]
ay = [1, 0, -1, 0, 0, -1, 1, 0]
az = [1, 2, 3, 2, 0, -1, -2, 0]

ax_sq = np.square(ax)
ay_sq = np.square(ay)
az_sq = np.square(az)

a = np.sqrt(ax_sq + ay_sq + az_sq)
l = len(a)
print("Acceleration array:", a)
print("The length of the array is:", l)

thr = 7 #soglia settata basandomi sul grafico. i picchi inizio passo e fine passo raggiungono 8g.
count = 0
for i in range(0, l):
    if a[i] >= thr:
        count += 1
steps = str(count /2)

print("number of peaks:", count)
print("number of steps:", steps)

# dati da inserire in lista



class Graph(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(Graph, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        # PULSANTI
        label_steps = QLabel('The number of Steps is:', self)
        label_steps_text = QLabel(steps, self)
        label_steps.resize(170, 40)
        label_steps_text.resize(50, 40)
        label_steps.move(50, 25)
        label_steps_text.move(210, 25)

        self.start = False
        self.count = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.showTimer)  # collega timer a showTimer

        label_timer = QLabel('Timer:', self)
        self.timelabel = QLabel('', self)  # label per visualizzare il tempo
        label_timer.resize(70, 40)
        self.timelabel.resize(50, 40)
        label_timer.move(500, 25)
        self.timelabel.move(560, 25)

        self.graphWidget = PlotWidget()

        # Define buttons
        self.clear_btn = QPushButton(
            text="Clear",
            clicked=self.graphWidget.clear  # .clear() is a method of the PlotWidget class
        )
        self.draw_btn = QPushButton(
            text="Draw",
            clicked=self.draw
        )
        self.start_btn = QPushButton(
            text="Start",
            clicked=self.startTimer
        )
        self.stop_btn = QPushButton(
            text="Stop",
            clicked=self.stopTimer
        )
        self.reset_btn = QPushButton(
            text="Reset",
            clicked=self.resetTimer
        )

        button_hlay = QHBoxLayout()
        button_hlay.addWidget(self.clear_btn)
        button_hlay.addWidget(self.draw_btn)
        button_hlay.addWidget(self.start_btn)
        button_hlay.addWidget(self.stop_btn)
        button_hlay.addWidget(self.reset_btn)
        vlay = QVBoxLayout()
        vlay.addLayout(button_hlay)
        vlay.addWidget(self.graphWidget)
        widget = QWidget()
        widget.setLayout(vlay)
        self.setCentralWidget(widget)

        # plot settings
        self.graphWidget.showGrid(x=True, y=True)
        self.graphWidget.setBackground('w')
        self.graphWidget.setTitle("Acceleration measurement")
        # Add axis labels
        styles = {'color': 'k', 'font-size': '15px'}
        self.graphWidget.setLabel('left', 'Acceleration [g]', **styles)
        self.graphWidget.setLabel('bottom', 'Time [sec]', **styles)
        self.graphWidget.addLegend()

        # grafico dati

        self.hour = list(range(8))  # 100 time points
        self.acceleration = a

        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line = self.graphWidget.plot(self.hour, self.acceleration, pen=pen)
        self.timer = QtCore.QTimer()

        # def update_plot_data(self):

        # self.hour = self.hour[1:]  # Remove the first y element.
        # self.hour.append(self.hour[-1] + 1)  # Add a new value 1 higher than the last.

        # self.acceleration = self.acceleration[1:]  # Remove the first
        # self.acceleration.append(randint(0,8))  # Add a new random value.

        # self.data_line.setData(self.hour, self.acceleration)

    def stopTimer(self):
        self.timer.stop()
        self.start = False
        self.start_btn.setDisabled(False)

    def showTimer(self):
        if self.start:
            self.count += 0.1

        if self.start:
            text_timer = str(round(self.count, 2)) + ' s'
            self.timelabel.setText(text_timer)

    def startTimer(self):
        self.start = True
        self.timer.start(100)
        self.start_btn.setDisabled(True)

    def resetTimer(self):
        self.count = 0
        text_timer = str(self.count) + ' s'
        self.timelabel.setText(text_timer)
        self.start = False
        self.start_btn.setDisabled(False)

    def draw(self):
        """!
        @brief Draw the plots.
        """
        self.acc = self.plot(self.graphWidget, self.hour, self.acceleration, 'Acceleration', 'r')

    def clicked(self, qmodelindex):
        item = self.listwidget.currentItem()
        print(item.text())


class List_Acquisitions(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()

        self.setLayout(layout)
        self.listwidget = QListWidget()
        self.listwidget.insertItem(0, "Red")
        self.listwidget.insertItem(1, "Orange")
        self.listwidget.insertItem(2, "Blue")
        self.listwidget.insertItem(3, "White")
        self.listwidget.insertItem(4, "Green")
        # self.listwidget.setMaximumSize(50, 50)
        # self.listwidget.setMaximumSize(100, 100)
        self.listwidget.clicked.connect(self.clicked)
        layout.addWidget(self.listwidget)

    def clicked(self, qmodelindex):
        item = self.listwidget.currentItem()
        print(item.text())


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1440, 810)

        mainLayout = QGridLayout()
        vLayout = QVBoxLayout()
        self.setWindowTitle("GUI")

        # TAb 1
        self.tab_1 = QWidget()
        self.tab_1.layout = QVBoxLayout()
        # self.tab_1.setMaximumSize(50, 50)
        # self.tab_1.setMaximumSize(100, 100)
        # self.tab_1.layout.addWidget(QLabel('<font size+8><b>List of past acquisitions </font'))

        self.list = List_Acquisitions()

        self.tab_1.layout.addWidget(self.list)

        self.tab_1.setLayout(self.tab_1.layout)
        #self.tab_1.resize(20, 810)

        self.tabs1 = QTabWidget()
        self.tabs1.addTab(self.tab_1, 'List of past acquisitions')
        self.tabs1.setMaximumSize(250, 810)
        self.tabs1.setMinimumSize(250, 750)

        # tab 2

        self.tab_2 = QWidget()
        self.tab_2.layout = QVBoxLayout()

        self.graph = Graph()

        self.tab_2.layout.addWidget(self.graph)
        self.tab_2.setLayout(self.tab_2.layout)
        # self.tab_2.resize(150, 250)

        self.tabs2 = QTabWidget()
        self.tabs2.addTab(self.tab_2, 'Graph ')


        mainLayout.addWidget(self.tabs1, 0, 0)
        mainLayout.addWidget(self.tabs2, 0, 1) #1 serve per mettere in colonne diverse
        self.setLayout(mainLayout)



if __name__ == '__main__':
        app = QApplication(sys.argv)

        demo = AppDemo()
        demo.show()

        sys.exit(app.exec_())