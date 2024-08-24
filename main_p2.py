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
    metrics = pd.read_csv("data/metrics_true.csv")
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
    for j in range(6, k + 1):
        # время работы алгоритма
        import time
        start = time.perf_counter()
        fcm(j, dataset, n, d, str_)
        finish = time.perf_counter()
        time_c.append(finish - start)
    print('Время работы: ', time_c)

def main():
    k = 6

    # str_ = "chords/dataset"
    # str_ = "chords/dataset_gauss"
    # str_ = "chords/dataset_gauss_"
    # chords(k, str_)

    str_ = "classic/dataset"
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
    # chords/dataset: eb = [0.02266734770615795, 0.016403557358961363, 0.012985183556979587, 0.010784168942633796, 0.009253053614906583, 0.007486965641433933, 0.006724086239492887, 0.006202611668789534, 0.0056421736024886045, 0.005378068884622969, 0.004870865619948707, 0.004740180616817705, 0.004582415527847291]
    # chords/dataset_gauss: eb = [0.031645023189926715, 0.02156350910941023, 0.01725539441852113, 0.014255601642374143, 0.012387656901419818, 0.010591167811927904, 0.009873110405876852, 0.00850008587213826, 0.00810597748283986, 0.007844085418143062, 0.006665118430459525, 0.006404448324916068, 0.006231831041028563]
    # chords/dataset_gauss_C: eb = [0.023437493935279004, 0.01661738232176893, 0.01282274137236017, 0.010287411129983968, 0.008569696973809021, 0.00708550982275808, 0.0065902909896259874, 0.0060958017608721965, 0.005491845386773213, 0.005578493061638481, 0.004977192039577485, 0.004576181478668616, 0.004478976883841871]
    #
    # classic/dataset: eb = [5185.511437105444, 3007.2929029218503, 2282.72724221728, 1928.8951397672777, 1213.6515089634072, 1100.174554705399, 1018.5766061948871, 890.4267461183011, 845.5958595486169, 808.5256010018331, 763.8849489963535, 733.0546061935781, 708.1107901325968]
    # classic/dataset_gauss: eb = [3994.4467391521366, 2806.161869588306, 2335.9963300658083, 1936.6706100595727, 1708.3176366725702, 1587.5312355832284, 1412.8812608136955, 1232.979855191866, 1142.623208950198, 1069.242283098129, 1033.5990110571308, 984.9521765468185, 901.992250374501]
    # classic/dataset_gauss_C: eb = [5481.402594212324, 3195.683617459166, 2376.196299916927, 1907.4207573234496, 1013.701869472729, 1744.0185852361988, 851.976951257153, 802.4947313242922, 752.1895787993686, 734.2569355563002, 656.2533199841192, 635.4638873670451, 605.75382382853]
    # #
    x = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
    x_l = np.array([5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
    x_s = np.array([6, 7, 8, 9, 10, 11, 12, 13, 14])

    eb = [5185.511437105444, 3007.2929029218503, 2282.72724221728, 1928.8951397672777, 1213.6515089634072, 1100.174554705399, 1018.5766061948871, 890.4267461183011, 845.5958595486169, 808.5256010018331, 763.8849489963535, 733.0546061935781, 708.1107901325968]
    eb_l = [1928.8951397672777, 1213.6515089634072, 1100.174554705399, 1018.5766061948871, 890.4267461183011, 845.5958595486169, 808.5256010018331, 763.8849489963535, 733.0546061935781, 708.1107901325968]
    eb_s = [1213.6515089634072, 1100.174554705399, 1018.5766061948871, 890.4267461183011, 845.5958595486169, 808.5256010018331, 763.8849489963535, 733.0546061935781, 708.1107901325968]

    A_l = np.vstack([x_l, np.ones(len(x_l))]).T
    m_l, c_l = np.linalg.lstsq(A_l, eb_l, rcond=None)[0]
    A_s = np.vstack([x_s, np.ones(len(x_s))]).T
    m_s, c_s = np.linalg.lstsq(A_s, eb_s, rcond=None)[0]

    # plt.axvline(x=6, color="black", linestyle='dashed')
    plt.plot(x, eb, color="red", label='wcss', markersize=5, marker="D", alpha=0.5)


    # plt.plot(x_l, m_l * x_l + c_l, 'b', label='MLS 5-14', linestyle='dashed') # l
    # plt.plot(x_s, m_s * x_s + c_s, 'green', label='MLS 6-14', linestyle='dashed') # l


    plt.grid(True)
    plt.title("Метод локтя", fontsize=16, fontweight='bold')
    plt.xlabel("номер кластера", fontsize=16, fontweight='bold')
    plt.ylabel("wcss", fontsize=16, fontweight='bold')
    plt.legend()
    plt.savefig("pic/" + str_ + "/eb_.png")
    plt.show()

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
    # # chords/dataset: fitTime = [1.0858328, 2.6455773000000002, 10.5472658, 18.837593199999997, 42.5415243, 35.360885999999994, 29.52733339999999, 49.98752479999999, 53.8458852, 24.981976600000024, 45.197780600000044, 56.61176879999999, 67.44432109999997]
    # # chords/dataset_ev: fitTime = [1.5153604999999999, 3.8058905, 14.206687700000002, 18.9816806, 27.59161139999999, 45.91496769999999, 124.30058000000001, 46.19594500000002, 78.7204696, 86.35662580000002, 86.94522990000002, 78.98337670000001, 100.25990520000005]
    # # chords/dataset_gauss: fitTime = [1.2207328, 4.1258889000000005, 10.101417600000001, 14.4712474, 18.3791764, 31.495880199999995, 17.804773300000008, 13.188537100000005, 17.671792499999995, 41.14154210000001, 34.12847529999999, 67.18715339999997, 127.6670709]
    # # chords/dataset_gauss_C: fitTime = [1.0716291999999998, 5.2881507999999995, 6.541198600000001, 10.956027299999999, 11.004923399999996, 8.084346600000003, 9.862694300000001, 16.216204399999995, 42.33613870000001, 29.329837800000007, 46.71325949999999, 31.776965899999993, 51.467472999999984]
    # #
    # # classic/dataset: fitTime = [0.3823555999999999, 0.5596836999999999, 0.6431515999999995, 1.3233586000000006, 2.1199874000000003, 2.8003155, 4.0078043, 3.9971244000000006, 4.407764, 5.4565749, 14.017656200000001, 8.187089700000001, 11.412519199999998]
    # # classic/dataset_gauss: fitTime = [0.2828047, 0.5609098000000001, 1.0373195000000002, 1.5345022000000004, 1.8485805000000006, 5.1852322, 11.6236258, 4.321233399999997, 7.521791700000005, 9.8831129, 12.5230095, 18.446077599999995, 8.010078500000006]
    # # classic/dataset_gauss_C: fitTime = [0.3850844, 0.6120890999999999, 1.6300562000000003, 0.9804114999999998, 1.2471228000000005, 1.7244789999999988, 5.318852400000001, 2.6380979999999994, 3.877330100000002, 9.887307700000001, 14.336542699999999, 12.791398799999996, 14.517288800000003]
    #
    # fitTime = [0.3850844, 0.6120890999999999, 1.6300562000000003, 0.9804114999999998, 1.2471228000000005, 1.7244789999999988, 5.318852400000001, 2.6380979999999994, 3.877330100000002, 9.887307700000001, 14.336542699999999, 12.791398799999996, 14.517288800000003]
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
    # обновленный файл без них: metrics_true.csv
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