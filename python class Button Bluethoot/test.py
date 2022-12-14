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
    QGridLayout,
    
)

STATO=0

BAUDRATE=9600

HEIGHT_M=300
WIDTH_M=300


from BTPY_class import(
    BT_search,
    ErrorW,
)


class MainWindow(QMainWindow):
    def __init__(self):
      super(MainWindow, self).__init__()
      #self.BT_W=BT_search()
      self.setWindowTitle("main")
      
      self.e = BT_search('Ready')
      #self.e.show()
      
      self.checkport=QPushButton("checkport")
      self.checkport.pressed.connect(self.ShowConnPort)
      
      self.Gui()
      
    def Gui(self):
        win= QWidget()
        hlayout = QHBoxLayout()
        
        hlayout.addWidget(self.e)
        vlayout=QVBoxLayout()
        vlayout.addLayout(hlayout)
        vlayout.addWidget(self.checkport)

        #layout.addWidget(self.check)
        #self.e.show()
        win.setLayout(vlayout)
        #self.setCentralWidget(self.win)
        self.setCentralWidget(win)
        
        #self.e.show()
    
    def ShowConnPort(self):
        print(str(self.e.portName))
  
        


    



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
