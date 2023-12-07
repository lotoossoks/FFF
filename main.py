from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
import sys
import random
from UI import Ui_MainWindow

SCREEN_SIZE = [680, 480]


class RandomCircle(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Git и случайные окружности')
        self.coords = []
        self.setupUi(self)
        self.FLAG = False
        self.pushButton.clicked.connect(self.draw)


    def draw(self):
        self.FIGURE = 'circle'
        self.SIZE = random.randint(10, 100)
        self.COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.FLAG = True
        self.update()

    def paintEvent(self, event):
        if self.FLAG:
            w = QPainter()
            w.begin(self)
            w.setPen(QColor(*self.COLOR))
            w.setBrush(QColor(*self.COLOR))
            self.x, self.y = random.randint(100, SCREEN_SIZE[0] - 100), random.randint(100, SCREEN_SIZE[1] - 100)
            if self.FIGURE == 'circle':
                w.drawEllipse(self.x, self.y, self.SIZE, self.SIZE)
            w.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomCircle()
    ex.show()
    sys.exit(app.exec_())