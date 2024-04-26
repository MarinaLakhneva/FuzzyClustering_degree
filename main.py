import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from FCM.FCM import fcm
from dimensionReduction.PCA import metricPCA
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

def main(k, dataset, n, d):
#-----------------------------------------------------------------------------------------------------------------------
    # pie
    # ['Stubby', 'Mushroom', 'Thin', 'Filopodia', 'Outlier']
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

    # eb = []
    # eb6 = []

    # A = np.vstack([x, np.ones(len(x))]).T
    # m, c = np.linalg.lstsq(A, eb, rcond=None)[0]
    # A6 = np.vstack([x6, np.ones(len(x6))]).T
    # m6, c6 = np.linalg.lstsq(A6, eb6, rcond=None)[0]

    # plt.axvline(x=7, color="black", linestyle='dashed')
    # plt.plot(x, eb, color="green", label='wcss', markersize=5, marker="D", alpha=0.5)

    # plt.plot(x, m * x + c, 'b', label='MLS', linestyle='dashed')
    # plt.plot(x6, m6 * x6 + c6, 'm', label='MLS 5-14', linestyle='dashed')

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
    #     start = datetime.datetime.now()
    #     fcm(j)
    #     finish = datetime.datetime.now()
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

    # fitTime = []
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

#-----------------------------------------------------------------------------------------------------------------------
    # шипики, которые портили статистику на классике
    # 304 | 0.025 0.025 0.1 dataset\5-2\spine_10.off шипик принадлежал 5
    # 122 | 0.025 0.025 0.1 dataset\3_full_res (1)\spine_6.off шипик принадлежал 6
    # обновленный файл без них: metrics_for_classic.csv
#-----------------------------------------------------------------------------------------------------------------------
#     for j in range(1, k + 1):
#         fcm(j, dataset, n, d)
#     fcm(k, dataset, n, d)

if __name__ == '__main__':
    # # удалила шипики которых нет в 0.025 0.025 0.1 dataset
    # import glob
    #
    # metrics_d = pd.read_csv("data/metrics.csv")
    # print(len(metrics_d))
    # to_delete = []
    # for indexClusterization, p in enumerate(metrics_d['Spine File'].to_numpy()):
    #     if p.replace("/", "\\") not in glob.glob('0.025 0.025 0.1 dataset/*/*.off', recursive=True):
    #         to_delete.append(indexClusterization)
    #
    # for n_drop in range(0, len(to_delete)):
    #     metrics_d = metrics_d.drop(to_delete[n_drop])
    # metrics_d.to_csv("data/metrics_update.csv", indexClusterization=False)

    # хорды
    metrics = pd.read_csv("data/metrics_update.csv")
    OldChordDistribution_metric = metrics['OldChordDistribution']

    # dataset = np.zeros((len(OldChordDistribution_metric[0].split()), len(OldChordDistribution_metric)))
    # for i in range(0, len(OldChordDistribution_metric)):
    #     for j in range(0, len(OldChordDistribution_metric[0].split())):
    #         dataset[j][i] = list(map(float, OldChordDistribution_metric[i][1:-1].split()))[j]
    #
    # dataset_for_PCA = pd.DataFrame(dataset)
    # dataset_for_PCA.to_csv("data/dataset.csv", index=False, header=False)
    #
    # dataset = pd.read_csv('data/dataset.csv', header=None, index_col=None).values

    n = len(OldChordDistribution_metric)
    d = len(OldChordDistribution_metric[0].split())

    # классика
    # metrics = pd.read_csv("data/metrics_for_classic.csv", usecols=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]).transpose()
    # dataset_for_PCA = pd.DataFrame(metrics)
    # dataset_for_PCA.to_csv("data/dataset.csv", index=False, header=False)
    # dataset = pd.read_csv('data/dataset.csv', header=None, index_col=None).values

    # n = dataset.shape[1]
    # print(n)
    # d = dataset.shape[0]
    # print(d)

    # датасет для проверки метрик достоверности кластеризации
    # # from ucimlrepo import fetch_ucirepo
    # #
    # # iris = fetch_ucirepo(id=53)
    # #
    # # dataset = iris.data.features.values.transpose()
    # # n = 150
    # # d = 4

    dataset = pd.read_csv('data/dataset.csv', header=None, index_col=None).values
    k = 14
    main(k, dataset, n, d)


