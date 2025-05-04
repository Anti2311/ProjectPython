from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QLineEdit, QWidget, QLabel, QApplication, QVBoxLayout, QHBoxLayout
from instr import*
from second_win import *
class MainWin(QWidget):
    def iniUI(self):
       #description of interface elements
       self.hello_text =QLabel(txt_hello)
       self.instruction =QLabel(txt_instruction)
       self.button = QPushButton(txt_next)
       self.layout = QVBoxLayout()
       self.hello_text.addWidget(self.layout)
       self.instruction.addWidget(self.layout)
       self.button.addWidget(self.layout)

    def connects(self):
        self.btn_next.clicked.connet(self.next_click)
    def next_click(self):
       self.hide()  
    def next_click(self):
        self.hide()
        self.tw = TestWin()
app = QApplication([])
mw = MainWin()
app.exec_()

