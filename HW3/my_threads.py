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

    def __init__(self, calculator):
        QThread.__init__(self)
        self.calculator = calculator

    def run(self):
        for i in range(self.calculator.converger_condition):
            self.calculator.calculate(i)
            time.sleep(0.0000000000000000000000000000000000000000000001)

        # calculation done
        time.sleep(0.1)
        self.calculator.after_calculate()
        self.log.emit("程式計算完畢，請點擊Done按鈕")
        while True:
            time.sleep(0.01)


class DisplayThread(QThread):
    # initialize signal
    progress = pyqtSignal(int)

    def __init__(self, calculator):
        QThread.__init__(self)
        self.calculator = calculator

    def run(self):
        while True:
            # send the event to Main Thread to update the GUI label value
            self.progress.emit(self.calculator.progress_percent)
            time.sleep(0.0000000000000000000000000000000000000000000001)
