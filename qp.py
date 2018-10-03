import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
from PyQt5.QtWidgets import QLineEdit, QVBoxLayout, QFormLayout
from PyQt5.QtCore import QThread, pyqtSignal

class TutorialThread(QThread):
    set_max = pyqtSignal(int)
    update = pyqtSignal(int)

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        self.set_max.emit(101)
        for i in range(0,101):
            self.update.emit(i)
            time.sleep(0.5)

class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi()
        self._tutorial_thread = TutorialThread()
        self._tutorial_thread.set_max.connect(self.set_max)
        self._tutorial_thread.update.connect(self.set_value)
        self.show()
    def setupUi(self):
        self.setWindowTitle("Thread Test")

        self.button_start = QPushButton()
        self.button_start.setText("start")
        self.button_stop = QPushButton()
        self.button_stop.setText("stop")

        self.progress_bar = QProgressBar()

        self.line = QLineEdit()

        the_form = QFormLayout()
        the_form.addRow(self.button_start, self.line)
        the_form.addRow(self.button_stop)
        the_form.addRow(self.progress_bar)

        the_layout = QVBoxLayout()
        the_layout.addLayout(the_form)

        self.setLayout(the_layout)

        self.button_start.clicked.connect(self.start)
        self.button_stop.clicked.connect(self.stop)
        
    def start(self):
        self.line.setText("觸發重置這裡")
        self._tutorial_thread.start()
    
    def stop(self):
        self._tutorial_thread.terminate()

    def set_max(self, data):
        self.progress_bar.setMaximum(data)

    
    def set_value(self, data):
        self.progress_bar.setValue(data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_window = MainWindow()
    sys.exit(app.exec_())