from FCM.FCM import fcm
# from analysis import info
from indexClusterization.metric_PC import PC
from indexClusterization.metric_XB import XB
from indexClusterization.metric_PBMF import PBMF
from indexClusterization.F_DWSVF import DWSVF

path_FCM = "FCM/clusters_"
# k - количество кластеров 1<j<k
# d - размерность вектора данных 1<l<d
# n - мощность выборки


def main(k):
    # for j in range(2, k+1):
    #     fcm(j)

    m_XB = XB(k)
    m_PBMF = PBMF(k)
    m_MPC = PC(k)

    m_DWSVF = DWSVF(k, m_XB, m_PBMF, m_MPC)


    import matplotlib.pyplot as plt
    x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    plt.plot(x, m_DWSVF, 'ms-', alpha=0.3, label="DWSVF")
    plt.grid(True)
    plt.xlabel("cluster number", fontweight='bold', fontsize="large")
    plt.ylabel("quality metric", fontweight='bold', fontsize="large")
    plt.legend()
    plt.show()

    # for j in range(2, k + 1):
    #     info(j)
    # info(k)

if __name__ == '__main__':
    k = 14
    main(k)