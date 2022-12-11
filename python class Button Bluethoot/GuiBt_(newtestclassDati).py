import serial
import numpy as np
import sys
import ctypes

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
from BTPY_class import(
    BT_search
)

    





class MainW(QMainWindow):
    def __init__(self):
        super(MainW,self).__init__()
        self.X=[]
        self.Y=[]
        self.Z=[]
        self.time=[]
        self.portname=''
        
        self.setWindowTitle("classDatiTest")

        self.startAcq=QPushButton("Start Acquisition")
        self.startAcq.setDisabled(True)
        self.stopAcq=QPushButton("Stop Acquisition")
        self.stopAcq.setDisabled(True)
        self.ShowData=QPushButton("ShowData")
        self.ShowData.setDisabled(True)

        self.Dati=DatiSerial(None,'Ready')
        
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
            self.FlagStart=True
            self.ThreadDati.start(self.Dati)
            self.Dati.is_killed=False
            print("iskilled:"+str(self.Dati.is_killed))
            self.startAcq.setDisabled(True)
            

    
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

    def SetPort(self,Port):
        self.portname=str(Port)
        self.Dati=DatiSerial(str(Port),'Ready')
        self.startAcq.setDisabled(False)
        self.stopAcq.setDisabled(False)
        self.ShowData.setDisabled(False)
        

    def initGUI(self):
        Wid=QWidget()
        hlay=QHBoxLayout()
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


        
