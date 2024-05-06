import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

metrics = pd.read_csv("data/metrics_update.csv")
OldChordDistribution_metric = metrics['OldChordDistribution']

dataset = pd.read_csv('data/dataset_gauss.csv', header=None, index_col=None).values

n = len(OldChordDistribution_metric)
d = len(OldChordDistribution_metric[0].split())
print("data", dataset)

data = np.empty((0, dataset.shape[1]))

count = []
for i in range(d):
    sorted_row = np.sort(dataset[i, :]).reshape(1, -1)
    data = np.vstack([data, sorted_row])
    neg_count = sum(1 for x in dataset[i, :] if x < 0)
    count.append(neg_count)
# print(count)
print("data_update", data)
print(data[:, 0])

