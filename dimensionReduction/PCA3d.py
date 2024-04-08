import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

path_FCM = "C:/Users/Marina/degree_ML/FCM/clusters_"
k = 6
# хорды
# metrics = pd.read_csv("C:/Users/Marina/degree_ML/data/metrics_update.csv")
# property = metrics['OldChordDistribution']
#
# dataset = np.zeros((len(property[0].split()), len(property)))
# for i in range(0, len(property)):
#     for j in range(0, len(property[0].split())):
#         dataset[j][i] = list(map(float, property[i][1:-1].split()))[j]

# классика
metrics = pd.read_csv("C:/Users/Marina/degree_ML/data/metrics_for_classic.csv", usecols=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]).transpose()
dataset_m = pd.DataFrame(metrics)
dataset_m.to_csv(path_FCM + str(k) + "/dataset.csv", index=False, header=False)
dataset = pd.read_csv(path_FCM + str(k) + '/dataset.csv', header=None, index_col=None).values

from sklearn.preprocessing import StandardScaler

data = dataset.transpose()
data = StandardScaler().fit_transform(data)

from sklearn.decomposition import PCA

pca = PCA(n_components=3)
principalComponents = pca.fit_transform(data)

Xax = principalComponents[:, 0]
Yax = principalComponents[:, 1]
Zax = principalComponents[:, 2]

colors = ['#EE0000', '#FF6103', '#FFFF00', '#00FF7F', '#FF34B3', '#4B0082'] # '#008080', - 6

fig = plt.figure(figsize=(7, 5))
ax = fig.add_subplot(111, projection='3d')

fig.patch.set_facecolor('white')
result = pd.read_csv(path_FCM + str(k) + '/FCM.csv', header=None, index_col=None).values
for t in range(0, k):
 probability = np.zeros(len(result[0]))
 for j in range(0, len(result[0])):
  probability[j] = result[t][j]
 ax.scatter(Xax, Yax, Zax, s=40, alpha=probability, c=colors[t],  marker='o', edgecolors="black")

# ax.set_xlabel("PC 1", fontsize=14)
# ax.set_ylabel("PC 2", fontsize=14)
# ax.set_zlabel("PC 3", fontsize=14)

ax.legend(["1", "2", "3", "4", "5", "6"])
for t in range(0, k):
    ax.get_legend().legend_handles[t].set_alpha(1)
ax.view_init(-140, -30)
plt.show()
