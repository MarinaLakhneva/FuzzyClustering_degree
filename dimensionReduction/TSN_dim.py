import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dimensionReduction.TSN import metricTSN

path_FCM = "C:/Users/Marina/degree_ML/FCM/clusters_"
k = 3
components = 2

dataset = pd.read_csv(path_FCM+str(k)+'/dataset_gauss_C.csv', header=None, index_col=None).values

from sklearn.preprocessing import StandardScaler

data = dataset.transpose()
data = StandardScaler().fit_transform(data)

from sklearn.manifold import TSNE

tsne = TSNE(n_components=components, random_state=0)
principalComponents = tsne.fit_transform(data)

Xax = principalComponents[:, 0]
Yax = principalComponents[:, 1]
# Zax = principalComponents[:, 2]
#
# colors = ['#EE0000', '#FF6103', '#FFFF00', '#00FF7F', '#FF34B3', '#008080', '#4B0082'] # '#008080', - 6
colors = ['#EE0000', '#FF6103', '#FFFF00']

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

plt.title("The Bhattacharyya distance")
# plt.title("The Euclidean distance")
ax.legend(["1", "2", "3"])
for t in range(0, k):
    ax.get_legend().legend_handles[t].set_alpha(1)

# ax.view_init(-140, -30)
plt.show()
