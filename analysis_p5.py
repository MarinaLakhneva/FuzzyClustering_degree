import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# k - количество кластеров 1<j<k
# d - размерность вектора данных 1<l<d
# n - мощность выборки

def ambiguitySpikes(k, n, result, dataset_11, spike):
    difference = 0.1
    ambiguity = np.ones(n)
    for i in range(0, n):
        max_membership = 0
        for j in range(0, k):
            if(max_membership < result[j][i]):
                max_membership = result[j][i]
        for j in range(0, k):
            if(max_membership != result[j][i]):
                if((max_membership - result[j][i]) < difference):
                    ambiguity[i] += 1

    count_ambiguity = np.ones(k)
    for i in range(0, n):
        if(ambiguity[i] == 1):
            count_ambiguity[0] += 1
        elif (ambiguity[i] == 2):
            count_ambiguity[1] += 1
            print(i, " | ambiguity = 2:", spike[i])
        elif (ambiguity[i] == 3):
            count_ambiguity[2] += 1
            print(i, " | ambiguity = 3:", spike[i])
        elif (ambiguity[i] == 4):
            count_ambiguity[3] += 1
            print(i, " | ambiguity = 4:", spike[i])
        elif (ambiguity[i] == 5):
            count_ambiguity[4] += 1
            print(i, " | ambiguity = 5:", spike[i])
            # print("OpenAngle,CVD,AverageDistance,LengthVolumeRatio,LengthAreaRatio,JunctionArea,Length,Area,Volume,ConvexHullVolume,ConvexHullRatio")
            # print([dataset_11[g, i] for g in range(dataset_11.shape[0])])
        elif (ambiguity[i] == 6):
            count_ambiguity[5] += 1
            print(i, " | ambiguity = 6:", spike[i])
        elif (ambiguity[i] == 7):
            count_ambiguity[6] += 1
            print(i, " | ambiguity = 7:", spike[i])
        elif (ambiguity[i] == 8):
            count_ambiguity[7] += 1
            print(i, " | ambiguity = 8:", spike[i])

    print("count_ambiguity:")
    for j in range(0, k):
        print(count_ambiguity[j]-1)

def probability_40_70_80_90(k, n, result):
    p = np.ones(4)
    print("probability: 40/70/80/90")
    for j in range(0, k):
        for odds in range(0, 4):
            p[odds] = 0
        for i in range(0, n):
            if result[j][i] <= 0.4:
                p[0] += 1
            elif (result[j][i] >= 0.7) & (result[j][i] < 0.8):
                p[1] += 1
            elif (result[j][i] >= 0.8) & (result[j][i] < 0.9):
                p[2] += 1
            elif (result[j][i] >= 0.9):
                p[3] += 1
        print("for ", j+1, ":", p)

def minMax_membership(k, n, spike, result):
    x = np.zeros(n)
    y_2 = np.zeros(n)
    count = np.zeros(k)
    membership_1 = []
    membership_1_number = []
    membership_2 = []
    membership_2_number = []
    membership_3 = []
    membership_3_number = []
    membership_4 = []
    membership_4_number = []
    membership_5 = []
    membership_5_number = []
    membership_6 = []
    membership_6_number = []
    membership_7 = []
    membership_7_number = []
    membership_8 = []
    membership_8_number = []
    cluster = -1
    for i in range(0, n):
        max = 0.0
        membership = 0
        for j in range(0, k):
            x[i] = i + 1
            if (max < result[j][i]):
                max = result[j][i]
                membership = max + j
                cluster = j
        if cluster == 0:
            count[cluster] += 1
            membership_1.append(max)
            membership_1_number.append(i)
        elif cluster == 1:
            count[cluster] += 1
            membership_2.append(max)
            membership_2_number.append(i)
        elif cluster == 2:
            count[cluster] += 1
            membership_3.append(max)
            membership_3_number.append(i)
        elif cluster == 3:
            count[cluster] += 1
            membership_4.append(max)
            membership_4_number.append(i)
        elif cluster == 4:
            count[cluster] += 1
            membership_5.append(max)
            membership_5_number.append(i)
        elif cluster == 5:
            count[cluster] += 1
            membership_6.append(max)
            membership_6_number.append(i)
        elif cluster == 6:
            count[cluster] += 1
            membership_7.append(max)
            membership_7_number.append(i)
        elif cluster == 7:
            count[cluster] += 1
            membership_8.append(max)
            membership_8_number.append(i)
        y_2[i] = membership
    print("количество шипиков в каждом кластере", count)

    for j in range(0, k):
        print('for ', j + 1, ':')
        exec(f"max_{j + 1} = 0")
        exec(f"min_{j + 1} = 1000")
        exec(f"num_{j + 1}_max = 0")
        exec(f"num_{j + 1}_min = 0")
        for mm in range(0, len(eval(f'membership_{j + 1}'))):
            if (eval(f"max_{j + 1}") < eval(f'membership_{j + 1}')[mm]):
                exec(f"max_{j + 1} = {eval(f'membership_{j + 1}')[mm]}")
                exec(f"num_{j + 1}_max = {eval(f'membership_{j + 1}_number')[mm]}")
            if (eval(f"min_{j + 1}") > eval(f'membership_{j + 1}')[mm]):
                exec(f"min_{j + 1} = {eval(f'membership_{j + 1}')[mm]}")
                exec(f"num_{j + 1}_min = {eval(f'membership_{j + 1}_number')[mm]}")
        print(eval(f'num_{j + 1}_min'), ' | ', "min = ", eval(f'min_{j + 1}'), ' | ', spike[eval(f'num_{j + 1}_min')])
        print(eval(f'num_{j + 1}_max'), ' | ', "max = ", eval(f'max_{j + 1}'), ' | ', spike[eval(f'num_{j + 1}_max')], )

def clearСlustering(k, n, result, dataset_11, str_):
    cluster1 = []
    cluster1_num = []
    cluster2 = []
    cluster2_num = []
    cluster3 = []
    cluster3_num = []
    cluster4 = []
    cluster4_num = []
    cluster5 = []
    cluster5_num = []
    cluster6 = []
    cluster6_num = []
    # cluster7 = []
    # cluster7_num = []
    # cluster8 = []
    # cluster8_num = []

    cluster_num = -1
    for i in range(0, n):
        max_m = 0.0
        for j in range(0, k):
            if (max_m < result[j][i]):
                max_m = result[j][i]
                cluster_num = j
        if cluster_num == 0:
            cluster1.append(max_m)
            cluster1_num.append(i)
        elif cluster_num == 1:
            cluster2.append(max_m)
            cluster2_num.append(i)
        elif cluster_num == 2:
            cluster3.append(max_m)
            cluster3_num.append(i)
        elif cluster_num == 3:
            cluster4.append(max_m)
            cluster4_num.append(i)
        elif cluster_num == 4:
            cluster5.append(max_m)
            cluster5_num.append(i)
        elif cluster_num == 5:
            cluster6.append(max_m)
            cluster6_num.append(i)
        # elif cluster_num == 6:
        #     cluster7.append(max_m)
        #     cluster7_num.append(i)
        # elif cluster_num == 7:
        #     cluster8.append(max_m)
        #     cluster8_num.append(i)

    # print("1", len(cluster1_num))
    # print(cluster1)
    # print(cluster1_num)
    #
    # print("2", len(cluster2_num))
    # print(cluster2)
    # print(cluster2_num)
    #
    # print("3", len(cluster3_num))
    # print(cluster3)
    # print(cluster3_num)
    #
    # print("4", len(cluster4_num))
    # print(cluster4)
    # print(cluster4_num)
    #
    # print("5", len(cluster5_num))
    # print(cluster5)
    # print(cluster5_num)
    #
    # print("6", len(cluster6_num))
    # print(cluster6)
    # print(cluster6_num)
    #
    # print("7", len(cluster7_num))
    # print(cluster7)
    # print(cluster7_num)

    # print("8", len(cluster8_num))
    # print(cluster8)
    # print(cluster8_num)

    # print(len(cluster1_num)+len(cluster2_num)+len(cluster3_num)+
    #       len(cluster4_num)+len(cluster5_num)+len(cluster6_num)+len(cluster7_num))

    for met in range(0, 11):
        met_11_1 = []
        met_11_2 = []
        met_11_3 = []
        met_11_4 = []
        met_11_5 = []
        met_11_6 = []
        # met_11_7 = []
        # met_11_8 = []
        for n_11 in range(0, len(cluster1_num)):
            arr = [dataset_11[met, cluster1_num[n_11]]]
            met_11_1 = np.concatenate((met_11_1, arr))
        for n_11 in range(0, len(cluster2_num)):
            arr = [dataset_11[met, cluster2_num[n_11]]]
            met_11_2 = np.concatenate((met_11_2, arr))
        for n_11 in range(0, len(cluster3_num)):
            arr = [dataset_11[met, cluster3_num[n_11]]]
            met_11_3 = np.concatenate((met_11_3, arr))
        for n_11 in range(0, len(cluster4_num)):
            arr = [dataset_11[met, cluster4_num[n_11]]]
            met_11_4 = np.concatenate((met_11_4, arr))
        for n_11 in range(0, len(cluster5_num)):
            arr = [dataset_11[met, cluster5_num[n_11]]]
            met_11_5 = np.concatenate((met_11_5, arr))
        for n_11 in range(0, len(cluster6_num)):
            arr = [dataset_11[met, cluster6_num[n_11]]]
            met_11_6 = np.concatenate((met_11_6, arr))
        # for n_11 in range(0, len(cluster7_num)):
        #     arr = [dataset_11[met, cluster7_num[n_11]]]
        #     met_11_7 = np.concatenate((met_11_7, arr))
        # for n_11 in range(0, len(cluster8_num)):
        #     arr = [dataset_11[met, cluster8_num[n_11]]]
        #     met_11_8 = np.concatenate((met_11_8, arr))

        my_dict = {' 1': met_11_1, ' 2': met_11_2, ' 3': met_11_3,
                   ' 4': met_11_4, ' 5': met_11_5, '6': met_11_6}
        title = ["OpenAngle", "CVD", "AverageDistance", "LengthVolumeRatio", "LengthAreaRatio",
                "JunctionArea", "Length", "Area", "Volume", "ConvexHullVolume", "ConvexHullRatio"]


        fig, ax = plt.subplots()
        ax.boxplot(my_dict.values())
        plt.title(title[met])
        ax.set_xticklabels(my_dict.keys())
        plt.savefig("/Users/Marina/degree_ML/boxPlot/" + str_ + "/" + str(met+1) + ".png")
        plt.show()

    # impotant = []
    # for o in range(0, 3):
    #     max__ = 0.0
    #     count_ = 0
    #     for p in range(0, len(cluster6)):
    #         if(cluster6[p] > max__):
    #             max__ = cluster6[p]
    #             count_ = p
    #     print(max__)
    #     impotant.append(cluster6_num[count_])
    #     cluster6.pop(count_)
    #     cluster6_num.pop(count_)
    # print(impotant)
    # print(spike[impotant[0]])
    # print(spike[impotant[1]])
    # print(spike[impotant[2]])
    # print([dataset_11[g, impotant[0]] for g in range(dataset_11.shape[0])])
    # print([dataset_11[g, impotant[1]] for g in range(dataset_11.shape[0])])
    # print([dataset_11[g, impotant[2]] for g in range(dataset_11.shape[0])])

def clusteringMetrics(k, n, result, dataset_11, str_):
    cluster1 = []
    cluster1_num = []
    cluster2 = []
    cluster2_num = []
    cluster3 = []
    cluster3_num = []
    cluster4 = []
    cluster4_num = []
    cluster5 = []
    cluster5_num = []
    cluster6 = []
    cluster6_num = []


    cluster_num = -1
    for i in range(0, n):
        max_m = 0.0
        for j in range(0, k):
            if (max_m < result[j][i]):
                max_m = result[j][i]
                cluster_num = j
        if cluster_num == 0:
            cluster1.append(max_m)
            cluster1_num.append(i)
        elif cluster_num == 1:
            cluster2.append(max_m)
            cluster2_num.append(i)
        elif cluster_num == 2:
            cluster3.append(max_m)
            cluster3_num.append(i)
        elif cluster_num == 3:
            cluster4.append(max_m)
            cluster4_num.append(i)
        elif cluster_num == 4:
            cluster5.append(max_m)
            cluster5_num.append(i)
        elif cluster_num == 5:
            cluster6.append(max_m)
            cluster6_num.append(i)

    met_11_1 = []
    met_11_2 = []
    met_11_3 = []
    met_11_4 = []
    met_11_5 = []
    met_11_6 = []
    met_11_7 = []
    met_11_8 = []
    met_11_9 = []
    met_11_10 = []
    met_11_11 = []

    for n_11 in range(0, len(cluster1_num)):
        arr = [dataset_11[0, cluster1_num[n_11]]]
        met_11_1 = np.concatenate((met_11_1, arr))
    for n_11 in range(0, len(cluster1_num)):
        arr = [dataset_11[1, cluster1_num[n_11]]]
        met_11_2 = np.concatenate((met_11_2, arr))
    for n_11 in range(0, len(cluster1_num)):
        arr = [dataset_11[2, cluster1_num[n_11]]]
        met_11_3 = np.concatenate((met_11_3, arr))
    # for n_11 in range(0, len(cluster6_num)):
    #     arr = [dataset_11[3, cluster6_num[n_11]]]
    #     met_11_4 = np.concatenate((met_11_4, arr))
    for n_11 in range(0, len(cluster1_num)):
        arr = [dataset_11[4, cluster1_num[n_11]]]
        met_11_5 = np.concatenate((met_11_5, arr))
    for n_11 in range(0, len(cluster1_num)):
        arr = [dataset_11[5, cluster1_num[n_11]]]
        met_11_6 = np.concatenate((met_11_6, arr))
    for n_11 in range(0, len(cluster1_num)):
        arr = [dataset_11[6, cluster1_num[n_11]]]
        met_11_7 = np.concatenate((met_11_7, arr))
    # for n_11 in range(0, len(cluster6_num)):
    #     arr = [dataset_11[7, cluster6_num[n_11]]]
    #     met_11_8 = np.concatenate((met_11_8, arr))
    for n_11 in range(0, len(cluster1_num)):
        arr = [dataset_11[8, cluster1_num[n_11]]]
        met_11_9 = np.concatenate((met_11_9, arr))
    for n_11 in range(0, len(cluster1_num)):
        arr = [dataset_11[9, cluster1_num[n_11]]]
        met_11_10 = np.concatenate((met_11_10, arr))
    for n_11 in range(0, len(cluster1_num)):
        arr = [dataset_11[10, cluster1_num[n_11]]]
        met_11_11 = np.concatenate((met_11_11, arr))


    my_dict = {' OA': met_11_1, ' CVD': met_11_2, ' AD': met_11_3,
                ' LAR': met_11_5, 'JA': met_11_6,
               'L': met_11_7, 'V': met_11_9, 'CHV': met_11_10,
               'CHR': met_11_11}
    title = ['Кластер №1']

    fig, ax = plt.subplots()
    ax.boxplot(my_dict.values())
    plt.title(title[0])
    ax.set_xticklabels(my_dict.keys())
    ax.set_ylim(0, 5)
    # plt.savefig("/Users/Marina/degree_ML/boxPlot/" + str_ + "/k" + str(6) + ".png")
    plt.show()

def errorRealization(k, n, result_my, result):
    error_realization = []
    max_error = 0
    for i in range(0, n):
        for j in range(0, k):
            err_result = abs(result[j][i]-result_my[j][i])
            if(err_result > max_error):
                max_error = err_result/100
        error_realization.append(max_error)
    print(error_realization)

    x = np.arange(1, 330)
    plt.plot(x, error_realization, 'ro-', alpha=0.6)
    plt.grid(True)
    plt.xlabel("номер точки в наборе данных", fontweight='bold', fontsize=14)
    plt.ylabel("максимальная ошибка", fontweight='bold', fontsize=14)
    plt.show()



k = 6

# _str_ = "chords"
_str_ = "classic"

str_ = _str_ + "/dataset"
# str_ = _str_ + "/dataset_gauss"
# str_ = _str_ + "/dataset_gauss_"

path_FCM = "C:/Users/Marina/degree_ML/FCM/" + str_ + "/clusters_"
path = "C:/Users/Marina/degree_ML/data/dataset/" + str_ + ".csv"

dataset = pd.read_csv(path, header=None, index_col=None).values
print(dataset.shape)
n = dataset.shape[1]

# result = pd.read_csv(path_FCM+str(k)+'/FCM.csv', header=None, index_col=None).values

metrics_spike = pd.read_csv("data/metrics_true.csv")
spike = metrics_spike['Spine File']

# metrics = pd.read_csv("data/metrics_true.csv", usecols=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]).transpose()
# dataset_ = pd.DataFrame(metrics)
# dataset_.to_csv("data/dataset11.csv", index=False, header=False)
dataset11 = pd.read_csv('data/dataset11.csv', header=None, index_col=None).values
#-----------------------------------------------------------------------------------------------------------------------
# ambiguitySpikes(k, n, result, dataset11, spike)
# probability_40_70_80_90(k, n, result)
# minMax_membership(k, n, spike, result)
# clearСlustering(k, n, result, dataset11, str_)
# clusteringMetrics(k, n, result, dataset11, str_)


result = pd.read_csv(path_FCM+str(k)+'/FCM_pypypy.csv', header=None, index_col=None).values
result_sk = pd.read_csv(path_FCM+str(k)+'/FCM_cMEANS.csv', header=None, index_col=None).values
errorRealization(k, n, result, result_sk)