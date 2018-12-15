from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np


class PlotCanvas(FigureCanvas):

    def __init__(self, parent, preview_parent, width, height, sub_width, sub_height, dpi):
        # initialize the object for plotting picture
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(
            self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.changed = False
        self.preview_picture = PlotPreview(preview_parent, sub_width, sub_height, dpi)

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
        self.preview_picture.plot('Topology Only', self.x_min, self.x_max, self.y_min, self.y_max, self.matrix, self.topology_size_i, self.topology_size_j)
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
        for i in range(self.topology_size_i-1):
            for j in range(self.topology_size_j):
                x = [self.matrix[i][j][0], self.matrix[i+1][j][0]]
                y = [self.matrix[i][j][1], self.matrix[i+1][j][1]]
                self.axes.plot(x, y, color='lightsteelblue', marker='.')
        for j in range(self.topology_size_j-1):
            for i in range(self.topology_size_i):
                x = [self.matrix[i][j][0], self.matrix[i][j+1][0]]
                y = [self.matrix[i][j][1], self.matrix[i][j+1][1]]
                self.axes.plot(x, y, color='lightsteelblue', marker='.')
    
    def get_matrix(self, matrix, topology_size_i, topology_size_j):
        self.matrix = matrix
        self.topology_size_i = topology_size_i
        self.topology_size_j = topology_size_j
        self.changed = True

class PlotPreview(FigureCanvas):
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

    def plot(self, title, x_min, x_max, y_min, y_max, matrix, topology_size_i, topology_size_j):
        self.subplot(title, x_min, x_max, y_min, y_max)
        self.plot_connection(matrix, topology_size_i, topology_size_j)

    def subplot(self, title, x_min, x_max, y_min, y_max):
        self.axes.clear()
        self.axes.set_title(title)
        self.axes.set_xlim(x_min, x_max)
        self.axes.set_ylim(y_min, y_max)
    
    def plot_connection(self, matrix, topology_size_i, topology_size_j):
        for i in range(topology_size_i-1):
            for j in range(topology_size_j):
                x = [matrix[i][j][0], matrix[i+1][j][0]]
                y = [matrix[i][j][1], matrix[i+1][j][1]]
                self.axes.plot(x, y, color='lightsteelblue', marker='.')
        for j in range(topology_size_j-1):
            for i in range(topology_size_i):
                x = [matrix[i][j][0], matrix[i][j+1][0]]
                y = [matrix[i][j][1], matrix[i][j+1][1]]
                self.axes.plot(x, y, color='lightsteelblue', marker='.')