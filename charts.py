import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dimensionReduction.PCA import p

path_FCM = "FCM/clusters_"
def charts(k):
    # metrics = pd.read_csv("data/metrics_update.csv")
    # property = metrics['OldChordDistribution']
    #
    # dataset = np.zeros((len(property[0].split()), len(property)))
    # for i in range(0, len(property)):
    #     for j in range(0, len(property[0].split())):
    #         dataset[j][i] = list(map(float, property[i][1:-1].split()))[j]
    #
    # n = len(property)

    metrics = pd.read_csv("data/metrics_for_classic.csv", usecols=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]).transpose()
    dataset_m = pd.DataFrame(metrics)
    dataset_m.to_csv(path_FCM + str(k) + "/dataset.csv", index=False, header=False)
    dataset = pd.read_csv(path_FCM + str(k) + '/dataset.csv', header=None, index_col=None).values

    n = dataset.shape[1]
    result = pd.read_csv(path_FCM + str(k) + '/FCM.csv', header=None, index_col=None).values

    from sklearn.preprocessing import StandardScaler

    data = dataset.transpose()
    data = StandardScaler().fit_transform(data)

    from sklearn.decomposition import PCA

    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(data)

    x = np.zeros(n)
    y = np.zeros(n)
    for i in range(0, n):
        x[i] = principalComponents[i][0]
        y[i] = principalComponents[i][1]

    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title('Clusters ', fontsize=20)
    ax.set_xlabel('PC 1', fontsize=15)
    ax.set_ylabel('PC 2', fontsize=15)
    colors = ['#EE0000', '#FF6103', '#FFFF00', '#00FF7F', '#FF34B3', '#4B0082'] # 6 был '#008080'
    for t in range(0, k):
        probability = np.zeros(len(result[0]))
        for j in range(0, len(result[0])):
            probability[j] = result[t][j]
        ax.scatter(x, y, s=100, alpha=probability, color=colors[t], edgecolors="black")
    ax.legend(["1", "2", "3", "4", "5", "6", "7"])
    for t in range(0, k):
        ax.get_legend().legend_handles[t].set_alpha(1)

    center_x = np.zeros(k)
    center_y = np.zeros(k)
    p(k)
    center = pd.read_csv('dimensionReduction/PCA/clusters_' + str(k) + '/center_PCA.csv', header=None,
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
    plt.show()