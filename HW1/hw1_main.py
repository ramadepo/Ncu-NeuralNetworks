import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal

from my_matplot import PlotCanvas
from my_file_manager import FileManager
import window
from my_threads import PlotThread, CalculateThread, DisplayThread
from my_calculator import Calculaor
import time


class Main(QMainWindow, window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.started = False
        self.fileManager = FileManager(self.comboBox_filename)
        self.train_picture = PlotCanvas(self.plot_trainingData, 5, 5, 100)
        self.test_picture = PlotCanvas(self.plot_testData, 5, 5, 100)
        self.plot_train_thread = PlotThread(
            self.train_picture, "training data")
        self.plot_test_thread = PlotThread(self.test_picture, "testing data")
        self.preview_picture()
        self.calculator = Calculaor(
            self.train_picture, self.test_picture)
        self.calculate_thread = CalculateThread(self, self.calculator)
        self.calculate_thread.log.connect(self.done_log)
        self.display_thread = DisplayThread(self, self.calculator)
        self.display_thread.ratio.connect(self.set_ratio)
        self.display_thread.weight.connect(self.set_weight)
        self.display_thread.progress.connect(self.set_progress)

    def start_calculate(self):
        if self.started:
            if self.textArea_log.last != "程式計算完畢，請點擊Done按鈕":
                self.add_log("程式計算中，按鈕已鎖定")
            else:
                self.stop_calculate()
                self.pushButton.setText("Start")
        else:
            if len(self.lineEdit_studyScale.text()) < 1:
                self.add_log("請輸入學習率")
            elif len(self.lineEdit_convergeCondition.text()) < 1:
                self.add_log("請輸入收斂條件(迭代次數)")
            else:
                self.pushButton.setText("Wait...")
                self.calculate()

    def calculate(self):
        self.started = True
        self.add_log("開始計算...")
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
        self.display_thread.terminate()
        self.add_log("可點擊Start按鈕再次進行計算")

    def load_file_data(self):
        self.fileManager.scan_file(self.comboBox_filename.currentText())
        self.train_picture.pre_plot(self.fileManager.train1, self.fileManager.train2, self.fileManager.x_min,
                                    self.fileManager.x_max, self.fileManager.y_min, self.fileManager.y_max)
        self.test_picture.pre_plot(self.fileManager.test1, self.fileManager.test2, self.fileManager.x_min,
                                   self.fileManager.x_max, self.fileManager.y_min, self.fileManager.y_max)

    def preview_picture(self):
        if not self.started:
            self.load_file_data()
            self.train_picture.subplot("training data")
            self.test_picture.subplot("test data")
            self.train_picture.draw()
            self.test_picture.draw()

    def add_log(self, log):
        self.textArea_log.append(log)
        self.textArea_log.last = log

    def done_log(self, log):
        self.add_log(log)
        self.pushButton.setText("Done")

    def set_ratio(self, train, test):
        self.label_trainingPercent.setText(train)
        self.label_testPercent.setText(test)

    def set_weight(self, w0, w1, w2):
        self.label_weightValue.setText(
            "[ " + w0 + ", " + w1 + ", " + w2 + " ]")

    def set_progress(self, progress):
        self.progressBar_progress.setValue(progress)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_window = Main()
    the_window.show()
    sys.exit(app.exec_())
