import random
import numpy as np
from random import shuffle


class Calculaor():
    def __init__(self, train_picture, test_picture):
        self.train_picture = train_picture
        self.test_picture = test_picture

    def initialize(self, study_scale, converger_condition, fileManager):
        # initialize essential variable
        self.done = False
        self.study_scale = study_scale
        self.converger_condition = converger_condition
        self.progress_percent = 0
        self.times = 0
        self.ratio_train = 0
        self.ratio_test = 0
        self.RMSE = 0
        self.w0 = random.uniform(-1, 1)
        self.w1 = random.uniform(-1, 1)
        self.w2 = random.uniform(-1, 1)
        self.k = 2
        self.train1 = fileManager.train1
        self.train2 = fileManager.train2
        self.test1 = fileManager.test1
        self.test2 = fileManager.test2
        self.data_merge()
        self.rbfn_point = []
        for i in range(self.k):
            self.rbfn_point.append(RBFN_Point(fileManager))

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

        self.test_data = []
        for i in range(len(self.test1["results"])):
            tmp = []
            tmp.append(self.test1["xs"][i])
            tmp.append(self.test1["ys"][i])
            tmp.append(self.test1["results"][i])
            self.test_data.append(tmp)
        for i in range(len(self.test2["results"])):
            tmp = []
            tmp.append(self.test2["xs"][i])
            tmp.append(self.test2["ys"][i])
            tmp.append(self.test2["results"][i])
            self.test_data.append(tmp)
        shuffle(self.test_data)

    def calculate(self, i):
        now = i % len(self.train_data)
        changed = False

        # use dot to calculate the result of data point
        tmp_w = np.array([self.w0, self.w1, self.w2])
        tmp_x = np.array([self.train_data[now][0:2]])
        tmp_x = np.array([-1, self.rbfn_point[0].get_y(tmp_x), self.rbfn_point[1].get_y(tmp_x)])
        F_of_X = np.dot(tmp_w, tmp_x)
        if F_of_X >= 0:
            tmp_result = 1
        else:
            tmp_result = 2

        # revise the wrong weight value
        if tmp_result != self.train_data[now][2] and self.done == False:
            changed = True
            tmp_m = [0, 0]
            tmp_ro = [0, 0]
            if tmp_result == 1:
                ################## weight, m, ro, theta gradient decent
                tmp_w[0] = tmp_w[0] + (self.study_scale * (-1 - F_of_X))
                for k in range(self.k):
                    tmp_w[k+1] = tmp_w[k+1] + (self.study_scale * (-1 - F_of_X) * tmp_x[k+1])
                    tmp_m[k] =self.rbfn_point[k].m + ((self.study_scale * (-1 - F_of_X) * tmp_w[k+1] * tmp_x[k+1] * (np.array([self.train_data[now][0:2]]) - self.rbfn_point[k].m)) / self.rbfn_point[k].ro**2)
                    tmp_ro[k] = self.rbfn_point[k].ro + (self.study_scale * (-1 - F_of_X) * tmp_w[k+1] * tmp_x[k+1] * (np.linalg.norm(np.array([self.train_data[now][0:2]]) - self.rbfn_point[k].m)**2) / self.rbfn_point[k].ro**3)
                
            elif (tmp_result == 2) and (self.train_data[now][2] == 0):
                pass
            else:
                ################## weight, m, ro, theta gradient decent
                tmp_w[0] = tmp_w[0] + (self.study_scale * (1 - F_of_X))
                for k in range(self.k):
                    tmp_w[k+1] = tmp_w[k+1] + (self.study_scale * (1 - F_of_X) * tmp_x[k+1])
                    tmp_m[k] = self.rbfn_point[k].m + ((self.study_scale * (1 - F_of_X) * tmp_w[k+1] * tmp_x[k+1] * (np.array([self.train_data[now][0:2]]) - self.rbfn_point[k].m)) / self.rbfn_point[k].ro**2)
                    tmp_ro[k] = self.rbfn_point[k].ro + (self.study_scale * (1 - F_of_X) * tmp_w[k+1] * tmp_x[k+1] * (np.linalg.norm(np.array([self.train_data[now][0:2]]) - self.rbfn_point[k].m)**2) / self.rbfn_point[k].ro**3)

            self.w0 = tmp_w[0]
            self.w1 = tmp_w[1]
            self.w2 = tmp_w[2]
            for k in range(self.k):
                self.rbfn_point[k].set_m(tmp_m[k])
                self.rbfn_point[k].set_ro(tmp_ro[k])

        # update value needed by GUI
        if changed:
            x_min, x_max, y_min, y_max = 9999, -9999, 9999, -9999
            data1, data2 = {"xs": [], "ys": []}, {"xs": [], "ys": []}
            for j in self.train_data:
                x = self.rbfn_point[0].get_y(np.array(j[0:2]))
                y = self.rbfn_point[1].get_y(np.array(j[0:2]))
                if x < x_min:
                    x_min = x
                if x > x_max:
                    x_max = x
                if y < y_min:
                    y_min = y
                if y > y_max:
                    y_max = y
                if j[2] == 1:
                    data1['xs'].append(x)
                    data1['ys'].append(y)
                else:
                    data2['xs'].append(x)
                    data2['ys'].append(y)
            self.train_picture.pre_plot(data1, data2, x_min, x_max, y_min, y_max)
            data1, data2 = {"xs": [], "ys": []}, {"xs": [], "ys": []}
            for j in self.test_data:
                x = self.rbfn_point[0].get_y(np.array(j[0:2]))
                y = self.rbfn_point[1].get_y(np.array(j[0:2]))
                if x < x_min:
                    x_min = x
                if x > x_max:
                    x_max = x
                if y < y_min:
                    y_min = y
                if y > y_max:
                    y_max = y
                if j[2] == 1:
                    data1['xs'].append(x)
                    data1['ys'].append(y)
                else:
                    data2['xs'].append(x)
                    data2['ys'].append(y)
            self.test_picture.pre_plot(data1, data2, x_min, x_max, y_min, y_max)

            self.transfer_data(self.train_picture)
            self.transfer_data(self.test_picture)
        
        self.progress_percent = int(i * 100 / self.converger_condition)

        # calculate correct ratio every 100 times
        self.times += 1
        if self.times % 100 == 0:
            self.ratio_calculate()

    def after_calculate(self):
        # last update the result of calculation
        self.transfer_data(self.train_picture)
        self.transfer_data(self.test_picture)
        self.ratio_calculate()

    def ratio_calculate(self):
        # calculate train and test correct ratio
        self.ratio_test = self.get_percent_RMSE(self.test_data)
        self.ratio_train = self.get_percent_RMSE(self.train_data)
        if self.ratio_train == 0:
            self.done = True
            self.ratio_train = 100
            self.ratio_test = 100 - self.ratio_test
        if self.ratio_train < 50:
            self.ratio_train = 100 - self.ratio_train
            self.ratio_test = 100 - self.ratio_test

    def get_percent_RMSE(self, data):
        # calculate the correct percent of data
        if len(data) < 1:
            return 0
        tmp_w = np.array([self.w0, self.w1, self.w2])
        right = 0
        error = 0
        for i in data:
            tmp_x = np.array(i[0:2])
            tmp_x = np.array([-1, self.rbfn_point[0].get_y(tmp_x), self.rbfn_point[1].get_y(tmp_x)])
            if np.dot(tmp_w, tmp_x) >= 0 and i[2] == 1:
                right += 1
            elif np.dot(tmp_w, tmp_x) <= 0 and (i[2] == 0 or i[2] == 2):
                right += 1
            else:
                error += 1
        error /= len(data)
        if error == 1:
            error = 0
        self.RMSE = error**(1/2)


        return (100 * right) / len(data)

    def transfer_data(self, picture):
        # send the line weight to picture drawer
        picture.get_weight_interval(self.w0, self.w1, self.w2)

class RBFN_Point():
    def __init__(self, fileManager):
        self.m = np.array([random.uniform(fileManager.x_min, fileManager.x_max), random.uniform(fileManager.y_min, fileManager.y_max)])
        self.ro = random.uniform(1, 10)

    def set_m(self, m):
        self.m = m

    def set_ro(self, ro):
        self.ro = ro
    
    def get_y(self, x):
        dist = np.linalg.norm(self.m - x)
        return  np.exp(float(-1 * (dist**2) / (2 * self.ro**2)))


