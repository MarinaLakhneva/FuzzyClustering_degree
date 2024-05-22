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
    metrics = pd.read_csv("data/metrics_update_drop.csv")
    OldChordDistribution_metric = metrics['OldChordDistribution']

    dataset = pd.read_csv("data/dataset/" + str_ + "8_true.csv", header=None, index_col=None).values

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

    str_ = "chords/dataset"
    # str_ = "chords/dataset_gauss"
    # str_ = "chords/dataset_gauss_"
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
    # # chords/dataset: eb = [0.022651509834960643, 0.016466535945632268, 0.013023779775958453, 0.010860909085125435, 0.008766004143607705, 0.007852057564333412, 0.006776142633890462, 0.006246646799755966, 0.005902012753613108, 0.005556364697499616, 0.004884788116267907, 0.004745725138086387, 0.004692150334953178]
    # # classic/dataset_gauss: eb = [0.03266178550945682, 0.022613893549625275, 0.01796460436741905, 0.013710564614697513, 0.010757127634510958, 0.009436998043306092, 0.008460942181398182, 0.007739684723785025, 0.0073344272140222514, 0.0066274219721112965, 0.006416953901280264, 0.0060300342697580086, 0.005605805971386404]
    # # chords/dataset_gauss_C: eb = [0.021679271710371067, 0.015460564649298635, 0.012015848746809813, 0.009455404057316173, 0.008077524255735893, 0.005962370982060997, 0.004949254002686825, 0.004691994545256598, 0.0044794294301213275, 0.004358821674754459, 0.004139724664004769, 0.004016000223873641, 0.0038190530936881625]
    # #
    # # classic/dataset: eb = [5970.216619806015, 3665.3713673567368, 2847.5302783455963, 2403.917509380308, 1682.6848032389885, 1543.4997873725679, 1454.537609674139, 1326.7701191267788, 1188.8650809699275, 1137.5395174095352, 1091.0018125379825, 1055.058760844435, 1027.3145207578214]
    # # classic/dataset_gauss: eb = [4329.554229130427, 3296.4671194542466, 2718.7897996803067, 2236.4087159923947, 1997.3188883027583, 1733.6773380973902, 1592.7775493007107, 1502.0429168124497, 1426.9234103048527, 1366.4825098665815, 1289.2495497855175, 1193.0160198104916, 1144.2913472696562]
    # # classic/dataset_gauss_C: eb = [5442.173440662615, 3174.6612631414455, 2425.21089668878, 1587.5126103226294, 1519.4191443909028, 891.1876037871563, 1398.955619568909, 779.1796513895499, 752.1118329786052, 708.9563781584623, 695.9119216511416, 629.9642871293587, 615.6316372182566]
    #
    # x = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
    # x_m = np.array([7, 8, 9, 10, 11, 12, 13, 14])
    # x_l = np.array([7, 8, 9, 10, 11, 12, 13, 14])
    # x_s = np.array([8, 9, 10, 11, 12, 13, 14])
    #
    # eb = [5442.173440662615, 3174.6612631414455, 2425.21089668878, 1587.5126103226294, 1519.4191443909028, 891.1876037871563, 1398.955619568909, 779.1796513895499, 752.1118329786052, 708.9563781584623, 695.9119216511416, 629.9642871293587, 615.6316372182566]
    # eb_l = [891.1876037871563, 1398.955619568909, 779.1796513895499, 752.1118329786052, 708.9563781584623, 695.9119216511416, 629.9642871293587, 615.6316372182566]
    # eb_s = [1398.955619568909, 779.1796513895499, 752.1118329786052, 708.9563781584623, 695.9119216511416, 629.9642871293587, 615.6316372182566]
    #
    # # A = np.vstack([x, np.ones(len(x))]).T
    # # m, c = np.linalg.lstsq(A, eb, rcond=None)[0]
    # # A_m = np.vstack([x_m, np.ones(len(x_m))]).T
    # # m_m, c_m = np.linalg.lstsq(A_m, eb_m, rcond=None)[0]
    # A_l = np.vstack([x_l, np.ones(len(x_l))]).T
    # m_l, c_l = np.linalg.lstsq(A_l, eb_l, rcond=None)[0]
    # A_s = np.vstack([x_s, np.ones(len(x_s))]).T
    # m_s, c_s = np.linalg.lstsq(A_s, eb_s, rcond=None)[0]
    #
    # plt.axvline(x=7, color="black", linestyle='dashed')
    # plt.plot(x, eb, color="red", label='wcss', markersize=5, marker="D", alpha=0.5)
    #
    # # plt.plot(x, m * x + c, 'b', label='MLS', linestyle='dashed')
    # # plt.plot(x_m, m_m * x_m + c_m, 'm', label='MLS 7-14', linestyle='dashed') # m
    # plt.plot(x_l, m_l * x_l + c_l, 'b', label='MLS 7-14', linestyle='dashed') # l
    # plt.plot(x_s, m_s * x_s + c_s, 'green', label='MLS 8-14', linestyle='dashed') # l
    #
    #
    # plt.grid(True)
    # plt.title("The Elbow Method", fontsize=16, fontweight='bold')
    # plt.xlabel("cluster number", fontsize=16, fontweight='bold')
    # plt.ylabel("wcss", fontsize=16, fontweight='bold')
    # plt.legend()
    # plt.savefig("pic/" + str_ + "C/eb_MLS.png")
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
    #
    #
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
    # # chords/dataset: fitTime = [0.9275415999999999, 4.085654999999999, 9.5716784, 7.786300100000002, 9.8690225, 21.497312700000002, 43.952473, 34.128100399999994, 35.069336899999996, 39.25615930000001, 56.6659865, 44.479362500000036, 42.54996790000001]
    # # chords/dataset_gauss: fitTime = [ 0.9315798999999998, 3.2816072, 6.4858287, 23.6265762, 18.6443922, 13.098301599999992, 13.692754999999991, 37.712126299999994, 45.6459323, 29.325714699999992, 27.741583100000014, 139.91008129999997, 223.58177140000004]
    # # chords/dataset_gauss_C: fitTime = [ 0.9317805000000001, 4.0876927, 4.692801, 16.2255527, 8.075427900000001, 14.0234375, 19.734027600000005, 30.6524335, 25.650479199999992, 36.8108371, 44.52995150000001, 121.95614429999998, 70.9707598]
    # #
    # # classic/dataset: fitTime = [ 0.4235547999999998, 0.8161394999999998, 1.2861998999999997, 1.4747832999999995, 4.311793499999999, 4.7529886999999995, 3.999365600000001, 8.880025499999999, 7.262690900000003, 17.1199916, 53.564895500000006, 9.303790300000003, 22.80326799999999]
    # # classic/dataset_gauss: fitTime = [ 0.15762169999999998, 0.5417057000000001, 1.2479858, 7.496629500000001, 7.0332995, 4.140908199999998, 12.996233999999998, 5.8489211999999995, 10.870105600000002, 7.7351648, 8.2063196, 32.22100739999999, 15.557815700000006]
    # # classic/dataset_gauss_C: fitTime = [0.40859829999999997, 0.3869697000000003, 0.7966461999999996, 1.3676933, 6.632002699999999, 2.5547958999999985, 2.2472403000000014, 3.3867388, 10.7179322, 13.166586699999996, 7.687622400000002, 7.813149199999998, 10.510618499999993]
    # fitTime = [0.40859829999999997, 0.3869697000000003, 0.7966461999999996, 1.3676933, 6.632002699999999,
    #            2.5547958999999985, 2.2472403000000014, 3.3867388, 10.7179322, 13.166586699999996, 7.687622400000002,
    #            7.813149199999998, 10.510618499999993]
    #
    # model = np.poly1d(np.polyfit(x, fitTime, 2))
    # ax2 = ax1.twinx()
    # color = 'tab:green'
    # ax2.set_ylabel('fit time, sec', color="black", fontsize=16, fontweight='bold')
    # polyline = np.linspace(1, 14, 50)
    # ax2.plot(x, fitTime, color=color, linestyle='dashed', marker="o")
    # plt.plot(polyline, model(polyline))
    # ax2.tick_params(axis='y', labelcolor=color)
    # plt.title("The Elbow Method", fontsize=16, fontweight='bold')
    # plt.grid(True)
    # plt.savefig("pic/" + str_ + "C/eb.png")
    # plt.show()
#-----------------------------------------------------------------------------------------------------------------------
    # x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    #
    # m_MPC = PC(k, str_)
    # # plt.plot(x, m_MPC, 'b+-', alpha=0.3, label="MPC")
    #
    # m_XB = XB(k, str_)
    # # plt.plot(x, m_XB, 'g^-', alpha=0.3, label="XB")
    # # #
    # m_PBMF = PBMF(k, str_)
    # # plt.plot(x, m_PBMF, 'ro-', alpha=0.3, label="PBMF")
    # # #
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