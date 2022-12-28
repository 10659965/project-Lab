import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QTabWidget, \
                            QGridLayout, QVBoxLayout

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)

        mainLayout = QGridLayout()
        vLayout = QVBoxLayout()

        # TAb 1.1
        self.tab_1 = QWidget()
        self.tab_1.layout =QVBoxLayout()
        self.tab_1.layout.addWidget(QLabel('<font size+8><b>Type something </font'))

        self.lineEdit = QLineEdit()
        self.btn_print = QPushButton('Print')
        self.tab_1.layout.addWidget(self.lineEdit)
        self.tab_1.layout.addWidget(self.btn_print)

        self.tab_1.setLayout(self.tab_1.layout)

        # tab 1.2
        self.btn = QPushButton(' A button')
        self.btn.clicked.connect(lambda: print('hello'))

        self.tab_2 = QWidget()
        self.tab_2.layout = QVBoxLayout()
        self.tab_2.layout.addWidget(self.btn)
        self.tab_2.setLayout(self.tab_2.layout)

        # tab 1 parent
        self.tabs1 = QTabWidget()
        self.tabs1.addTab(self.tab_1, 'Tab 1.1') #caption
        self.tabs1.addTab(self.tab_2, 'Tab 1.2')

        # tab 2

        self.btn2 = QPushButton('B Button')
        self.btn2.clicked.connect(lambda: print('B button clicked'))

        self.tabs2 = QTabWidget()
        self.tabs2.addTab(self.btn2, 'tab 2')


        mainLayout.addWidget(self.tabs1, 1, 0)
        mainLayout.addWidget(self.tabs2, 0, 1) #1 serve per mettere in colonne diverse
        self.setLayout(mainLayout)

    def type_something(self):
        print(self.lineEdit.text())

app = QApplication(sys.argv)

demo = AppDemo()
demo.show()

sys.exit(app.exec_())

