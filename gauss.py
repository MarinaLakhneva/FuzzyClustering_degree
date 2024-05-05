import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import multivariate_normal

metrics = pd.read_csv("data/metrics_update.csv")
OldChordDistribution_metric = metrics['OldChordDistribution']

dataset = np.zeros((len(OldChordDistribution_metric[0].split()), len(OldChordDistribution_metric)))
for i in range(0, len(OldChordDistribution_metric)):
    for j in range(0, len(OldChordDistribution_metric[0].split())):
        dataset[j][i] = list(map(float, OldChordDistribution_metric[i][1:-1].split()))[j]

dataset_for_PCA = pd.DataFrame(dataset)
dataset_for_PCA.to_csv("data/dataset.csv", index=False, header=False)
dataset = pd.read_csv('data/dataset.csv', header=None, index_col=None).values

n = len(OldChordDistribution_metric)
d = len(OldChordDistribution_metric[0].split())

data = pd.read_csv('data/dataset.csv', header=None, index_col=None).values
x = data.transpose()


mean_ = np.mean(x, axis=0)
# print(mean_)

cov_ = np.cov(data, bias=True)
# print(cov_)

print(np.random.multivariate_normal(mean_, cov_, size=331))
print(np.random.multivariate_normal(mean_, cov_, size=331).shape)