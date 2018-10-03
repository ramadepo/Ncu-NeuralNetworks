from PyQt5.QtCore import QThread
import time


class PlotThread(QThread):
    def __init__(self, train_picture, test_picture):
        QThread.__init__(self)
        self.train_picture = train_picture
        self.test_picture = test_picture

    def run(self):
        while True:
            self.train_picture.plot("training data")
            self.test_picture.plot("training data")
            print("oh")
            time.sleep(0.2)


class CalculateThread(QThread):
    def __init__(self):
        QThread.__init__(self)

    def run(self):
        while True:
            print("ho")
            time.sleep(0.3)
