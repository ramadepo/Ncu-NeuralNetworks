import random
import numpy as np


class Calculaor():
    def __init__(self, train_picture, test_picture, fileManager):
        self.train_picture = train_picture
        self.test_picture = test_picture
        self.fileManager = fileManager

    def initialize(self, study_scale, converger_condition):
        self.study_scale = study_scale
        self.converger_condition = converger_condition
        self.w0 = 0
        self.w1 = random.uniform(-1, 1)
        self.w2 = random.uniform(-1, 1)

    def calculate(self):
        self.w0 = 0
        self.w1 = random.uniform(-1, 1)
        self.w2 = random.uniform(-1, 1)

        self.transfer_data_train()
        self.transfer_data_test()

    def after_calculate(self):
        self.transfer_data_train()
        self.transfer_data_test()

    def transfer_data_train(self):
        self.train_picture.get_weight_interval(
            self.w0, self.w1, self.w2, self.fileManager.x_min, self.fileManager.x_max)

    def transfer_data_test(self):
        self.test_picture.get_weight_interval(
            self.w0, self.w1, self.w2, self.fileManager.x_min, self.fileManager.x_max)
