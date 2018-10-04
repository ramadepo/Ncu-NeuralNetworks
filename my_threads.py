from PyQt5.QtCore import QThread
import time


class PlotThread(QThread):
    def __init__(self, picture, name):
        QThread.__init__(self)
        self.picture = picture
        self. name = name

    def run(self):
        while True:
            if self.picture.changed:
                self.picture.plot(self.name)
                print(self.name)
                self.picture.draw()
                print(self.picture.w0, self.picture.w1, self.picture.w2)
            time.sleep(0.0000000000000000000000000000000000000000000001)


class CalculateThread(QThread):
    def __init__(self, calculator):
        QThread.__init__(self)
        self.calculator = calculator

    def run(self):
        for i in range(self.calculator.converger_condition):
            self.calculator.calculate(i)
            time.sleep(0.0000000000000000000000000000000000000000000001)
        time.sleep(0.1)
        self.calculator.after_calculate()

        while True:
            time.sleep(0.01)
