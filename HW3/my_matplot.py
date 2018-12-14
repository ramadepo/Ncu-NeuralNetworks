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
        self.x_min = x_min - 0.1
        self.x_max = x_max + 0.1
        self.y_min = y_min - 0.1
        self.y_max = y_max + 0.1

    def plot(self, plot_title):
        # plot the result line
        self.subplot(plot_title)
        # plot the connection between elements in matrix
        self.plot_connection()
        self.changed = False

    def subplot(self, plot_title):
        # plot the data point
        self.axes.clear()
        self.axes.set_title(plot_title)
        self.axes.set_xlim(self.x_min, self.x_max)
        self.axes.set_ylim(self.y_min, self.y_max)
        self.axes.plot(self.xs1, self.ys1, '.')
        self.axes.plot(self.xs2, self.ys2, 'x')
        self.changed = False

    def plot_connection(self):
        for i in range(9):
            for j in range(10):
                x = [self.matrix[i][j][0], self.matrix[i+1][j][0]]
                y = [self.matrix[i][j][1], self.matrix[i+1][j][1]]
                self.axes.plot(x, y, color='lightsteelblue', marker='.')
        for j in range(9):
            for i in range(10):
                x = [self.matrix[i][j][0], self.matrix[i][j+1][0]]
                y = [self.matrix[i][j][1], self.matrix[i][j+1][1]]
                self.axes.plot(x, y, color='lightsteelblue', marker='.')
    
    def get_matrix(self, matrix):
        self.matrix = matrix
        self.changed = True
