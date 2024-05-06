import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from FCM.FCM import fcm
# from dimensionReduction.PCA import metricPCA
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

def chor(k):
    metrics = pd.read_csv("data/metrics_update.csv")
    OldChordDistribution_metric = metrics['OldChordDistribution']

    # dataset = np.zeros((len(OldChordDistribution_metric[0].split()), len(OldChordDistribution_metric)))
    # for i in range(0, len(OldChordDistribution_metric)):
    #     for j in range(0, len(OldChordDistribution_metric[0].split())):
    #         dataset[j][i] = list(map(float, OldChordDistribution_metric[i][1:-1].split()))[j]
    #
    # dataset_for_PCA = pd.DataFrame(dataset)
    # dataset_for_PCA.to_csv("data/dataset.csv", index=False, header=False)
    dataset = pd.read_csv('data/dataset_gauss.csv', header=None, index_col=None).values

    n = len(OldChordDistribution_metric)
    d = len(OldChordDistribution_metric[0].split())

    time_c = []
    for j in range(1, k + 1):
        # время работы алгоритма
        import time
        start = time.perf_counter()
        fcm(j, dataset, n, d)
        finish = time.perf_counter()
        time_c.append(finish - start)
    print('Время работы: ', time_c)


def classic(k):
    metrics = pd.read_csv("data/metrics_for_classic.csv", usecols=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]).transpose()
    dataset_for_PCA = pd.DataFrame(metrics)
    dataset_for_PCA.to_csv("data/dataset.csv", index=False, header=False)
    dataset = pd.read_csv('data/dataset.csv', header=None, index_col=None).values

    n = dataset.shape[1]
    d = dataset.shape[0]

    fcm(k, dataset, n, d)

def main():
    k = 14
    # chor(k)
    #classic(k)
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

    # eb = [0.03128688166130681, 0.021362405299783817, 0.01591948718559371, 0.01263500763328776, 0.011133767186729798, 0.009962126238831165, 0.009000726478339556, 0.008763119530192076, 0.008233967331063458, 0.007650497565717164, 0.0073317083884914475, 0.0061435863196529356, 0.005856543695150195]
    # eb6 = []

    # A = np.vstack([x, np.ones(len(x))]).T
    # m, c = np.linalg.lstsq(A, eb, rcond=None)[0]
    # A6 = np.vstack([x6, np.ones(len(x6))]).T
    # m6, c6 = np.linalg.lstsq(A6, eb6, rcond=None)[0]

    # plt.axvline(x=, color="black", linestyle='dashed')
    # plt.plot(x, eb, color="green", label='wcss', markersize=5, marker="D", alpha=0.5)
    #
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
    # метод локтя
    # eb = elbow(k)
    # eb = [0.031287236511210285, 0.021427187482672746, 0.01591825185995278, 0.01264201671081432, 0.01167551623029187, 0.009986695166406385, 0.009674899617171686, 0.008748680649157708, 0.00823239667912572, 0.00790288183538709, 0.0063884342219914965, 0.006145403690216005, 0.005856121123591132]
    # x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    # plt.plot(x, eb, 'ro-', alpha=0.6)
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
    #
    # fitTime = [ 1.012308, 6.8664952, 14.758886600000002, 14.460521899999996, 37.1063593, 48.408479299999996, 62.53867070000001, 25.318514100000016, 48.59035020000002, 115.2432794, 116.38337340000004, 45.530485000000056, 130.95283940000002]
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
    x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    m_MPC = PC(k)
    # plt.plot(x, m_MPC, 'b+-', alpha=0.3, label="MPC")

    m_XB = XB(k)
    # plt.plot(x, m_XB, 'g^-', alpha=0.3, label="XB")

    m_PBMF = PBMF(k)
    # plt.plot(x, m_PBMF, 'ro-', alpha=0.3, label="PBMF")

    m_DWSVF = DWSVF(k, m_XB, m_PBMF, m_MPC)
    plt.plot(x, m_DWSVF, color = 'olive' , marker='s', alpha=0.3, label="DWSVF")

    plt.grid(True)
    plt.xlabel("cluster number", fontweight='bold', fontsize="large")
    plt.ylabel("quality metric", fontweight='bold', fontsize="large")
    plt.legend()
    plt.show()
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

if __name__ == '__main__':
    main()
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
#-----------------------------------------------------------------------------------------------------------------------
    # датасет для проверки метрик достоверности кластеризации
    # # from ucimlrepo import fetch_ucirepo
    # #
    # # iris = fetch_ucirepo(id=53)
    # #
    # # dataset = iris.data.features.values.transpose()
    # # n = 150
    # # d = 4
#-----------------------------------------------------------------------------------------------------------------------