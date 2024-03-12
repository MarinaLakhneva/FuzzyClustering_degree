import pandas as pd

path_FCM = "FCM/clusters_"
path_PCA = "PCA/clusters_"

m_PC = [] # [0, 1]
m_MPC = []

def PC(k):
    for c in range(2, k + 1):
        u = pd.read_csv(path_FCM + str(c) + "/FCM.csv", header=None, index_col=None).values
        n = len(u[0])

        V_pc = 0.0
        for i in range(0, c):
            for j in range(0, n):
                V_pc += u[i][j]*u[i][j]
        variable = V_pc/n
        m_PC.append(variable)

        V_mpc = 1 - (k/(k-1))*(1-variable)
        m_MPC.append(V_mpc)
    print(m_MPC)
    return m_MPC
