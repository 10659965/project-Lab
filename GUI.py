import numpy as np
from PyQt5.QtCore import QTime, QTimer, QDateTime
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QListWidget, QGridLayout, QLabel

# ser = serial.Serial('/dev/ttyUSB0') # open serial port

#sono stati inseriti momentaneamente valori casuali
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


#PLOT
# We import library dedicated to data plot
import sys

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QWidget, QMessageBox, QLabel

)

from PyQt5.QtCore import QTimer
import pyqtgraph as pg
from pyqtgraph import PlotWidget

###############
# MAIN WINDOW #
###############

class MWd(QMainWindow):
    def __init__(self):
        """!
        @brief Init MainWindow.
        """
        super(MWd, self).__init__()

        # title and geometry
        self.setWindowTitle("GUI")
        width = 200
        height = 160
        self.setMinimumSize(width, height)

        self.initUI()

        # VISUALIZZA STEPS

        pybutton = QLabel('The number of Steps is:', self)
        pybutton1 = QLabel(steps, self)
        pybutton.resize(170, 40)
        pybutton1.resize(50, 40)
        pybutton.move(50, 50)
        pybutton1.move(210, 50)

        # TIMER

        self.start = False
        self.count = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.showTimer)  # collega timer a showTimer


        pybutton2 = QLabel('Timer:', self)
        self.timelabel = QLabel('', self)  #label per visualizzare il tempo
        pybutton2.resize(70, 40)
        self.timelabel.resize(50, 40)
        pybutton2.move(500, 50)
        self.timelabel.move(560, 50)

    def stopTimer(self):
        self.timer.stop()
        self.start = False
        self.start_btn.setDisabled(False)

    def showTimer(self):
        if self.start:
            self.count += 0.1

        if self.start:
            text = str(round(self.count, 2)) + ' s'
            self.timelabel.setText(text)

    def startTimer(self):
        self.start = True
        self.timer.start(100)
        self.start_btn.setDisabled(True)

    def resetTimer(self):
        self.count = 0
        text = str(self.count) + ' s'
        self.timelabel.setText(text)
        self.start = False
        self.start_btn.setDisabled(False)


    #####################
    # GRAPHIC INTERFACE #
    #####################
    def initUI(self):
        """!
        @brief Set up the graphical interface structure.
        """
        # Create the plot widget (crea bottoni)

        self.graphWidget = PlotWidget()
        # Define buttons
        self.clear_btn = QPushButton(
            text="Clear",
            clicked=self.graphWidget.clear # .clear() is a method of the PlotWidget class
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

        # layout
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

        # lettura dati
        self.hour = [1, 2, 3, 4, 5, 6, 7, 8] #cambiare con ongi quanto viene rilevato il dato
        self.acceleration = a


        # Plot settings
        # Add grid
        self.graphWidget.showGrid(x=True, y=True)
        # Set background color
        self.graphWidget.setBackground('w')
        # Add title
        self.graphWidget.setTitle("Acceleration measurement")
        # Add axis labels
        styles = {'color': 'k', 'font-size': '15px'}
        self.graphWidget.setLabel('left', 'Acceleration [g]', **styles)
        self.graphWidget.setLabel('bottom', 'Time [sec]', **styles)
        # Add legend
        self.graphWidget.addLegend()

        # Plot data: x, y values
        self.draw()


    def draw(self):
        """!
        @brief Draw the plots.
        """
        self.acc = self.plot(self.graphWidget, self.hour, self.acceleration, 'Acceleration', 'r')


    def plot(self, graph, x, y, curve_name, color):
        """!
        @brief Draw graph.
        """
        pen = pg.mkPen(color=color)
        line = graph.plot(x, y, name=curve_name, pen=pen)
        return line



    #############
    #  RUN APP  #
    #############

if __name__ == '__main__':
        app = QApplication(sys.argv)
        w = MWd()
        w.show()
        sys.exit(app.exec_())