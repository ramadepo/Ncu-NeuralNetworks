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
                self.picture.draw()
            time.sleep(0.0000000000000000000000000000000000000000000001)


class CalculateThread(QThread):
    def __init__(self, calculator, log):
        QThread.__init__(self)
        self.calculator = calculator
        self.log = log

    def run(self):
        for i in range(self.calculator.converger_condition):
            self.calculator.calculate(i)
            time.sleep(0.0000000000000000000000000000000000000000000001)
        time.sleep(0.1)
        self.calculator.after_calculate()
        self.log.append("Calculation done. Please click Start button.")
        self.log.last = "Calculation done. Please click Start button."
        while True:
            time.sleep(0.01)


class DisplayThread(QThread):
    def __init__(self, label_train, label_test, label_weight, calculator):
        QThread.__init__(self)
        self.label_train = label_train
        self.label_test = label_test
        self.label_weight = label_weight
        self.calculator = calculator

    def run(self):
        while True:
            self.label_train.setText(
                str(int(self.calculator.ratio_train)) + "%")
            self.label_test.setText(str(int(self.calculator.ratio_test)) + "%")
            w0 = str(round(self.calculator.w0, 5))
            w1 = str(round(self.calculator.w1, 5))
            w2 = str(round(self.calculator.w2, 5))
            self.label_weight.setText("[ " + w0 + ", " + w1 + ", " + w2 + " ]")
            time.sleep(0.0000000000000000000000000000000000000000000001)
