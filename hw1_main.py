import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal

from my_matplot import PlotCanvas
from my_file_manager import FileManager
import window
from my_threads import PlotThread, CalculateThread, DisplayThread
from my_calculator import Calculaor


class Main(QMainWindow, window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fileManager = FileManager(self.comboBox_filename)
        self.train_picture = PlotCanvas(self.plot_trainingData, 5, 5, 100)
        self.test_picture = PlotCanvas(self.plot_testData, 5, 5, 100)
        self.plot_train_thread = PlotThread(
            self.train_picture, "training data")
        self.plot_test_thread = PlotThread(self.test_picture, "testing data")
        self.calculator = Calculaor(
            self.train_picture, self.test_picture)
        self.calculate_thread = CalculateThread(
            self.calculator, self.textArea_log)
        self.display_thread = DisplayThread(
            self.label_trainingPercent, self.label_testPercent, self.label_weightValue, self.calculator)
        self.started = False

    def start_calculate(self):
        if self.started:
            if self.textArea_log.last != "Calculate done.":
                self.textArea_log.append(
                    "Process is calculating, so start button is locked.")
                self.textArea_log.last = "Process is calculating, so start button is locked."
            else:
                self.stop_calculate()
        else:
            self.calculate()

    def calculate(self):
        self.started = True
        self.fileManager.scan_file(self.comboBox_filename.currentText())
        self.train_picture.pre_plot(
            self.fileManager.train1, self.fileManager.train2, self.fileManager.x_min, self.fileManager.x_max, self.fileManager.y_min, self.fileManager.y_max)
        self.test_picture.pre_plot(
            self.fileManager.test1, self.fileManager.test2, self.fileManager.x_min, self.fileManager.x_max, self.fileManager.y_min, self.fileManager.y_max)

        self.textArea_log.append("work on !")
        self.textArea_log.last = "work on !"

        self.calculator.initialize(float(self.lineEdit_studyScale.text()), int(
            self.lineEdit_convergeCondition.text()), self.fileManager)

        self.plot_train_thread.start()
        self.plot_test_thread.start()
        self.calculate_thread.start()
        self.display_thread.start()

    def stop_calculate(self):
        self.started = False
        self.plot_train_thread.terminate()
        self.plot_test_thread.terminate()
        self.calculate_thread.terminate()
        self.textArea_log.append(
            "Calculation is shut down. Please click start button to restart calculation.")
        self.textArea_log.last = "Calculation is shut down. Please click start button to restart calculation."


if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_window = Main()
    the_window.show()
    sys.exit(app.exec_())
