from PyQt5.QtCore import QThread, pyqtSignal
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
    log = pyqtSignal(str)

    def __init__(self, main, calculator):
        QThread.__init__(self)
        self.calculator = calculator
        self.main = main

    def run(self):
        for i in range(self.calculator.converger_condition):
            self.calculator.calculate(i)
            time.sleep(0.0000000000000000000000000000000000000000000001)
        time.sleep(0.1)
        self.calculator.after_calculate()
        self.log.emit("程式計算完畢，請點擊Done按鈕")
        while True:
            time.sleep(0.01)


class DisplayThread(QThread):
    ratio = pyqtSignal(str, str)
    weight = pyqtSignal(str, str, str)
    progress = pyqtSignal(int)

    def __init__(self, main, calculator):
        QThread.__init__(self)
        self.main = main
        self.calculator = calculator

    def run(self):
        while True:
            self.ratio.emit(str(int(self.calculator.ratio_train)) +
                            "%", str(int(self.calculator.ratio_test)) + "%")
            w0 = str(round(self.calculator.w0, 5))
            w1 = str(round(self.calculator.w1, 5))
            w2 = str(round(self.calculator.w2, 5))
            self.weight.emit(w0, w1, w2)
            self.progress.emit(self.calculator.progress_percent)
            time.sleep(0.0000000000000000000000000000000000000000000001)
