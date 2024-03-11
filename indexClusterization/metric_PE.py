import math
import pandas as pd

path_FCM = "FCM/clusters_"
path_PCA = "PCA/clusters_"

m_PE = [] # [0, log("+str(k)+", 2)]
m_MPE = []

def PE(k):
    for c in range(2, k + 1):
        u = pd.read_csv(path_FCM + str(k) + "/FCM.csv", header=None, index_col=None).values
        n = len(u[0])

        V_pe = 0.0
        for i in range(0, k):
            for j in range(0, n):
                V_pe += u[i][j] * math.log(u[i][j], 2)

        variable = - V_pe/n
        m_PE.append(variable)

        V_mpe = (n/(n-k))*V_pe
        m_MPE.append(V_mpe)

    return m_PE