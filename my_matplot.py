from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class PlotCanvas(FigureCanvas):

    def __init__(self, parent, width, height, dpi):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(
            self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def pre_plot(self, data1, data2):
        self.xs1 = data1["xs"]
        self.xs2 = data2["xs"]
        self.ys1 = data1["ys"]
        self.ys2 = data2["ys"]

    def plot(self, plot_title):
        ax = self.figure.add_subplot(111)
        ax.clear()
        ax.set_title(plot_title)
        ax.plot(self.xs1, self.ys1, '.')
        ax.plot(self.xs2, self.ys2, 'x')
        self.draw()
