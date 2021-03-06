# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hw1.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1024, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 768))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 768))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(55, 55, 55);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 451, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_hint_convergeCondition = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_hint_convergeCondition.setFont(font)
        self.label_hint_convergeCondition.setStyleSheet("color: rgb(162, 162, 162);")
        self.label_hint_convergeCondition.setAlignment(QtCore.Qt.AlignCenter)
        self.label_hint_convergeCondition.setObjectName("label_hint_convergeCondition")
        self.gridLayout.addWidget(self.label_hint_convergeCondition, 2, 2, 1, 1)
        self.label_convergeCondition = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_convergeCondition.setFont(font)
        self.label_convergeCondition.setStyleSheet("color: rgb(162, 162, 162);")
        self.label_convergeCondition.setAlignment(QtCore.Qt.AlignCenter)
        self.label_convergeCondition.setObjectName("label_convergeCondition")
        self.gridLayout.addWidget(self.label_convergeCondition, 2, 0, 1, 1)
        self.label_studyScale = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_studyScale.setFont(font)
        self.label_studyScale.setStyleSheet("color: rgb(162, 162, 162);")
        self.label_studyScale.setScaledContents(False)
        self.label_studyScale.setAlignment(QtCore.Qt.AlignCenter)
        self.label_studyScale.setObjectName("label_studyScale")
        self.gridLayout.addWidget(self.label_studyScale, 1, 0, 1, 1)
        self.label_filename = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_filename.setFont(font)
        self.label_filename.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_filename.setAutoFillBackground(False)
        self.label_filename.setStyleSheet("color: rgb(162, 162, 162);")
        self.label_filename.setTextFormat(QtCore.Qt.AutoText)
        self.label_filename.setScaledContents(False)
        self.label_filename.setAlignment(QtCore.Qt.AlignCenter)
        self.label_filename.setObjectName("label_filename")
        self.gridLayout.addWidget(self.label_filename, 0, 0, 1, 1)
        self.lineEdit_studyScale = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_studyScale.setFont(font)
        self.lineEdit_studyScale.setStyleSheet("color: rgb(162, 162, 162);\n"
"background-color: rgb(80, 80, 80);")
        self.lineEdit_studyScale.setObjectName("lineEdit_studyScale")
        self.gridLayout.addWidget(self.lineEdit_studyScale, 1, 1, 1, 2)
        self.lineEdit_convergeCondition = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_convergeCondition.sizePolicy().hasHeightForWidth())
        self.lineEdit_convergeCondition.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_convergeCondition.setFont(font)
        self.lineEdit_convergeCondition.setStyleSheet("color: rgb(162, 162, 162);\n"
"background-color: rgb(80, 80, 80);")
        self.lineEdit_convergeCondition.setObjectName("lineEdit_convergeCondition")
        self.gridLayout.addWidget(self.lineEdit_convergeCondition, 2, 1, 1, 1)
        self.widget_for_filenameBackground = QtWidgets.QWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_for_filenameBackground.sizePolicy().hasHeightForWidth())
        self.widget_for_filenameBackground.setSizePolicy(sizePolicy)
        self.widget_for_filenameBackground.setMinimumSize(QtCore.QSize(0, 30))
        self.widget_for_filenameBackground.setStyleSheet("background-color: rgb(125, 125, 125);")
        self.widget_for_filenameBackground.setObjectName("widget_for_filenameBackground")
        self.comboBox_filename = QtWidgets.QComboBox(self.widget_for_filenameBackground)
        self.comboBox_filename.setGeometry(QtCore.QRect(-1, 0, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_filename.setFont(font)
        self.comboBox_filename.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox_filename.setStyleSheet("color: rgb(162, 162, 162);\n"
"background-color: rgb(80, 80, 80);")
        self.comboBox_filename.setObjectName("comboBox_filename")
        self.gridLayout.addWidget(self.widget_for_filenameBackground, 0, 1, 1, 2)
        self.label_convergeCondition.raise_()
        self.lineEdit_convergeCondition.raise_()
        self.lineEdit_studyScale.raise_()
        self.label_filename.raise_()
        self.label_studyScale.raise_()
        self.label_hint_convergeCondition.raise_()
        self.widget_for_filenameBackground.raise_()
        self.textArea_log = QtWidgets.QTextBrowser(self.centralwidget)
        self.textArea_log.setGeometry(QtCore.QRect(0, 660, 1031, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textArea_log.setFont(font)
        self.textArea_log.setStyleSheet("color: rgb(0, 255, 0);")
        self.textArea_log.setReadOnly(True)
        self.textArea_log.setObjectName("textArea_log")
        self.picture_devidedLine = QtWidgets.QGraphicsView(self.centralwidget)
        self.picture_devidedLine.setGeometry(QtCore.QRect(0, 650, 1031, 20))
        self.picture_devidedLine.setStyleSheet("background-color: rgb(162, 162, 162);")
        self.picture_devidedLine.setObjectName("picture_devidedLine")
        self.plot_trainingData = QtWidgets.QWidget(self.centralwidget)
        self.plot_trainingData.setGeometry(QtCore.QRect(20, 150, 481, 481))
        self.plot_trainingData.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plot_trainingData.setObjectName("plot_trainingData")
        self.plot_testData = QtWidgets.QWidget(self.centralwidget)
        self.plot_testData.setGeometry(QtCore.QRect(520, 150, 481, 481))
        self.plot_testData.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plot_testData.setObjectName("plot_testData")
        self.label_trainingData = QtWidgets.QLabel(self.centralwidget)
        self.label_trainingData.setGeometry(QtCore.QRect(510, 30, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_trainingData.setFont(font)
        self.label_trainingData.setStyleSheet("color: rgb(162, 162, 162);")
        self.label_trainingData.setObjectName("label_trainingData")
        self.label_trainingPercent = QtWidgets.QLabel(self.centralwidget)
        self.label_trainingPercent.setGeometry(QtCore.QRect(660, 30, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_trainingPercent.setFont(font)
        self.label_trainingPercent.setStyleSheet("color: rgb(162, 162, 162);")
        self.label_trainingPercent.setObjectName("label_trainingPercent")
        self.label_testData = QtWidgets.QLabel(self.centralwidget)
        self.label_testData.setGeometry(QtCore.QRect(760, 30, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_testData.setFont(font)
        self.label_testData.setStyleSheet("color: rgb(162, 162, 162);")
        self.label_testData.setObjectName("label_testData")
        self.label_testPercent = QtWidgets.QLabel(self.centralwidget)
        self.label_testPercent.setGeometry(QtCore.QRect(910, 30, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_testPercent.setFont(font)
        self.label_testPercent.setStyleSheet("color: rgb(162, 162, 162);")
        self.label_testPercent.setObjectName("label_testPercent")
        self.label_weight = QtWidgets.QLabel(self.centralwidget)
        self.label_weight.setGeometry(QtCore.QRect(510, 70, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_weight.setFont(font)
        self.label_weight.setStyleSheet("color: rgb(162, 162, 162);")
        self.label_weight.setObjectName("label_weight")
        self.label_weightValue = QtWidgets.QLabel(self.centralwidget)
        self.label_weightValue.setGeometry(QtCore.QRect(650, 70, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_weightValue.setFont(font)
        self.label_weightValue.setStyleSheet("color: rgb(162, 162, 162);")
        self.label_weightValue.setObjectName("label_weightValue")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(700, 110, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(200,200, 200);\n"
"background-color: rgb(100,100, 100);")
        self.pushButton.setObjectName("pushButton")
        self.progressBar_progress = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_progress.setGeometry(QtCore.QRect(0, 640, 1071, 23))
        self.progressBar_progress.setProperty("value", 0)
        self.progressBar_progress.setObjectName("progressBar_progress")
        self.progressBar_progress.raise_()
        self.picture_devidedLine.raise_()
        self.gridLayoutWidget.raise_()
        self.textArea_log.raise_()
        self.plot_trainingData.raise_()
        self.plot_testData.raise_()
        self.label_trainingData.raise_()
        self.label_trainingPercent.raise_()
        self.label_testData.raise_()
        self.label_testPercent.raise_()
        self.label_weight.raise_()
        self.label_weightValue.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked['bool'].connect(MainWindow.start_calculate)
        self.comboBox_filename.activated['QString'].connect(MainWindow.preview_picture)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "類神經網路 作業1 ── 感知姬"))
        self.label_hint_convergeCondition.setText(_translate("MainWindow", "次"))
        self.label_convergeCondition.setText(_translate("MainWindow", "收斂條件(迭代次數)"))
        self.label_studyScale.setText(_translate("MainWindow", "學習率"))
        self.label_filename.setText(_translate("MainWindow", "檔名"))
        self.textArea_log.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'PMingLiU\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_trainingData.setText(_translate("MainWindow", "訓練辨識度："))
        self.label_trainingPercent.setText(_translate("MainWindow", "???%"))
        self.label_testData.setText(_translate("MainWindow", "測試辨識度："))
        self.label_testPercent.setText(_translate("MainWindow", "???%"))
        self.label_weight.setText(_translate("MainWindow", "鍵結值(W)："))
        self.label_weightValue.setText(_translate("MainWindow", "[?, ?, ?, ?]"))
        self.pushButton.setText(_translate("MainWindow", "Start"))

