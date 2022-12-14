import serial
import numpy as np
import sys
import ctypes
import time

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
    convert
)
    





class WidgetDati(QWidget):
    def __init__(self):
        super().__init__()
        self.X=[]
        self.Y=[]
        self.Z=[]
        self.time=[]
        
        
        
        self.serialport=None
        
        self.setWindowTitle("classDatiTest")

        self.startAcq=QPushButton("Start Acquisition")
        self.stopAcq=QPushButton("Stop Acquisition")
        self.ShowData=QPushButton("ShowData")

        self.Dati=DatiSerial(None,None)
        
        self.ThreadDati=QThreadPool()
        
        self.startAcq.pressed.connect(self.StartAcquisition)
        self.stopAcq.pressed.connect(self.AbortAcquisition)
        self.ShowData.pressed.connect(self.ShowVectData)
        self.Dati.signals.service_string.connect(self.SignalThreadStr)
        self.Dati.signals.dati.connect(self.SignalDati)
        
            
        


        self.initGUI()

    
        
    
    def StartAcquisition(self):
            self.FlagStart=True
            #restore serial
            self.Dati=DatiSerial(self.serialport,'Ready')
            self.Dati.signals.service_string.connect(self.SignalThreadStr)
            self.Dati.signals.dati.connect(self.SignalDati)
        
            
            time.sleep(0.05)
            self.StartThread()
            self.Dati.is_killed=False
            print("iskilled:"+str(self.Dati.is_killed))
            print("connected to port: "+str(self.Dati.PortName))
            self.startAcq.setDisabled(True)
            
    def StartThread(self):
        self.ThreadDati=QThreadPool()
        self.ThreadDati.start(self.Dati)
        
    
    def AbortAcquisition(self):
        self.Dati.Abort()
        #self.Dati.is_killed=True
        print("iskilled:"+str(self.Dati.is_killed))
        self.startAcq.setDisabled(False)
        
        

    def SignalThreadStr(self,stringa):
        print(str(stringa))
    
    def SignalDati(self,x,y,z):
        self.X=x
        self.Y=y
        self.Z=z
        
        
        if len(self.X) and len(self.Y) and len(self.Z):
            l=len(self.Z)

        print("x:{}\r\ny:{}\r\nz:{}".format(self.X[l-1],self.Y[l-1],self.Z[l-1]))

    def ShowVectData(self):
        print(self.X)
        print(len(self.X))

    def setPortW(self,portname):
        self.serialport=portname    

    def initGUI(self):
        
        hlay=QHBoxLayout()
        hlay.addWidget(self.startAcq)
        hlay.addWidget(self.stopAcq)
        vlay=QVBoxLayout()
        vlay.addLayout(hlay)
        vlay.addWidget(self.ShowData)
        self.setLayout(vlay)


        
