import matplotlib.pyplot as plt
import pandas as pd
from FCM.FCM import fcm
from dimensionReduction.PCA import pca
from analysis import general
from indexClusterization.elbow import elbow
from indexClusterization.metric_PC import PC
from indexClusterization.metric_XB import XB
from indexClusterization.metric_PBMF import PBMF
from indexClusterization.F_DWSVF import DWSVF
from indexClusterization.interClusterDist import interClusterDistance
from indexClusterization.interClusterDist_ss import interClusterDistance_sumsSquares
from indexClusterization.intraClusterDist_ss import intraClusterDistances_sumsSquares

path_FCM = "FCM/clusters_"
# k - количество кластеров 1<j<k
# d - размерность вектора данных 1<l<d
# n - мощность выборки

def main(k):
    # время работы алгоритма
    # import datetime
    # for j in range(1, k + 1):
    #     # фиксируем и выводим время старта работы кода
    #     start = datetime.datetime.now()
    #     print('Время старта: ' + str(start))
    #
    #     # код, время работы которого измеряем
    #     fcm(j)
    #     #фиксируем и выводим время окончания работы кода
    #     finish = datetime.datetime.now()
    #     print('Время окончания: ' + str(finish))
    #
    #     # вычитаем время старта из времени окончания
    #     print('Время работы: ' + str(finish - start))
#-----------------------------------------------------------------------------------------------------------------------
    # метод локтя
    # eb = elbow(k)
    # x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    # plt.plot(x, eb, 'ro-', alpha=0.6)
    # plt.grid(True)
    # plt.title("The Elbow Method")
    # plt.xlabel("cluster number", fontweight='bold', fontsize="large")
    # plt.ylabel("wcss", fontweight='bold', fontsize="large")
    # plt.show()
#-----------------------------------------------------------------------------------------------------------------------
    # m_MPC = PC(k)
    # plt.plot(x, m_MPC, 'b+-', alpha=0.3, label="MPC")

    # m_XB = XB(k)
    # plt.plot(x, m_XB, 'g^-', alpha=0.3, label="XB")

    # m_PBMF = PBMF(k)
    # plt.plot(x, m_PBMF, 'ro-', alpha=0.3, label="PBMF")

    # m_DWSVF = DWSVF(k, m_XB, m_PBMF, m_MPC)
    # plt.plot(x, m_DWSVF, color = 'olive' , marker='s', alpha=0.3, label="DWSVF")

    # plt.grid(True)
    # plt.xlabel("cluster number", fontweight='bold', fontsize="large")
    # plt.ylabel("quality metric", fontweight='bold', fontsize="large")
    # plt.legend()
    # plt.show()
#-----------------------------------------------------------------------------------------------------------------------
    # for j in range(1, k + 1):
    #     interClusterDistance(j, path_FCM)

    # Q3 = intraClusterDistances_sumsSquares(k, path_FCM)
    # x = [2, 3, 4, 5, 6, 7, 8]
    # plt.plot(x, Q3, 'mo-', alpha=0.6)
    # plt.grid(True)
    # plt.xlabel("cluster number", fontweight='bold', fontsize="large")
    # plt.ylabel("sums of squares of intra-cluster distances", fontweight='bold', fontsize="large")
    # plt.show()

    # Q4 = interClusterDistance_sumsSquares(k, path_FCM)
    # # x = [2, 3, 4, 5, 6, 7, 8]
    # # plt.plot(x, Q4, 'ro-', alpha=0.6)
    # # plt.grid(True)
    # # plt.xlabel("cluster number", fontweight='bold', fontsize="large")
    # # plt.ylabel("sums of squares of inter-cluster distances", fontweight='bold', fontsize="large")
    # # plt.show()

    # Q = []
    # for j in range(0, k-1):
    #     param = Q4[j]/Q3[j]
    #     Q.append(param)
    # x = [2, 3, 4, 5, 6, 7, 8]
    # plt.plot(x, Q, 'b^-', alpha=0.6)
    # plt.grid(True)
    # plt.xlabel("cluster number", fontweight='bold', fontsize="large")
    # plt.ylabel("intercluster distance / intracluster distance", fontweight='bold', fontsize="large")
    # plt.show()


if __name__ == '__main__':
    k = 5
    main(k)