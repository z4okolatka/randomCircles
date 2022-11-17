import sys
from random import randint
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic

class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.btn.clicked.connect(self.drawCircle)

    def drawCircle(self):
        self.doPaint = True

    def paintEvent(self, event):
        if self.doPaint:
            self.painter = QPainter()
            self.painter.begin(self)
            self.draw()
            self.painter.end()

    def draw(self):
        r = randint(20, 100)
        x = randint(r, self.width() - r)
        y = randint(r, self.width() - r)
        self.painter.setBrush(QColor('yellow'))
        self.painter.drawEllipse(self, x - r, y - r, x + r, y + r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UI()
    ex.show()
    sys.exit(app.exec())
