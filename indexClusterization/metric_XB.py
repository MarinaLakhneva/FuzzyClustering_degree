import pandas as pd

path_FCM = "FCM/clusters_"
path_PCA = "PCA/clusters_"

m_XB = []

def XB(k):
    for c in range(2, k + 1):
        u = pd.read_csv(path_FCM + str(c) + "/FCM.csv", header=None, index_col=None).values
        distance = pd.read_csv(path_FCM + str(c) + "/distance.csv", header=None, index_col=None).values
        cluster_center = pd.read_csv(path_FCM + str(c) + "/cluster_center.csv", header=None, index_col=None).values
        n = len(distance[0])
        d = len(cluster_center)

        m = 2
        min = 1000

        sum = 0.0
        for j in range(0, c):
            for i in range(0, n):
                sum += u[j][i]**m * distance[j][i]**2


        dist = 0.0
        for i in range(0, c):
            for j in range(i+1, c):
                for l in range(0, d):
                    dist += (cluster_center[l][i]-cluster_center[l][j])**2
                if(dist < min):
                    min = dist
                    dist = 0.0

        V_xb = (1/n) * sum/min
        m_XB.append(V_xb)
    return m_XB