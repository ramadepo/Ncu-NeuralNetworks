import os
from random import shuffle


class FileManager():
    def __init__(self, comboBox_filename):
        # set combo box list
        self.detect_files()
        for file in self.file_list:
            comboBox_filename.addItem(file)

    def detect_files(self):
        # find all file in Dataset directory
        self.file_list = []
        for i in os.listdir("./DataSet/SOM_dataset"):
            if i.endswith(".txt"):
                self.file_list.append(i)
        self.file_list.sort()

    def scan_file(self, filename):
        # read selected file's data and set border value
        self.x_max = -9999
        self.x_min = 9999
        self.y_max = -9999
        self.y_min = 9999
        tmp1 = {"xs": [], "ys": [], "results": []}
        tmp2 = {"xs": [], "ys": [], "results": []}

        file = open('./DataSet/SOM_dataset/'+filename, 'r').read()
        lines = file.split('\n')
        shuffle(lines)
        for line in lines:
            if len(line) > 1:
                x, y, result = line.split(' ')
                if float(x) < self.x_min:
                    self.x_min = float(x)
                if float(x) > self.x_max:
                    self.x_max = float(x)
                if float(y) < self.y_min:
                    self.y_min = float(y)
                if float(y) > self.y_max:
                    self.y_max = float(y)
                if result == "1":
                    tmp1["xs"].append(float(x))
                    tmp1["ys"].append(float(y))
                    tmp1["results"].append(float(result))
                elif result == "2" or result == "0":
                    tmp2["xs"].append(float(x))
                    tmp2["ys"].append(float(y))
                    tmp2["results"].append(float(result))

        self.divide_data(tmp1, tmp2)

    def divide_data(self, tmp1, tmp2):
        # initailize the variable to store initial data
        self.train1 = {"xs": [], "ys": [], "results": []}
        self.train2 = {"xs": [], "ys": [], "results": []}
        self.store_train(self.train1, tmp1)
        self.store_train(self.train2, tmp2)

    def store_train(self, train, tmp):
        # store data to train
        for i in range(len(tmp["results"])):
            train["xs"].append(tmp["xs"][i])
            train["ys"].append(tmp["ys"][i])
            train["results"].append(tmp["results"][i])
