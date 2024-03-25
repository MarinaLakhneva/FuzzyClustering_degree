import pandas as pd
def interClusterDistance_sumsSquares(k, path_FCM):
    m_Q4 = []
    for cl in range(2, k + 1):
        cluster_center = pd.read_csv(path_FCM + str(cl) + '/cluster_center.csv', header=None, index_col=None).values
        d = len(cluster_center)
        dist = 0
        for c in range(0, cl+1):
            for j in range(c + 1, cl):
                for l in range(0, d):
                    dist += (cluster_center[l][c] - cluster_center[l][j]) ** 2
        m_Q4.append(dist)
    return m_Q4