import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import umap.umap_ as umap

# str_ = "chords/dataset"
str_ = "classic/dataset"

path_FCM = "C:/Users/Marina/degree_ML/FCM/" + str_ + "/clusters_"
path = "C:/Users/Marina/degree_ML/data/dataset/" + str_ + ".csv"
path_accessories = "C:/Users/Marina/degree_ML/FCM/accessories/clusters_"
path_u = "C:/Users/Marina/degree_ML/dimensionReduction/UMAP"

k = 6
components = 2
# dataset = pd.read_csv(path, header=None, index_col=None).values
#
# from sklearn.preprocessing import StandardScaler
#
# data = dataset.transpose()
# data = StandardScaler().fit_transform(data)
#
# fit = umap.UMAP(
#     n_neighbors=15,
#     min_dist=0.0,
#     n_components=components,
#     metric='euclidean'
# )
# u = fit.fit_transform(data)
# print(u)
#
# u_ = pd.DataFrame(u)
# u_.to_csv(path_u+"/u_classic.csv", index=False, header=False)

_u_ = pd.read_csv(path_u + '/u_classic.csv', header=None, index_col=None).values
fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
ax = fig.add_subplot(111)
colors = ['#f00', '#0f0', '#ff3bb0', '#ff0', '#800080', '#1ae4ff'] #, '#ff7b00' - 8 '#008080', - 6

result = pd.read_csv(path_accessories + str(k) + '/table_of_accessories.csv', header=None, index_col=None).values
# result = pd.read_csv(path_FCM + str(k) + '/FCM.csv', header=None, index_col=None).values
for t in range(0, k):
    probability = np.zeros(len(result[0]))
    for j in range(0, len(result[0])):
        probability[j] = result[t][j]
    ax.scatter(_u_[:, 0], _u_[:, 1], alpha=probability, c=colors[t], s=40, marker='o', edgecolors="black")
    # ax.scatter(u[:, 0], u[:, 1], u[:, 2], alpha=probability, c=colors[t], s=40)
# ax.view_init(-140, 30)
ax.legend(["1", "2", "3", "4", "5", "6"])
for t in range(0, k):
    ax.get_legend().legend_handles[t].set_alpha(1)
plt.savefig("C:/Users/Marina/degree_ML/pic/" + str_ + "/umap0.png")
plt.show()