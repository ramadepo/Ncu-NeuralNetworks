import os
from random import shuffle


class FileManager():
    def __init__(self, comboBox_filename):
        self.detect_files()
        for file in self.file_list:
            comboBox_filename.addItem(file)

    def detect_files(self):
        self.file_list = []
        for i in os.listdir("./DataSet"):
            if i.endswith(".txt"):
                self.file_list.append(i)
        self.file_list.sort()

    def scan_file(self, filename):
        tmp1 = {"xs": [], "ys": [], "results": []}
        tmp2 = {"xs": [], "ys": [], "results": []}

        file = open('./DataSet/'+filename, 'r').read()
        lines = file.split('\n')
        shuffle(lines)
        for line in lines:
            if len(line) > 1:
                x, y, result = line.split(' ')
                if result == "1":
                    tmp1["xs"].append(float(x))
                    tmp1["ys"].append(float(y))
                    tmp1["results"].append(float(result))
                elif result == "2" or result == "0":
                    tmp2["xs"].append(float(x))
                    tmp2["ys"].append(float(y))
                    tmp2["results"].append(float(result))

        self.divide_test_train(tmp1, tmp2)

    def divide_test_train(self, tmp1, tmp2):
        self.test1 = {"xs": [], "ys": [], "results": []}
        self.train1 = {"xs": [], "ys": [], "results": []}
        self.test2 = {"xs": [], "ys": [], "results": []}
        self.train2 = {"xs": [], "ys": [], "results": []}
        for i in range(len(tmp1["results"])):
            if i <= (len(tmp1["results"])/3):
                self.test1["xs"].append(tmp1["xs"][i])
                self.test1["ys"].append(tmp1["ys"][i])
                self.test1["results"].append(tmp1["results"][i])
            else:
                self.train1["xs"].append(tmp1["xs"][i])
                self.train1["ys"].append(tmp1["ys"][i])
                self.train1["results"].append(tmp1["results"][i])

        for i in range(len(tmp2["results"])):
            if i <= (len(tmp2["results"])/3):
                self.test2["xs"].append(tmp2["xs"][i])
                self.test2["ys"].append(tmp2["ys"][i])
                self.test2["results"].append(tmp2["results"][i])
            else:
                self.train2["xs"].append(tmp2["xs"][i])
                self.train2["ys"].append(tmp2["ys"][i])
                self.train2["results"].append(tmp2["results"][i])
