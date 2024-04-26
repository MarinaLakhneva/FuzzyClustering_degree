import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import umap.umap_ as umap

path_FCM = "C:/Users/Marina/degree_ML/FCM/clusters_"
k = 3
components = 2
dataset = pd.read_csv(path_FCM+str(k)+'/dataset.csv', header=None, index_col=None).values

from sklearn.preprocessing import StandardScaler

data = dataset.transpose()
data = StandardScaler().fit_transform(data)

fit = umap.UMAP(
    n_neighbors=15,
    min_dist=0.0,
    n_components=components,
    metric='euclidean'
)
u = fit.fit_transform(data)
fig = plt.figure()


# ax = fig.add_subplot(111, projection='3d')
ax = fig.add_subplot(111)
# colors = ['#EE0000', '#FF6103', '#FFFF00', '#00FF7F', '#FF34B3', '#4B0082'] #'#008080', - 6
colors = ['#EE0000', '#FF6103', '#FFFF00']

result = pd.read_csv(path_FCM + str(k) + '/FCM_.csv', header=None, index_col=None).values
for t in range(0, k):
 probability = np.zeros(len(result[0]))
 for j in range(0, len(result[0])):
  probability[j] = result[t][j]
 ax.scatter(u[:, 0], u[:, 1], alpha=probability, c=colors[t], s=40, marker='o', edgecolors="black")
 # ax.scatter(u[:, 0], u[:, 1], u[:, 2], alpha=probability, c=colors[t], s=40)
# ax.view_init(-140, 30)
# plt.title("The Bhattacharyya distance")
plt.title("The Euclidean distance")
plt.show()