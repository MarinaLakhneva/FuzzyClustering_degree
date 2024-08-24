import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# k - количество кластеров 1<j<k
# d - размерность вектора данных 1<l<d
# n - мощность выборки


k = 6

# _str_ = "chords"
_str_ = "classic"

str_ = _str_ + "/dataset"
# str_ = _str_ + "/dataset_gauss"
# str_ = _str_ + "/dataset_gauss_"

path_FCM = "C:/Users/Marina/degree_ML/FCM/" + str_ + "/clusters_"
path = "C:/Users/Marina/degree_ML/data/dataset/" + str_ + ".csv"

dataset = pd.read_csv(path, header=None, index_col=None).values
print(dataset.shape)
n = dataset.shape[1]

result = pd.read_csv(path_FCM+str(k)+'/FCM.csv', header=None, index_col=None).values

metrics_spike = pd.read_csv("data/metrics_true.csv")
spike = metrics_spike['Spine File']

# metrics = pd.read_csv("data/metrics_true.csv", usecols=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]).transpose()
# dataset_ = pd.DataFrame(metrics)
# dataset_.to_csv("data/dataset11.csv", index=False, header=False)
dataset11 = pd.read_csv('data/dataset11.csv', header=None, index_col=None).values



for i in range(0, n):
    max_first = 0
    count_first = -1
    for j in range(0, k):
        if(max_first < result[j][i]):
            max_first = result[j][i]
            count_first = j
    if(max_first < 0.7):
        max_second = 0
        count_second = -1
        for x in range(0, k):
            if (max_first != result[x][i]):
                if (max_first - result[x][i] <= 0.1):
                    if (max_second < result[x][i]):
                        max_second = result[x][i]
                        count_second = x
        max_third = 0
        count_third = -1
        for y in range(0, k):
            if ((max_second != result[y][i]) & (max_first != result[y][i])):
                if (max_second - result[y][i] <= 0.1):
                    if (max_third < result[y][i]):
                        max_third = result[y][i]
                        count_third = y
        max_fourth = 0
        count_fourth = -1
        for z in range(0, k):
            if ((max_first != result[z][i]) & (max_second != result[z][i]) & (max_third != result[z][i])):
                if (max_third - result[z][i] <= 0.1):
                    if (max_fourth < result[z][i]):
                        max_fourth = result[z][i]
                        count_fourth = z
        if ((count_first != -1) & (count_second != -1) & (count_third != -1) & (count_fourth != -1)):
            print(i)
            print("n =", i, ":", spike[i])
            print(dataset11[:,i])
            print("cluster #", count_first, ":", max_first)
            print("cluster #", count_second, ":", max_second)
            print("cluster #", count_third, ":", max_third)
            print("cluster #", count_fourth, ":", max_fourth)