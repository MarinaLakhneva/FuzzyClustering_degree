import pandas as pd

path_FCM = "FCM/clusters_"
path_PCA = "PCA/clusters_"

m_PBMF = []

def PBMF(k):
    for c in range(2, k + 1):
        u = pd.read_csv(path_FCM + str(c) + "/FCM.csv", header=None, index_col=None).values
        distance = pd.read_csv(path_FCM + str(c) + "/distance.csv", header=None, index_col=None).values
        cluster_center = pd.read_csv(path_FCM + str(c) + "/cluster_center.csv", header=None, index_col=None).values
        n = len(distance[0])
        d = len(cluster_center)
        m = 2
        max = 0

        sum = 0.0
        for j in range(0, c):
            for i in range(0, n):
                sum += u[j][i]**m * distance[j][i]**2


        dist = 0.0
        for i in range(0, c):
            for j in range(i+1, c):
                for l in range(0, d):
                    dist += (cluster_center[l][i]-cluster_center[l][j])**2
                if(dist > max):
                    max = dist
                    dist = 0.0

        u1 = pd.read_csv(path_FCM + str(1) + "/FCM.csv", header=None, index_col=None).values
        distance1 = pd.read_csv(path_FCM + str(1) + "/distance.csv", header=None, index_col=None).values
        E1 = 0.0

        for i in range(0, n):
            E1 += u1[0][i]**m * distance1[0][i]**2

        V_pbmf = (1/k) * (E1 * max)/sum
        m_PBMF.append(V_pbmf)
    return m_PBMF