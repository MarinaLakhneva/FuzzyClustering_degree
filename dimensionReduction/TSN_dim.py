import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dimensionReduction.TSN import metricTSN

str_ = "chords/dataset"
# str_ = "classic/dataset"

path_FCM = "C:/Users/Marina/degree_ML/FCM/" + str_ + "/clusters_"
path = "C:/Users/Marina/degree_ML/data/dataset/" + str_ + ".csv"

k = 7
components = 2
dataset = pd.read_csv(path, header=None, index_col=None).values

from sklearn.preprocessing import StandardScaler

data = dataset.transpose()
data = StandardScaler().fit_transform(data)

from sklearn.manifold import TSNE

tsne = TSNE(n_components=components, random_state=0)
principalComponents = tsne.fit_transform(data)

Xax = principalComponents[:, 0]
Yax = principalComponents[:, 1]
# Zax = principalComponents[:, 2]

colors = ['#f00', '#0f0', '#ff3bb0', '#ff0', '#800080', '#008080', '#1ae4ff']

fig = plt.figure(figsize=(7, 5))
# ax = fig.add_subplot(111, projection='3d')
ax = fig.add_subplot(111)

fig.patch.set_facecolor('white')
result = pd.read_csv(path_FCM + str(k) + '/FCM.csv', header=None, index_col=None).values
for t in range(0, k):
 probability = np.zeros(len(result[0]))
 for j in range(0, len(result[0])):
  probability[j] = result[t][j]
 ax.scatter(Xax, Yax, s=40, alpha=probability, c=colors[t],  marker='o', edgecolors="black")
 # ax.scatter(Xax, Yax, Zax, s=40, alpha=probability, c=colors[t], marker='o', edgecolors="black")


ax.legend(["1", "2", "3", "4", "5", "6", "7"])
for t in range(0, k):
    ax.get_legend().legend_handles[t].set_alpha(1)

# ax.view_init(-140, -30)
plt.show()
