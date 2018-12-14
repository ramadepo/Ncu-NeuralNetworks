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
        # initialize all essential object in GUI
        super().__init__()
        self.setupUi(self)
        self.started = False

        self.fileManager = FileManager(self.comboBox_filename)

        self.train_picture = PlotCanvas(self.plot_trainingData, 6, 6, 100)
        self.plot_train_thread = PlotThread(
            self.train_picture, "Data")
        self.preview_picture()

        self.calculator = Calculaor(self.train_picture)
        self.calculate_thread = CalculateThread(self.calculator)
        self.calculate_thread.log.connect(self.done_log)

        self.display_thread = DisplayThread(self.calculator)
        self.display_thread.progress.connect(self.set_progress)

    def start_calculate(self):
        # button click event
        # lock the button when program is calculating
        if self.started:
            if self.textArea_log.last != "程式計算完畢，請點擊Done按鈕":
                self.add_log("程式計算中，按鈕已鎖定")
            else:
                self.stop_calculate()
                self.pushButton.setText("Start")
        else:
            # input data is needed
            if len(self.lineEdit_convergeCondition.text()) < 1:
                self.add_log("請輸入收斂條件(迭代次數)")
            else:
                self.pushButton.setText("Wait...")
                self.calculate()

    def calculate(self):
        # turn on the thread to calculate and draw
        self.started = True
        self.add_log("開始計算...")
        self.calculator.initialize(int(self.lineEdit_convergeCondition.text()), self.fileManager)
        self.plot_train_thread.start()
        self.calculate_thread.start()
        self.display_thread.start()

    def stop_calculate(self):
        # turn off the thread and wait next event of button click
        self.started = False
        self.plot_train_thread.terminate()
        self.calculate_thread.terminate()
        self.display_thread.terminate()
        self.add_log("可點擊Start按鈕再次進行計算")

    def load_file_data(self):
        # load the current file selected in combo box
        self.fileManager.scan_file(self.comboBox_filename.currentText())
        self.train_picture.pre_plot(self.fileManager.train1, self.fileManager.train2, self.fileManager.x_min,
                                    self.fileManager.x_max, self.fileManager.y_min, self.fileManager.y_max)

    def preview_picture(self):
        # preview the picture of current file in combo box
        if not self.started:
            self.load_file_data()
            self.train_picture.subplot("Data")
            self.train_picture.draw()

    def add_log(self, log):
        # add log the GUI console window
        self.textArea_log.append(log)
        self.textArea_log.last = log

    def done_log(self, log):
        # the event of calculation done
        self.add_log(log)
        self.pushButton.setText("Done")

    def set_progress(self, progress):
        # set the value of GUI progress bar
        self.progressBar_progress.setValue(progress)


# program executed entry
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_window = Main()
    the_window.show()
    sys.exit(app.exec_())
