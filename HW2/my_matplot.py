from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np


class PlotCanvas(FigureCanvas):

    def __init__(self, parent, width, height, dpi):
        # initialize the object for plotting picture
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(
            self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.changed = False

    def pre_plot(self, data1, data2, x_min, x_max, y_min, y_max):
        # load some essential data
        self.xs1 = data1["xs"]
        self.xs2 = data2["xs"]
        self.ys1 = data1["ys"]
        self.ys2 = data2["ys"]
        self.x_min = x_min - ((x_max - x_min) / 20)
        self.x_max = x_max + ((x_max - x_min) / 20)
        self.y_min = y_min - ((y_max - y_min) / 20)
        self.y_max = y_max + ((y_max - y_min) / 20)

    def get_weight_interval(self, w0, w1, w2):
        # set the result line weight
        self.w0 = w0
        self.w1 = w1
        self.w2 = w2
        self.changed = True

    def plot(self, plot_title):
        # plot the result line
        self.subplot(plot_title)
        x = np.linspace(self.x_min, self.x_max, 2)
        y = ((self.w1 * x * (-1)) + self.w0) / self.w2
        self.axes.plot(x, y, 'r')
        self.changed = False

    def subplot(self, plot_title):
        # plot the data point
        self.axes.clear()
        self.axes.set_title(plot_title)
        self.axes.set_xlim(self.x_min, self.x_max)
        self.axes.set_ylim(self.y_min, self.y_max)
        self.axes.plot(self.xs1, self.ys1, '.')
        self.axes.plot(self.xs2, self.ys2, 'x')
