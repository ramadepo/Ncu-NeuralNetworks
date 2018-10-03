import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QThread, pyqtSignal

from my_matplot import PlotCanvas
from my_file_manager import FileManager
import window


class Main(QMainWindow, window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fileManager = FileManager()
        self.set_files_list()
        self.train_picture = PlotCanvas(self.plot_trainingData, 5, 5, 100)
        self.test_picture = PlotCanvas(self.plot_testData, 5, 5, 100)

    def start_calculate(self):
        self.fileManager.scan_file(self.comboBox_filename.currentText())
        self.train_picture.pre_plot(
            self.fileManager.train1, self.fileManager.train2)
        self.train_picture.plot("training data")
        self.test_picture.pre_plot(
            self.fileManager.test1, self.fileManager.test2)
        self.test_picture.plot("testing data")

        self.textArea_log.append("work on !")

    def set_files_list(self):
        for file in self.fileManager.file_list:
            self.comboBox_filename.addItem(file)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_window = Main()
    the_window.show()
    sys.exit(app.exec_())
