import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


path_FCM = "FCM/clusters_"
def charts(k):
    metrics = pd.read_csv("data/metrics_update.csv")
    metric = metrics['OldChordDistribution']

    dataset = np.zeros((len(metric[0].split()), len(metric)))
    for i in range(0, len(metric)):
        for j in range(0, len(metric[0].split())):
            dataset[j][i] = list(map(float, metric[i][1:-1].split()))[j]

    number_of_elements = len(metric)

    # 11-ть метрик
    # dataset = pd.read_csv(path_FCM + str(number_of_clusters) + '/dataset.csv', header=None, index_col=None).values
    # number_of_elements = dataset.shape[1]

    result = pd.read_csv('FCM/clusters_' + str(k) + '/FCM.csv', header=None, index_col=None).values
    #------------------------------------------------------PCA-------------------------------------------------------------
    from sklearn.preprocessing import StandardScaler

    data = dataset.transpose()
    data = StandardScaler().fit_transform(data)

    from sklearn.decomposition import PCA

    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(data)

    x = np.zeros(number_of_elements)
    y = np.zeros(number_of_elements)
    for i in range(0, number_of_elements):
        x[i] = principalComponents[i][0]
        y[i] = principalComponents[i][1]
    # ------------------------------------------------------TSN-------------------------------------------------------------
    # from sklearn.manifold import TSNE
    #
    # data = dataset.transpose()
    # data = StandardScaler().fit_transform(data)
    #
    # tsne = TSNE(n_components=2, random_state=0)
    # projections = tsne.fit_transform(data)
    #
    #
    # x = np.zeros(number_of_elements)
    # y = np.zeros(number_of_elements)
    # for i in range(0, number_of_elements):
    #     x[i] = projections[i][0]
    #     y[i] = projections[i][1]

    #---------------------------------------------------графики------------------------------------------------------------

    for k in range(0, k):
        fig = plt.figure(figsize=(20, 10))
        ax = fig.add_subplot(1, 1, 1)
        ax.set_xlabel('Principal Component 1', fontsize=15)
        ax.set_ylabel('Principal Component 2', fontsize=15)
        ax.set_title('Cluster ' + str(k + 1), fontsize=20)
        probability = np.zeros(len(result[0]))
        for j in range(0, len(result[0])):
            probability[j] = result[k][j]
        ax.scatter(x, y, s=60, alpha=0.5, c=probability, cmap="PuRd", edgecolors="black")
        # plt.savefig('/Users/Marina/degree_ML/charts/clusters_'+str(number_of_clusters)+'/cluster_'+str(k+1)+'.png')
        plt.show()

    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title('Clusters ', fontsize=20)
    ax.set_xlabel('Principal Component 1', fontsize=15)
    ax.set_ylabel('Principal Component 2', fontsize=15)
    colors = ['#ea9999', '#ffe599', '#b6d7a8', '#9fc5e8', '#d9d2e9']
    for k in range(0, k):
        probability = np.zeros(len(result[0]))
        for j in range(0, len(result[0])):
            probability[j] = result[k][j]
        ax.scatter(x, y, s=60, alpha=probability, color=colors[k], edgecolors="black")
    ax.legend(["1", "2", "3", "4", "5"])
    for k in range(0, k):
        ax.get_legend().legend_handles[k].set_alpha(1)
    center_x = np.zeros(k)
    center_y = np.zeros(k)
    # ВЫБЕРИ МЕТОД СОКРАЩЕНИЯ РАЗМЕРНОСТИ
    center = pd.read_csv('PCA/clusters_' + str(k) + '/center_PCA.csv', header=None, index_col=None).values
    for k in range(0, k):
        center_x[k] = center[k][0]
        center_y[k] = center[k][1]
    print(center_x)
    print(center_y)
    # center_color = ['#ea9999', '#ffe599', '#b6d7a8']
    center_color = ['#ea9999', '#ffe599', '#b6d7a8', '#9fc5e8', '#d9d2e9']
    plt.scatter(center_x, center_y, s=80, marker="^", color=center_color, edgecolors="red")
    # plt.savefig('/Users/Marina/degree_ML/charts/clusters_'+str(number_of_clusters)+'/clusters'+str(number_of_clusters)+'.png')
    plt.show()

    distance = pd.read_csv('FCM/clusters_' + str(k) + '/distance.csv', header=None, index_col=None).values
    dist_1 = []
    dist_2 = []
    dist_3 = []
    dist_4 = []
    dist_5 = []

    for i in range(0, number_of_elements):
        count_cluster = 0
        min_dist = 1000
        for k in range(0, k):
            if (min_dist > distance[k][i]):
                min_dist = distance[k][i]
                count_cluster = k + 1
        if (count_cluster == 1):
            dist_1.append(min_dist)
        elif (count_cluster == 2):
            dist_2.append(min_dist)
        elif (count_cluster == 3):
            dist_3.append(min_dist)
        elif (count_cluster == 4):
            dist_4.append(min_dist)
        elif (count_cluster == 5):
            dist_5.append(min_dist)

    plt.xlabel('Number of clusters')
    plt.ylabel('distance')
    plt.title('Intracluster distance')
    y_dist_1 = np.ones(len(dist_1))
    y_dist_2 = np.ones(len(dist_2))
    y_dist_3 = np.ones(len(dist_3))
    y_dist_4 = np.ones(len(dist_4))
    y_dist_5 = np.ones(len(dist_5))

    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    s5 = 0
    for d_1 in range(0, len(dist_1)):
        s1 += dist_1[d_1]
    plt.plot(y_dist_1, dist_1, color="#ea9999")
    for d_2 in range(0, len(dist_2)):
        y_dist_2[d_2] = 2
        s2 += dist_2[d_2]
    plt.plot(y_dist_2, dist_2, color="#ffe599")
    for d_3 in range(0, len(dist_3)):
        y_dist_3[d_3] = 3
        s3 += dist_3[d_3]
    plt.plot(y_dist_3, dist_3, color="#b6d7a8")
    for d_4 in range(0, len(dist_4)):
        y_dist_4[d_4] = 4
        s4 += dist_4[d_4]
    plt.plot(y_dist_4, dist_4, color="#9fc5e8")
    for d_5 in range(0, len(dist_5)):
        y_dist_5[d_5] = 5
        s5 += dist_5[d_5]
    plt.plot(y_dist_5, dist_5, color="#d9d2e9")
    plt.legend([round(s1), round(s2), round(s3)])
    plt.legend([round(s1), round(s2), round(s3), round(s4), round(s5)])
    plt.show()
