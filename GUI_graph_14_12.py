import serial
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtWidgets import *
import sys
import PyQt5
import ctypes

####graph###

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

##excel
import pandas as pd

from PyQt5.QtCore import (
    QObject,
    QThreadPool, 
    QRunnable, 
    pyqtSignal, 
    pyqtSlot
)

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QComboBox,
    QHBoxLayout,
    QWidget,
    QDialog,
    QLabel,
    QMessageBox,
    QVBoxLayout,
    
)

from class_Dati import (
    DatiSerial,
    WorkerKilled,
    DatiSignals,
    convert
)
from BTPY_class import(
    BT_search
)

thr = 300
count = 0
l = len(a)
for i in range(0, l):
    if a[i] >= thr:
        count += 1
steps = str(count /2)

print("number of peaks:", count)
print("number of steps:", steps)
    





class MainW(QMainWindow):
    def __init__(self):
        super(MainW,self).__init__()
        self.X=[]
        self.Y=[]
        self.Z=[]
        self.time=[]
        self.portname=''
        #self.FlagFirstAbort=0
        
        
        #####Graph#####
        self.graphWidget = pg.PlotWidget()
        self.graphWidget = PlotWidget()

        ####excel###
        self.n_ex=0
        
        self.setWindowTitle("classDatiTest")

        self.startAcq=QPushButton("Start Acquisition")
        self.startAcq.setDisabled(True)
        self.stopAcq=QPushButton("Stop Acquisition")
        self.stopAcq.setDisabled(True)
        self.ShowData=QPushButton("ShowData")
        self.ShowData.setDisabled(True)

        self.Dati=DatiSerial(self.portname,'Ready')
        
        self.ThreadDati=QThreadPool()

        self.searchWdiget=BT_search('Ready')

        self.searchWdiget.signalport.portname.connect(self.SetPort)
        
        self.startAcq.pressed.connect(self.StartAcquisition)
        self.stopAcq.pressed.connect(self.AbortAcquisition)
        self.ShowData.pressed.connect(self.ShowVectData)
        self.Dati.signals.service_string.connect(self.SignalThreadStr)
        self.Dati.signals.dati.connect(self.SignalDati)
        
            
        


        self.initGUI()

    
        
    
    def StartAcquisition(self):
            self.Dati=DatiSerial(str(self.portname),'Ready')
            self.Dati.signals.service_string.connect(self.SignalThreadStr)
            self.Dati.signals.dati.connect(self.SignalDati)
            
            
            self.FlagStart=True
            self.ThreadDati=QThreadPool()

            self.ThreadDati.start(self.Dati)
            self.Dati.is_killed=False
            print("iskilled:"+str(self.Dati.is_killed))
            self.startAcq.setDisabled(True)
            

    
    def AbortAcquisition(self):
        
        self.Dati.Abort()
        #self.Dati.is_killed=True
        
        #print(self.Dati.PortName)
        print("iskilled:"+str(self.Dati.is_killed))
        self.startAcq.setDisabled(False)
        #self.FlagFirstAbort=1
        
        

    def SignalThreadStr(self,stringa):
        print(str(stringa))
    
    def SignalDati(self,x,y,z):
        self.X=x
        self.Y=y
        self.Z=z
        
        
        if len(self.X) and len(self.Y) and len(self.Z):
            l=len(self.Z)

            self.draw(self.X,self.Y,self.Z)

        print("x:{}\r\ny:{}\r\nz:{}".format(self.X[l-1],self.Y[l-1],self.Z[l-1]))

    def draw(self,X,Y,Z):
        """!
        @brief Draw the plots.
    
        """
        ax_sq = np.square(X)
        ay_sq = np.square(Y)
        az_sq = np.square(Z)
        acc=np.sqrt(ax_sq+ay_sq+az_sq)
        l = len(acc)
        length = l-1
        l = np.arange(0, length+1, 1)
        self.graphWidget.plot(l,acc)


    def ShowVectData(self):

        ####excel####
        self.ExcelSave(self.X,self.Y,self.Z)

        print(self.X)
        print(len(self.X))

    def ExcelSave(self,X,Y,Z):
        d={'X':X,'Y':Y,'Z':Z}
        df=pd.DataFrame(data=d)
        
        df.to_excel("ouput_{}.xlsx".format(self.n_ex))
        self.n_ex+=1




    def SetPort(self,Port):
        self.portname=str(Port)
        print(self.portname)
        
        self.startAcq.setDisabled(False)
        self.stopAcq.setDisabled(False)
        self.ShowData.setDisabled(False)
        

    def initGUI(self):
        Wid=QWidget()
        hlay=QHBoxLayout()
        hlay.addWidget(self.graphWidget)
        hlay.addWidget(self.startAcq)
        hlay.addWidget(self.stopAcq)
        hlay.addWidget(self.searchWdiget)
        vlay=QVBoxLayout()
        vlay.addLayout(hlay)
        vlay.addWidget(self.ShowData)
        Wid.setLayout(vlay)
        self.setCentralWidget(Wid)

if __name__ == '__main__':
    # You need one (and only one) QApplication instance per application.
    # Pass in sys.argv to allow command line arguments for your app.
    # If you know you won't use command line arguments QApplication([])
    # works too.
    app = QApplication(sys.argv)
    
    # Create a Qt widget, which will be our window.
    
    w = MainW()
    w.show() # IMPORTANT!!!!! Windows are hidden by default.
    
    # Start the event loop.
    
    '''
    bt=BT_search()
    bt.show()
    '''
    
    sys.exit(app.exec_())


        
