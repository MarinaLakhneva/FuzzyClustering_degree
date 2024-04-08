import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import umap.umap_ as umap

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

fit = umap.UMAP(
    n_neighbors=15,
    min_dist=0.0,
    n_components=3,
    metric='euclidean'
)
u = fit.fit_transform(data);
fig = plt.figure()


# ax = fig.add_subplot(111, projection='3d')
ax = fig.add_subplot(111)
colors = ['#EE0000', '#FF6103', '#FFFF00', '#00FF7F', '#FF34B3', '#4B0082'] #'#008080', - 6

result = pd.read_csv(path_FCM + str(k) + '/FCM.csv', header=None, index_col=None).values
for t in range(0, k):
 probability = np.zeros(len(result[0]))
 for j in range(0, len(result[0])):
  probability[j] = result[t][j]
 ax.scatter(u[:, 0], u[:, 1], alpha=probability, c=colors[t], s=40)
 # ax.scatter(u[:, 0], u[:, 1], u[:, 2], alpha=probability, c=colors[t], s=40)
# ax.view_init(-140, 30)
plt.show()




# reducer = umap.UMAP()
#
# path_FCM = "C:/Users/Marina/degree_ML/FCM/clusters_"
# k = 7
# metrics = pd.read_csv("C:/Users/Marina/degree_ML/data/metrics_update.csv")
# property = metrics['OldChordDistribution']
#
# dataset = np.zeros((len(property[0].split()), len(property)))
# for i in range(0, len(property)):
#     for j in range(0, len(property[0].split())):
#         dataset[j][i] = list(map(float, property[i][1:-1].split()))[j]
#
# from sklearn.preprocessing import StandardScaler
#
# data = dataset.transpose()
# data = StandardScaler().fit_transform(data)
# embedding = reducer.fit_transform(data)
#
# colors = ['#EE0000', '#FF6103', '#FFFF00', '#00FF7F', '#FF34B3', '#008080', '#4B0082']
#
# result = pd.read_csv(path_FCM + str(k) + '/FCM.csv', header=None, index_col=None).values
# for t in range(0, k):
#  probability = np.zeros(len(result[0]))
#  for j in range(0, len(result[0])):
#   probability[j] = result[t][j]
#  plt.scatter(embedding[:, 0], embedding[:, 1], s=40, alpha=probability, c=colors[t])
#
# plt.gca().set_aspect('equal', 'datalim')
# plt.show()