from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np


class PlotCanvas(FigureCanvas):

    def __init__(self, parent, width, height, dpi):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(
            self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.changed = False

    def pre_plot(self, data1, data2):
        self.xs1 = data1["xs"]
        self.xs2 = data2["xs"]
        self.ys1 = data1["ys"]
        self.ys2 = data2["ys"]

    def get_weight_interval(self, w0, w1, w2, x_min, x_max):
        self.w0 = w0
        self.w1 = w1
        self.w2 = w2
        self.x_min = x_min
        self.x_max = x_max
        self.changed = True

    def plot(self, plot_title):
        #ax = self.figure.add_subplot(111)
        self.axes.clear()
        self.axes.set_title(plot_title)
        self.axes.plot(self.xs1, self.ys1, '.')
        self.axes.plot(self.xs2, self.ys2, 'x')
        x = np.linspace(self.x_min, self.x_max, 2)
        y = ((self.w1 * x * (-1)) + self.w0) / self.w2
        self.axes.plot(x, y, 'r')
        self.changed = False
