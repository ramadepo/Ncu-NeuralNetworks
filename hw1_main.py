import sys
from PyQt5.QtWidgets import QApplication, QSizePolicy
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QThread, pyqtSignal

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import window
import os


class Main(QMainWindow, window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fileManager = FileManager()
        self.set_files_list()
        self.train_picture = PlotCanvas(self.plot_trainingData, 5, 5, 100)
        self.test_picture = PlotCanvas(self.plot_testData, 5, 5, 100)

    def start_calculate(self):
        self.textArea_log.append("work on !")
        self.fileManager.scan_file(self.comboBox_filename.currentText())
        self.train_picture.pre_plot(
            self.fileManager.xs, self.fileManager.ys, self.fileManager.results)
        self.train_picture.plot("training data")
        self.test_picture.pre_plot(
            self.fileManager.xs, self.fileManager.ys, self.fileManager.results)
        self.test_picture.plot("testing data")

    def set_files_list(self):
        for file in self.fileManager.file_list:
            self.comboBox_filename.addItem(file)


class PlotCanvas(FigureCanvas):

    def __init__(self, parent, width, height, dpi):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(
            self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def pre_plot(self, xs, ys, results):
        self.xs1 = []
        self.xs2 = []
        self.ys1 = []
        self.ys2 = []
        for i in range(len(results)):
            if results[i] == 1:
                self.xs1.append(xs[i])
                self.ys1.append(ys[i])
            elif results[i] == 2 or results[i] == 0:
                self.xs2.append(xs[i])
                self.ys2.append(ys[i])

    def plot(self, plot_title):
        ax = self.figure.add_subplot(111)
        ax.clear()
        ax.set_title(plot_title)
        ax.plot(self.xs1, self.ys1, '.')
        ax.plot(self.xs2, self.ys2, 'x')
        self.draw()


class FileManager():
    def __init__(self):
        self.detect_files()

    def detect_files(self):
        self.file_list = []
        for i in os.listdir("./DataSet"):
            if i.endswith(".txt"):
                self.file_list.append(i)
        self.file_list.sort()

    def scan_file(self, filename):
        self.xs = []
        self.ys = []
        self.results = []
        file = open('./DataSet/'+filename, 'r').read()
        lines = file.split('\n')
        for line in lines:
            if len(line) > 1:
                x, y, result = line.split(' ')
                self.xs.append(float(x))
                self.ys.append(float(y))
                self.results.append(float(result))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_window = Main()
    the_window.show()
    sys.exit(app.exec_())
