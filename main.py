import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from FCM.FCM import fcm
from dimensionReduction.PCA import p
from analysis import general
from charts import charts
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
    # general(k)
    # charts(k)
#-----------------------------------------------------------------------------------------------------------------------
    # groups = ['Stubby', 'Mushroom', 'Thin', 'Filopodia', 'Outlier']
    # groups = ['Filopodia', 'Thin']
    # data = [1, 7]
    #
    # # Creating plot
    # fig = plt.figure(figsize=(10, 10))
    # plt.pie(data, labels=groups)
    # plt.savefig('/Users/Marina/degree_ML/pie_chord_11/' + str(3) + '.png')
    # plt.show()
#-----------------------------------------------------------------------------------------------------------------------
    # MLS
    # x = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
    # x6 = np.array([5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
    # x7 = np.array([6, 7, 8, 9, 10, 11, 12, 13, 14])
    # x8 = np.array([7, 8, 9, 10, 11, 12, 13, 14])
    # x9 = np.array([8, 9, 10, 11, 12, 13, 14])
    # x10 = np.array([9, 10, 11, 12, 13, 14])
    # x11= np.array([10, 11, 12, 13, 14])
    #
    # # chord
    # # eb = [4282.021384349321, 3592.405990489654, 3221.8847263472762, 2907.229991464451, 2679.7623652262723, 2557.6134559130246, 2457.30493860853, 2455.918789743303, 2377.9686958697803, 2277.3905726868243, 2196.163986070705, 2142.7520524755955, 2108.7520645006703]
    # eb = [10689.534710343383, 5964.837474035636, 3666.1939016407855, 2888.6652232325664, 2231.585429729597, 1536.7552805086768, 1216.3228863746704, 1100.6351354251672, 978.5885903378548, 1274.3526712948992, 836.7357667966131, 809.2843418925468, 765.6028499812267]
    # eb6 = [2888.6652232325664, 2231.585429729597, 1536.7552805086768, 1216.3228863746704, 1100.6351354251672, 978.5885903378548, 1274.3526712948992, 836.7357667966131, 809.2843418925468, 765.6028499812267]
    # eb7 = [ 2231.585429729597, 1536.7552805086768, 1216.3228863746704, 1100.6351354251672, 978.5885903378548, 1274.3526712948992, 836.7357667966131, 809.2843418925468, 765.6028499812267]
    # eb8 = [ 1536.7552805086768, 1216.3228863746704, 1100.6351354251672, 978.5885903378548, 1274.3526712948992, 836.7357667966131, 809.2843418925468, 765.6028499812267]
    # eb9 = [ 1216.3228863746704, 1100.6351354251672, 978.5885903378548, 1274.3526712948992, 836.7357667966131, 809.2843418925468, 765.6028499812267]
    # eb10 = [ 1100.6351354251672, 978.5885903378548, 1274.3526712948992, 836.7357667966131, 809.2843418925468, 765.6028499812267]
    # eb11 = [ 978.5885903378548, 1274.3526712948992, 836.7357667966131, 809.2843418925468, 765.6028499812267]
    #
    #
    # A = np.vstack([x, np.ones(len(x))]).T
    # m, c = np.linalg.lstsq(A, eb, rcond=None)[0]
    # A6 = np.vstack([x6, np.ones(len(x6))]).T
    # m6, c6 = np.linalg.lstsq(A6, eb6, rcond=None)[0]
    # A7 = np.vstack([x7, np.ones(len(x7))]).T
    # m7, c7 = np.linalg.lstsq(A7, eb7, rcond=None)[0]
    # A8 = np.vstack([x8, np.ones(len(x8))]).T
    # m8, c8 = np.linalg.lstsq(A8, eb8, rcond=None)[0]
    # A9 = np.vstack([x9, np.ones(len(x9))]).T
    # m9, c9 = np.linalg.lstsq(A9, eb9, rcond=None)[0]
    # A10 = np.vstack([x10, np.ones(len(x10))]).T
    # m10, c10 = np.linalg.lstsq(A10, eb10, rcond=None)[0]
    # A11 = np.vstack([x11, np.ones(len(x11))]).T
    # m11, c11 = np.linalg.lstsq(A11, eb11, rcond=None)[0]
    #
    # plt.axvline(x=7, color="black", linestyle='dashed')
    # plt.plot(x, eb, color="green", label='wcss', markersize=5, marker="D", alpha=0.5)
    # plt.plot(x, m * x + c, 'b', label='MLS', linestyle='dashed')
    # plt.plot(x6, m6 * x6 + c6, 'm', label='MLS 5-14', linestyle='dashed')
    # plt.plot(x7, m7 * x7 + c7, 'r', label='MLS 6-14', linestyle='dashed')
    # # plt.plot(x8, m8 * x8 + c8, 'y', linestyle='dashed')
    # # plt.plot(x9, m9 * x9 + c9, 'g', linestyle='dashed')
    # # plt.plot(x10, m10 * x10 + c10, 'pink', linestyle='dashed')
    # # plt.plot(x11, m11 * x11 + c11, 'm',  linestyle='dashed')
    #
    #
    # plt.grid(True)
    # plt.xlabel("cluster number", fontweight='bold', fontsize="large")
    # plt.ylabel("wcss", fontweight='bold', fontsize="large")
    # plt.legend()
    # plt.show()

    # from sklearn.metrics import mean_squared_error
    # print(mean_squared_error(m * x + c, y))
#-----------------------------------------------------------------------------------------------------------------------
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
    # plt.plot(x, fitTime, 'b--', alpha=0.6)
    # plt.grid(True)
    # plt.title("The Elbow Method")
    # plt.xlabel("cluster number", fontweight='bold', fontsize="large")
    # plt.ylabel("wcss", fontweight='bold', fontsize="large")
    # plt.show()

    # график метода локтя и времени обучения
    # fig, ax1 = plt.subplots()
    # color = 'tab:green'
    # ax1.set_xlabel('number of cluster')
    # ax1.set_ylabel('wcss', color=color)
    # ax1.plot(x, eb, color=color, marker="D")
    # ax1.tick_params(axis='y', labelcolor=color)
    # plt.grid(True)


    # на хордах
    # fitTime = [2, 5, 14, 36, 27, 139, 29, 75, 54, 102, 161, 164, 84]
    # на 11
    # fitTime = [0.052, 0.059, 1.017, 1.095, 3.017, 3.091, 4.081, 4.070, 4.098, 5.037, 20.022, 7.044, 12.004]
    # model = np.poly1d(np.polyfit(x, fitTime, 2))
    # ax2 = ax1.twinx()
    # color = 'tab:red'
    # ax2.set_ylabel('fit time, millisec', color=color)
    # polyline = np.linspace(1, 14, 50)
    # ax2.plot(x, fitTime, color=color, linestyle='dashed', marker="o")
    # plt.plot(polyline, model(polyline))
    # ax2.tick_params(axis='y', labelcolor=color)
    # plt.axvline(x=6, color="black", linestyle='dashed')
    # plt.grid(True)
    # plt.show()
#-----------------------------------------------------------------------------------------------------------------------
    # x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

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
    # x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    # plt.plot(x, Q3, 'mo-', alpha=0.6)
    # plt.grid(True)
    # plt.xlabel("cluster number", fontweight='bold', fontsize="large")
    # plt.ylabel("sums of squares of intra-cluster distances", fontweight='bold', fontsize="large")
    # plt.show()

    # Q4 = interClusterDistance_sumsSquares(k, path_FCM)
    # x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    # plt.plot(x, Q4, 'ro-', alpha=0.6)
    # plt.grid(True)
    # plt.xlabel("cluster number", fontweight='bold', fontsize="large")
    # plt.ylabel("sums of squares of inter-cluster distances", fontweight='bold', fontsize="large")
    # plt.show()

    # Q = []
    # for j in range(0, k-1):
    #     param = Q4[j]/Q3[j]
    #     Q.append(param)
    # x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    # plt.plot(x, Q, 'b^-', alpha=0.6)
    # plt.grid(True)
    # plt.xlabel("cluster number", fontweight='bold', fontsize="large")
    # plt.show()

    # шипики, которые портили статистику
    # 304 | 0.025 0.025 0.1 dataset\5-2\spine_10.off шипик принадлежал 5
    # 122 | 0.025 0.025 0.1 dataset\3_full_res (1)\spine_6.off шипик принадлежал 6


if __name__ == '__main__':
    k = 6
    main(k)


