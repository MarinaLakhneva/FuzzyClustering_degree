import pandas as pd
def interClusterDistance(k, path_FCM):
    cluster_center = pd.read_csv(path_FCM + str(k) + '/cluster_center.csv', header=None, index_col=None).values
    d = len(cluster_center)
    dist = 0
    for i in range(0, k):
        for j in range(i + 1, k):
            for l in range(0, d):
                dist += (cluster_center[l][i] - cluster_center[l][j]) ** 2
            print(dist)
            dist = 0