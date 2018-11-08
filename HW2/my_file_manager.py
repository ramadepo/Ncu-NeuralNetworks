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
        for i in os.listdir("./DataSet"):
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

        file = open('./DataSet/'+filename, 'r').read()
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
        self.test1 = {"xs": [], "ys": [], "results": []}
        self.train1 = {"xs": [], "ys": [], "results": []}
        self.test2 = {"xs": [], "ys": [], "results": []}
        self.train2 = {"xs": [], "ys": [], "results": []}
        self.devide_train_test(self.train1, self.test1, tmp1)
        self.devide_train_test(self.train2, self.test2, tmp2)

    def devide_train_test(self, train, test, tmp):
        # devide data to train and test
        for i in range(len(tmp["results"])):
            if i+1 < (len(tmp["results"])/3):
                test["xs"].append(tmp["xs"][i])
                test["ys"].append(tmp["ys"][i])
                test["results"].append(tmp["results"][i])
            else:
                train["xs"].append(tmp["xs"][i])
                train["ys"].append(tmp["ys"][i])
                train["results"].append(tmp["results"][i])
