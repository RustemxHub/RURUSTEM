import typing
import PyQt5
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont

# font -> .ttf

class Window(QWidget):
    
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.resize(1280, 900)
        self.setWindowTitle("PyQt5")
        self.label = QLabel(self, text='Hello PyQt5')
        self.label.move(50,720)
        font = QFont()
        font.setFamily('Roboto')
        font.setPointSize(20)
        self.label.setFont(font)

        self.label_1 = QLabel(self, text='Hello PyQt5')
        self.label_1.move(790,320)
        font = QFont()
        font.setFamily('Roboto')
        font.setPointSize(20)
        self.label_1.setFont(font)

        self.label_2 = QLabel(self, text='Hello PyQt5')
        self.label_2.move(540,220)
        font = QFont()
        font.setFamily('Italic')
        font.setPointSize(20)
        self.label_2.setFont(font)

def application():
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    application()