import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dimensionReduction.PCA import metricPCA

path_FCM = "C:/Users/Marina/degree_ML/FCM/clusters_"
k = 3
components = 2
dataset = pd.read_csv(path_FCM+str(k)+'/dataset.csv', header=None, index_col=None).values

n = dataset.shape[1]

from sklearn.preprocessing import StandardScaler

data = dataset.transpose()
data = StandardScaler().fit_transform(data)

from sklearn.decomposition import PCA

pca = PCA(n_components=components)
principalComponents = pca.fit_transform(data)

Xax = principalComponents[:, 0]
Yax = principalComponents[:, 1]
# Zax = principalComponents[:, 2]

# colors = ['#EE0000', '#FF6103', '#FFFF00', '#00FF7F', '#FF34B3', '#4B0082'] # '#008080', - 6
colors = ['#EE0000', '#FF6103', '#FFFF00']

fig = plt.figure(figsize=(7, 5))
ax = fig.add_subplot(111)
# ax = fig.add_subplot(111, projection='3d')

fig.patch.set_facecolor('white')
result = pd.read_csv(path_FCM + str(k) + '/FCM.csv', header=None, index_col=None).values
for t in range(0, k):
 probability = np.zeros(len(result[0]))
 for j in range(0, len(result[0])):
  probability[j] = result[t][j]
 ax.scatter(Xax, Yax, s=40, alpha=probability, c=colors[t],  marker='o', edgecolors="black")

plt.title("The Bhattacharyya distance")
# plt.title("The Euclidean distance")
ax.legend(["1", "2", "3"])
for t in range(0, k):
    ax.get_legend().legend_handles[t].set_alpha(1)

center_x = np.zeros(k)
center_y = np.zeros(k)
metricPCA(k)
center = pd.read_csv('C:/Users/Marina/degree_ML/dimensionReduction/PCA/clusters_' + str(k) + '/center_PCA.csv', header=None,
                     index_col=None).values
for t in range(0, k):
    center_x[t] = center[t][0]
    center_y[t] = center[t][1]

i = 200
while i < 90000:
    plt.scatter(center_x, center_y, s=i, facecolors='none', alpha=0.5, edgecolors=colors, linestyle='dashed')
    i *= 1.5
plt.axis('equal')

plt.scatter(center_x, center_y, s=400, marker="^", color=colors, edgecolors="black")

# ax.view_init(-140, -30)
plt.show()
