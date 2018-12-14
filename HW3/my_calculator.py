import random
import numpy as np
from random import shuffle


class Calculaor():
    def __init__(self, train_picture):
        self.train_picture = train_picture

    def initialize(self, converger_condition, fileManager):
        # initialize essential variable
        self.study_scale = 0
        self.converger_condition = converger_condition
        self.progress_percent = 0
        self.times = 0
        self.train1 = fileManager.train1
        self.train2 = fileManager.train2
        self.data_merge()

    def data_merge(self):
        # combine result 1 and 2 data then shuffle
        self.train_data = []
        for i in range(len(self.train1["results"])):
            tmp = []
            tmp.append(self.train1["xs"][i])
            tmp.append(self.train1["ys"][i])
            tmp.append(self.train1["results"][i])
            self.train_data.append(tmp)
        for i in range(len(self.train2["results"])):
            tmp = []
            tmp.append(self.train2["xs"][i])
            tmp.append(self.train2["ys"][i])
            tmp.append(self.train2["results"][i])
            self.train_data.append(tmp)
        shuffle(self.train_data)

    def calculate(self, i):
        now = i % len(self.train_data)


        # update value needed by GUI
        self.progress_percent = int(i * 100 / self.converger_condition)

        # every 100 times
        self.times += 1
        if self.times%100 == 0:
            pass

    def after_calculate(self):
        pass

