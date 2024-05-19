import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from FCM.FCM import fcm
from dimensionReduction.PCA import metricPCA
from indexClusterization.elbow import elbow

from indexClusterization.metric_PC import PC
from indexClusterization.metric_XB import XB
from indexClusterization.metric_PBMF import PBMF
from indexClusterization.F_DWSVF import DWSVF

from indexClusterization.interClusterDist import interClusterDistance
from indexClusterization.interClusterDist_ss import interClusterDistance_sumsSquares
from indexClusterization.intraClusterDist_ss import intraClusterDistances_sumsSquares

# k - количество кластеров 1<j<k
# d - размерность вектора данных 1<l<d
# n - мощность выборки

def chords(k, str_):
    metrics = pd.read_csv("data/metrics_update.csv")
    OldChordDistribution_metric = metrics['OldChordDistribution']

    dataset = pd.read_csv("data/dataset/" + str_ + ".csv", header=None, index_col=None).values

    n = len(OldChordDistribution_metric)
    d = len(OldChordDistribution_metric[0].split())

    time_c = []
    for j in range(1, k + 1):
        # время работы алгоритма
        import time
        start = time.perf_counter()
        fcm(j, dataset, n, d, str_)
        finish = time.perf_counter()
        time_c.append(finish - start)
    print('Время работы: ', time_c)


def classic(k, str_):
    dataset = pd.read_csv("data/dataset/" + str_ + ".csv", header=None, index_col=None).values

    n = dataset.shape[1]
    d = dataset.shape[0]

    time_c = []
    for j in range(1, k + 1):
        # время работы алгоритма
        import time
        start = time.perf_counter()
        fcm(j, dataset, n, d, str_)
        finish = time.perf_counter()
        time_c.append(finish - start)
    print('Время работы: ', time_c)

def main():
    k = 14

    # str_ = "chords/dataset"
    str_ = "chords/dataset_gauss"
    # str_ = "chords/dataset_gauss_C"
    # chords(k, str_)

    # str_ = "classic/dataset"
    # str_ = "classic/dataset_gauss"
    # str_ = "classic/dataset_gauss_"
    # classic(k, str_)
#-----------------------------------------------------------------------------------------------------------------------
    # pie
    # groups = ['Stubby', 'Mushroom', 'Thin', 'Filopodia', 'Outlier']
    # data = [0, 4, 4, 0, 0]
    #
    # # Creating plot
    # fig = plt.figure(figsize=(10, 10))
    # plt.pie(data, labels=groups)
    # plt.show()
#-----------------------------------------------------------------------------------------------------------------------
    # MLS
    # # chords/dataset: eb = [0.025933184900380997, 0.01917722372860509, 0.015297671177932955, 0.012275585175465491, 0.010301049111834276, 0.009062819181046155, 0.007746787898485164, 0.006832926053162332, 0.0060515841713747465, 0.0056085228859189575, 0.005151338480900906, 0.005000635222686606, 0.0049319920184902515]
    # # chords/dataset_gauss: eb = [0.04210020417430692, 0.029315582867348054, 0.02437917293425056, 0.01918816510624472, 0.017360201892725965, 0.01564382144125048, 0.012861067212417445, 0.011494249459819599, 0.010617828558005886, 0.010234457232520575, 0.00982739690969041, 0.009320894260629532, 0.009004027227349066]
    # # chords/dataset_gauss_C: eb =
    # #
    # # classic/dataset: eb = [5970.216619806015, 3665.3713673567368, 2847.5302783455963, 2403.917509380308, 1682.6848032389885, 1543.4997873725679, 1454.537609674139, 1326.7701191267788, 1188.8650809699275, 1137.5395174095352, 1091.0018125379825, 1055.058760844435, 1027.3145207578214]
    # # classic/dataset_gauss: eb = [4329.554229130427, 3296.4671194542466, 2718.7897996803067, 2236.4087159923947, 1997.3188883027583, 1733.6773380973902, 1592.7775493007107, 1502.0429168124497, 1426.9234103048527, 1366.4825098665815, 1289.2495497855175, 1193.0160198104916, 1144.2913472696562]
    # # classic/dataset_gauss_C: eb = [5442.173440662615, 3174.6612631414455, 2425.21089668878, 1587.5126103226294, 1519.4191443909028, 891.1876037871563, 1398.955619568909, 779.1796513895499, 752.1118329786052, 708.9563781584623, 695.9119216511416, 629.9642871293587, 615.6316372182566]
    #
    # x = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
    # x_m = np.array([7, 8, 9, 10, 11, 12, 13, 14])
    # x_l = np.array([8, 9, 10, 11, 12, 13, 14])
    # # x_s = np.array([7, 8, 9, 10, 11, 12, 13, 14])
    #
    # eb = [0.04210020417430692, 0.029315582867348054, 0.02437917293425056, 0.01918816510624472, 0.017360201892725965, 0.01564382144125048, 0.012861067212417445, 0.011494249459819599, 0.010617828558005886, 0.010234457232520575, 0.00982739690969041, 0.009320894260629532, 0.009004027227349066]
    # eb_m = [0.01564382144125048, 0.012861067212417445, 0.011494249459819599, 0.010617828558005886, 0.010234457232520575, 0.00982739690969041, 0.009320894260629532, 0.009004027227349066]
    # eb_l = [0.012861067212417445, 0.011494249459819599, 0.010617828558005886, 0.010234457232520575, 0.00982739690969041, 0.009320894260629532, 0.009004027227349066]
    # # eb_s = [0.009062819181046155, 0.007746787898485164, 0.006832926053162332, 0.0060515841713747465, 0.0056085228859189575, 0.005151338480900906, 0.005000635222686606, 0.0049319920184902515]
    #
    # A = np.vstack([x, np.ones(len(x))]).T
    # m, c = np.linalg.lstsq(A, eb, rcond=None)[0]
    # A_m = np.vstack([x_m, np.ones(len(x_m))]).T
    # m_m, c_m = np.linalg.lstsq(A_m, eb_m, rcond=None)[0]
    # A_l = np.vstack([x_l, np.ones(len(x_l))]).T
    # m_l, c_l = np.linalg.lstsq(A_l, eb_l, rcond=None)[0]
    # # A_s = np.vstack([x_s, np.ones(len(x_s))]).T
    # # m_s, c_s = np.linalg.lstsq(A_s, eb_s, rcond=None)[0]
    #
    # plt.axvline(x=8, color="black", linestyle='dashed')
    # plt.plot(x, eb, color="red", label='wcss', markersize=5, marker="D", alpha=0.5)
    #
    # plt.plot(x, m * x + c, 'b', label='MLS', linestyle='dashed')
    # plt.plot(x_m, m_m * x_m + c_m, 'm', label='MLS 7-14', linestyle='dashed') # m
    # plt.plot(x_l, m_l * x_l + c_l, 'green', label='MLS 8-14', linestyle='dashed') # l
    # # plt.plot(x_s, m_s * x_s + c_s, 'yellow', label='MLS 7-14', linestyle='dashed') # l
    #
    #
    # plt.grid(True)
    # plt.title("The Elbow Method", fontsize=16, fontweight='bold')
    # plt.xlabel("cluster number", fontsize=16, fontweight='bold')
    # plt.ylabel("wcss", fontsize=16, fontweight='bold')
    # plt.legend()
    # plt.savefig("pic/" + str_ + "/eb_MLS.png")
    # plt.show()

    # from sklearn.metrics import mean_squared_error
    # print(mean_squared_error(m * x + c, y))
#-----------------------------------------------------------------------------------------------------------------------
    # метод локтя
    # eb = elbow(k, str_)
    # x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    # plt.plot(x, eb, 'ro-', alpha=0.6)
    # plt.grid(True)
    # plt.title("The Elbow Method")
    # plt.xlabel("cluster number", fontweight='bold', fontsize=16)
    # plt.ylabel("wcss", fontweight='bold', fontsize=16)
    # plt.show()


    # график метода локтя и времени обучения
    # eb = elbow(k, str_)
    # x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    # fig, ax1 = plt.subplots()
    # color = 'tab:red'
    # ax1.set_xlabel('number of cluster', fontsize=16, fontweight='bold')
    # ax1.set_ylabel('wcss', color="black", fontsize=16, fontweight='bold')
    # ax1.plot(x, eb, color=color, marker="D")
    # ax1.tick_params(axis='y', labelcolor=color)
    # plt.grid(True)
    #
    # # chords/dataset: fitTime = [ 1.0101250000000004, 5.046671600000001, 8.059192499999998, 6.275258700000002, 13.0933307, 22.811054500000004, 45.3959546, 47.333502899999985, 44.278549999999996, 61.20824089999999, 34.24126510000002, 45.516999999999996, 35.66385500000001]
    # # chords/dataset_gauss: fitTime = [ 1.1268296000000002, 4.5353292, 13.7917536, 7.153625699999999, 15.018148200000002, 31.74118080000001, 105.5867542, 33.16209939999999, 23.75558939999999, 66.76220840000002, 46.98436450000003, 214.25135410000001, 29.678181999999993]
    # # chords/dataset_gauss_C: fitTime =
    #
    # # classic/dataset: fitTime = [ 0.4235547999999998, 0.8161394999999998, 1.2861998999999997, 1.4747832999999995, 4.311793499999999, 4.7529886999999995, 3.999365600000001, 8.880025499999999, 7.262690900000003, 17.1199916, 53.564895500000006, 9.303790300000003, 22.80326799999999]
    # # classic/dataset_gauss: fitTime = [ 0.15762169999999998, 0.5417057000000001, 1.2479858, 7.496629500000001, 7.0332995, 4.140908199999998, 12.996233999999998, 5.8489211999999995, 10.870105600000002, 7.7351648, 8.2063196, 32.22100739999999, 15.557815700000006]
    # # classic/dataset_gauss_C: fitTime = [0.40859829999999997, 0.3869697000000003, 0.7966461999999996, 1.3676933, 6.632002699999999, 2.5547958999999985, 2.2472403000000014, 3.3867388, 10.7179322, 13.166586699999996, 7.687622400000002, 7.813149199999998, 10.510618499999993]
    # fitTime = [1.1268296000000002, 4.5353292, 13.7917536, 7.153625699999999, 15.018148200000002, 31.74118080000001, 105.5867542, 33.16209939999999, 23.75558939999999, 66.76220840000002, 46.98436450000003, 214.25135410000001, 29.678181999999993]
    # model = np.poly1d(np.polyfit(x, fitTime, 2))
    # ax2 = ax1.twinx()
    # color = 'tab:green'
    # ax2.set_ylabel('fit time, sec', color="black", fontsize=16, fontweight='bold')
    # polyline = np.linspace(1, 14, 50)
    # ax2.plot(x, fitTime, color=color, linestyle='dashed', marker="o")
    # plt.plot(polyline, model(polyline))
    # ax2.tick_params(axis='y', labelcolor=color)
    # # plt.axvline(x=6, color="black", linestyle='dashed')
    # plt.title("The Elbow Method", fontsize=16, fontweight='bold')
    # plt.grid(True)
    # plt.savefig("pic/" + str_ + "/eb.png")
    # plt.show()
#-----------------------------------------------------------------------------------------------------------------------
    # x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    # m_MPC = PC(k, str_)
    # plt.plot(x, m_MPC, 'b+-', alpha=0.3, label="MPC")
    #
    # m_XB = XB(k, str_)
    # plt.plot(x, m_XB, 'g^-', alpha=0.3, label="XB")
    # #
    # m_PBMF = PBMF(k, str_)
    # plt.plot(x, m_PBMF, 'ro-', alpha=0.3, label="PBMF")
    # #
    # m_DWSVF = DWSVF(k, m_XB, m_PBMF, m_MPC)
    # plt.plot(x, m_DWSVF, color = 'olive' , marker='s', alpha=0.3, label="DWSVF")
    # #
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
    # шипики, которые портили статистику на классике в PCA
    # 304 | 0.025 0.025 0.1 dataset_gauss_C\5-2\spine_10.off шипик принадлежал 5
    # 122 | 0.025 0.025 0.1 dataset_gauss_C\3_full_res (1)\spine_6.off шипик принадлежал 6
    # обновленный файл без них: metrics_for_classic.csv
#-----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
#-----------------------------------------------------------------------------------------------------------------------
    # # удалила шипики которых нет в 0.025 0.025 0.1 dataset_gauss_C
    # import glob
    #
    # metrics_d = pd.read_csv("data/metrics.csv")
    # print(len(metrics_d))
    # to_delete = []
    # for indexClusterization, p in enumerate(metrics_d['Spine File'].to_numpy()):
    #     if p.replace("/", "\\") not in glob.glob('0.025 0.025 0.1 dataset_gauss_C/*/*.off', recursive=True):
    #         to_delete.append(indexClusterization)
    #
    # for n_drop in range(0, len(to_delete)):
    #     metrics_d = metrics_d.drop(to_delete[n_drop])
    # metrics_d.to_csv("data/metrics_update.csv", indexClusterization=False)
#-----------------------------------------------------------------------------------------------------------------------
    # # удалить шипик

    # metrics_d = pd.read_csv("data/metrics_update_drop.csv")
    # print(len(metrics_d))

    # metrics_d = metrics_d.drop(304)
    # metrics_d.to_csv("data/metrics_update_drop.csv", index=False)