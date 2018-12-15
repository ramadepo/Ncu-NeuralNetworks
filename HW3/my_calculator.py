import random
import numpy as np
from random import shuffle


class Calculaor():
    def __init__(self, train_picture):
        self.train_picture = train_picture

    def initialize(self, converger_condition, topology_size_i, topology_size_j, fileManager):
        # initialize essential variable
        self.converger_condition = converger_condition
        self.topology_size_i = topology_size_i
        self.topology_size_j = topology_size_j
        self.progress_percent = 0
        self.times = 0
        self.train1 = fileManager.train1
        self.train2 = fileManager.train2
        self.data_merge()
        self.matrix = self.construct_matrix(fileManager.x_min, fileManager.x_max, fileManager.y_min, fileManager.y_max)
        self.transfer_matrix()
        self.last_winner = [-1, -1]

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

    def construct_matrix(self, x_min, x_max, y_min, y_max):
        matrix = []
        for i in range(self.topology_size_i):
            matrix.append([0] * self.topology_size_j)
        for i in range(self.topology_size_i):
            for j in range(self.topology_size_j):
                x = random.uniform(x_min, x_max)
                y = random.uniform(y_min, y_max)
                matrix[i][j] = np.array([x, y])
        return matrix

    def calculate(self, i):
        now = i % len(self.train_data)
        # calculate the relationship with matrix and data to build SOM
        x = self.train_data[now][0]
        y = self.train_data[now][1]
        target = np.array([x, y])
        winner = self.get_winner(target)
        self.winner_update(winner[0], winner[1], target, i)

        self.calculate_bottom(i)

    def winner_update(self, win_i, win_j, target, i):
        if i <= 1000:
            study_rate = 0.9 * (1 - (i/1000))
        else:
            study_rate = 0.01
        size = max(int(max(self.topology_size_i, self.topology_size_j)/2) - int(i/1000), 1)

        for i in range(self.topology_size_i):
            for j in range(self.topology_size_j):
                if abs(win_i-i) <= size and abs(win_j-j) <= size:
                    self.matrix[i][j] = self.matrix[i][j] + (study_rate * (target - self.matrix[i][j]))

    def get_winner(self, target):
        winner = [-1, -1]
        win_distance = 9999
        for i in range(self.topology_size_i):
            for j in range(self.topology_size_j):
                distance = np.linalg.norm(self.matrix[i][j] - target)
                if distance < win_distance:
                    if [i, j] != self.last_winner:
                        win_distance = distance
                        winner = [i, j]
        self.last_winner = winner
        return winner

    def after_calculate(self):
        self.transfer_matrix()

    def calculate_bottom(self, i):
        # update value needed by GUI
        self.progress_percent = int(i * 100 / self.converger_condition)

        # every 100 times
        self.times += 1
        if self.times%100 == 0:
            self.transfer_matrix()
        # Kohonen: shuffle in every learning loop
        if self.times%len(self.train_data) == 0:
            shuffle(self.train_data)

    def transfer_matrix(self):
        self.train_picture.get_matrix(self.matrix, self.topology_size_i, self.topology_size_j)
