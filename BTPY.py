import sys
import time
import logging
#from serial import Serial
import serial
import serial.tools.list_ports
#import libraries
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

STATO=0
CONNECTION_FLAG=0
BAUDRATE=9600

HEIGHT_M=300
WIDTH_M=300

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        global HEIGHT_M,WIDTH_M
        
        self.setWindowTitle("Scan BT Devices")
        self.MainWindowSize=[HEIGHT_M,WIDTH_M]
        self.setMinimumSize(self.MainWindowSize[0],self.MainWindowSize[1])
        self.butt_bt=QPushButton("Search for device")
        self.butt_bt.setMinimumSize(100,100)
        self.butt_bt.setMaximumSize(300,150)

        self.label_status=QLabel()
        self.listCom=[]
        self.baud=BAUDRATE
        self.s=serial.Serial()
        self.butt_bt.pressed.connect(self.ScanCom)

        #SearcCom()
        self.InitGUI()
        

    def ScanCom(self):
        listCom=[]
        for x in serial.tools.list_ports.comports():
            listCom.append(str(x.name))
        print(listCom)
        self.SearchCom(listCom)

    def SearchCom(self,list):
        try:
            for xc in list:
                self.s=serial.Serial(xc,self.baud,write_timeout=0, timeout=5)
                if self.s.is_open:
                    print(xc)
        except serial.SerialException:    
            self.displayerrorport(xc)

            


    def InitGUI(self):
        button_hlay = QHBoxLayout()
        button_hlay.addWidget(self.butt_bt)
        #self.setCentralWidget(self.butt_bt)
        button_hlay.addWidget(self.label_status)
        #self.setCentralWidget(self.label_status)
        vlay = QVBoxLayout()
        vlay.addLayout(button_hlay)
        widget = QWidget()
        widget.setLayout(vlay)
        self.setCentralWidget(widget)

    def displayerrorport(self,xc):
        """!
        self.dialog_errorport=QDialog(self)
        width = 300
        height = 250
        self.dialog_errorport.setMinimumSize(width, height)
        self.dialog_errorport.setWindowTitle("ERROR PORT: "+xc)
        self.dialog_errorportl=QLabel("ERROR PORT: "+xc)
        #self.dialog_errorportl.setAlignment(Qt.AlignCenter)
        
        self.error_hlay=QHBoxLayout()
        
        self.error_hlay.addWidget(self.dialog_errorportl)
        self.error_vlay=QVBoxLayout()
        self.error_vlay.addLayout(self.error_hlay)
        self.dialog_errorport.setLayout(self.error_vlay)
        
        self.dialog_errorport.exec_()
        """

        #try new class for error dialog
        self.ErrorCOM=ErrorW(300,200,'ERROR PORT: '+xc,'ERROR')
        self.ErrorCOM.exec_()

class ErrorW(QDialog):
    def __init__(self,width,height,errorText,windowTitle):
        super(QDialog).__init__()
        self.width=width
        self.height=height
        self.dialog_errorport.setMinimumSize(width, height)
        self.err_text=str(errorText)
        self.win_text=str(windowTitle)
        self.Text=QLabel(errorText)
        
        self.setWindowTitle(self.win_text)

        #define layout
        self.hlay=QHBoxLayout()
        self.hlay.addWidget(self.Text)
        self.vlay=QVBoxLayout()
        self.vlay.addLayout(self.error_hlay)
        self.setLayout(self.error_vlay)
        






#############
#  RUN APP  #
#############
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    
    w.show()
    sys.exit(app.exec_())





                  
