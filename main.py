import matplotlib.pyplot as plt
from FCM.FCM import fcm
from analysis import info
from indexClusterization.elbow import elbow
from indexClusterization.metric_PC import PC
from indexClusterization.metric_XB import XB
from indexClusterization.metric_PBMF import PBMF
from indexClusterization.F_DWSVF import DWSVF

path_FCM = "FCM/clusters_"
# k - количество кластеров 1<j<k
# d - размерность вектора данных 1<l<d
# n - мощность выборки


def main(k):
    # время работы алгоритма

    # import datetime
    # # фиксируем и выводим время старта работы кода
    # start = datetime.datetime.now()
    # print('Время старта: ' + str(start))
    #
    # # код, время работы которого измеряем
    # fcm(k)
    # #фиксируем и выводим время окончания работы кода
    # finish = datetime.datetime.now()
    # print('Время окончания: ' + str(finish))
    #
    # # вычитаем время старта из времени окончания
    # print('Время работы: ' + str(finish - start))

    # Время старта: 2024 - 03 - 12 14:52:22.058615
    # 8
    # Время окончания: 2024 - 03 - 12 14:53:49.892222
    # Время работы: 0:01:27.833607
    # m_XB = XB(k)
    # m_PBMF = PBMF(k)
    # m_MPC = PC(k)

    # метрики качества кластеризации

    # m_DWSVF = DWSVF(k, m_XB, m_PBMF, m_MPC)
    #
    #
    # import matplotlib.pyplot as plt
    # x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    #
    # plt.plot(x, m_DWSVF, 'ms-', alpha=0.3, label="DWSVF")
    # plt.grid(True)
    # plt.xlabel("cluster number", fontweight='bold', fontsize="large")
    # plt.ylabel("quality metric", fontweight='bold', fontsize="large")
    # plt.legend()
    # plt.show()

    # статистики
    # for j in range(2, k + 1):
    #     info(j)
    # info(k)

    # метод локтя
    # eb = elbow(k)
    # x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    # plt.plot(x, eb, 'ro-', alpha=0.6)
    # plt.grid(True)
    # plt.title("The Elbow Method")
    # plt.xlabel("cluster number", fontweight='bold', fontsize="large")
    # plt.ylabel("wcss", fontweight='bold', fontsize="large")
    # plt.show()

    # for j in range(1, k + 1):
    #     fcm(j)

    m_MPC = PC(k)
    m_XB = XB(k)
    m_PBMF = PBMF(k)
    DWSVF(k, m_XB, m_PBMF, m_MPC)

if __name__ == '__main__':
    k = 5
    main(k)