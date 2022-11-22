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

BAUDRATE=9600

HEIGHT_M=300
WIDTH_M=300

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        global HEIGHT_M,WIDTH_M
        

        self.connectionFlag=0

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
        

        self.chreceived=''
        self.chserial=''

        #SearcCom()
        self.InitGUI()
        

    def ScanCom(self):
        global STATO
        STATO="SEARCHING"
        self.ChangeStatus(STATO)
        listCom=[]
        
        for x in serial.tools.list_ports.comports():
            listCom.append(str(x.name))
        print(listCom)
        
        self.SearchCom(listCom)

    def SearchCom(self,list):
        
        global STATO
        
        

        try:
            if self.connectionFlag ==0:
                for xc in list:
                    self.s=serial.Serial(xc,self.baud,write_timeout=0, timeout=5)
                    if self.s.is_open and self.connectionFlag==0:
                        print(xc)
                        self.chreceived=self.ReadDataSerial()
                        print(str(self.chreceived))
                        if self.chreceived == '\'\'':
                            print("connection estabilished")
                            STATO='CONNECTED'
                            self.ChangeStatus(STATO)
                            self.connectionFlag=1
                            self.butt_bt.setDisabled(True)
                        



        except serial.SerialException:
            if self.connectionFlag==0:    
                self.displayerrorport(xc)
            


            
    def ReadDataSerial(self):
        self.chserial=str(self.s.readline())
        self.chserial=self.chserial[1:]
        return self.chserial


    def ChangeStatus(self, status):
        self.label_status.setText(str(status))


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
        self.ErrorCOM=ErrorW(300,200,'ERROR PORT CONNECTION: '+xc,'ERROR')
        self.ErrorCOM.exec_()

class ErrorW(QDialog):
    def __init__(self,width,height,errorText,windowTitle):
        super(QDialog,self).__init__()
        self.width=width
        self.height=height
        self.setMinimumSize(width, height)
        self.err_text=str(errorText)
        self.win_text=str(windowTitle)
        self.Text=QLabel(errorText)
        
        self.setWindowTitle(self.win_text)

        #define layout
        self.hlay=QHBoxLayout()
        self.hlay.addWidget(self.Text)
        self.vlay=QVBoxLayout()
        self.vlay.addLayout(self.hlay)
        self.setLayout(self.vlay)
        






#############
#  RUN APP  #
#############
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    
    w.show()
    sys.exit(app.exec_())





                  
