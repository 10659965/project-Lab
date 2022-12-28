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


class Graph(QWidget):

    def __init__(self):
        super(Graph, self).__init__()

        self.graphWidget = pg.PlotWidget()
        

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
        
        self.stop_btn = QPushButton(
            text="Stop",
            clicked=self.stopTimer
        )
        self.reset_btn = QPushButton(
            text="Reset",
            clicked=self.resetTimer
        )

        button_hlay = QHBoxLayout()
        
        #button_hlay.addWidget(self.start_btn)
        button_hlay.addWidget(self.stop_btn)
        button_hlay.addWidget(self.reset_btn)
        vlay = QVBoxLayout()
        vlay.addLayout(button_hlay)
        vlay.addWidget(self.graphWidget)
        #widget = QWidget()
        self.setLayout(vlay)
        

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
        #self.start_btn.setDisabled(True)

    def resetTimer(self):
        self.count = 0
        text_timer = str(self.count) + ' s'
        self.timelabel.setText(text_timer)
        self.start = False
        #self.start_btn.setDisabled(False)
    '''
    def draw(self):
        """!
        @brief Draw the plots.
        """
        self.acc = self.plot(self.graphWidget, self.hour, self.acceleration, 'Acceleration', 'r')
    '''

    def clicked(self, qmodelindex):
        item = self.listwidget.currentItem()
        print(item.text())

'''
app = QApplication(sys.argv)

demo = Graph()
demo.show()

sys.exit(app.exec_())
'''
