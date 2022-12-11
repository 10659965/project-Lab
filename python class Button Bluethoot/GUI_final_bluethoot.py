import serial
import numpy as np
import sys
import ctypes
import serial.tools.list_ports

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
    QGridLayout,
    
)

from BTPY_class import BT_search
from WidgetSerialDati import WidgetDati
from class_Dati import DatiSerial


STATO=0
BAUDRATE=115200
HEIGHT_M=300
WIDTH_M=300

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle("mainTotalBt")
        self.Search=BT_search('Ready')
        self.DataStream=WidgetDati()
        
        self.DataLabelX=QLabel()
        self.DataLabelY=QLabel()
        self.DataLabelZ=QLabel()
        
            
        self.Search.signalport.portname.connect(self.SetPort)
        
        
       
        self.DataStream.ShowData.pressed.connect(self.StampaDati)

        self.initGUI()
    
    def StampaDati(self):
        if len(self.DataStream.X)==len(self.DataStream.Y):
            l=len(self.DataStream.X)
            self.DataLabelX.setText("X: {}".format(self.DataStream.X[l-1]))
            self.DataLabelY.setText("Y: {}".format(self.DataStream.Y[l-1]))
            self.DataLabelZ.setText("X: {}".format(self.DataStream.Z[l-1]))

    def DataStreamEnable(self):
        self.DataStream.startAcq.setDisabled(False)
        self.DataStream.stopAcq.setDisabled(False)
        self.DataStream.ShowData.setDisabled(False)

    def SetPort(self,portname):
        
        self.DataStream.setPortW(portname)

        print("settedport:"+str(self.DataStream.serialport))

    def initGUI(self):
        Elements=QWidget()
        hlabel=QHBoxLayout()
        hlabel.addWidget(self.DataLabelX)
        hlabel.addWidget(self.DataLabelY)
        hlabel.addWidget(self.DataLabelZ)
        
        vhlay=QVBoxLayout()
        vhlay.addWidget(self.DataStream)
        vhlay.addLayout(hlabel)
        vhlay.addWidget(self.Search)
        Elements.setLayout(vhlay)
        self.setCentralWidget(Elements)

        

            
                
        








if __name__ == '__main__':
    # You need one (and only one) QApplication instance per application.
    # Pass in sys.argv to allow command line arguments for your app.
    # If you know you won't use command line arguments QApplication([])
    # works too.
    app = QApplication(sys.argv)
    
    # Create a Qt widget, which will be our window.
    
    w = MainWindow()
    w.show() # IMPORTANT!!!!! Windows are hidden by default.
    
    # Start the event loop.
    
    '''
    bt=BT_search()
    bt.show()
    '''
    
    sys.exit(app.exec_())
