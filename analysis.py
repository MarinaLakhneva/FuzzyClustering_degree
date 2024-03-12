import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


path_FCM = "FCM/clusters_"

def info(k):
    metrics = pd.read_csv("data/metrics_update.csv")
    metric = metrics['OldChordDistribution']

    dataset = np.zeros((len(metric[0].split()), len(metric)))
    for i in range(0, len(metric)):
        for j in range(0, len(metric[0].split())):
            dataset[j][i] = list(map(float, metric[i][1:-1].split()))[j]

    number_of_elements = len(metric)

    # 11-ть метрик
    # dataset = pd.read_csv(path_FCM + str(number_of_clusters) + '/dataset.csv', header=None, index_col=None).values
    # number_of_elements = dataset.shape[1]

    metrics_11 = pd.read_csv("data/metrics_update.csv", usecols=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]).transpose()

    dataset_m = pd.DataFrame(metrics_11)
    dataset_m.to_csv(path_FCM+str(k)+"/dataset_11.csv", header=False, index=False)
    dataset_11 = pd.read_csv(path_FCM+str(k)+'/dataset_11.csv', header=None, index_col=None).values


    result = pd.read_csv(path_FCM+str(k)+'/FCM.csv', header=None, index_col=None).values
#----------------------------------------------------------------------------------------------------------------------
    difference = 0.1
    ambiguity = np.ones(number_of_elements)
    for i in range(0, number_of_elements):
        max_membership = 0
        for j in range(0, k):
            if(max_membership < result[j][i]):
                max_membership = result[j][i]
        for j in range(0, k):
            if(max_membership != result[j][i]):
                if((max_membership - result[j][i]) < difference):
                    ambiguity[i] += 1

    metrics = pd.read_csv("data/metrics_update.csv")
    spike = metrics['Spine File']
    feature = metrics['Spine File']
    count_ambiguity = np.ones(k)
    for i in range(0, number_of_elements):
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
            print("OpenAngle,CVD,AverageDistance,LengthVolumeRatio,LengthAreaRatio,JunctionArea,Length,Area,Volume,ConvexHullVolume,ConvexHullRatio")
            print([dataset_11[g, i] for g in range(dataset_11.shape[0])])
        elif (ambiguity[i] == 6):
            count_ambiguity[5] += 1
            print(i, " | ambiguity = 6:", spike[i])
            print("OpenAngle,CVD,AverageDistance,LengthVolumeRatio,LengthAreaRatio,JunctionArea,Length,Area,Volume,ConvexHullVolume,ConvexHullRatio")
            print([dataset_11[g, i] for g in range(dataset_11.shape[0])])
        elif (ambiguity[i] == 7):
            count_ambiguity[6] += 1
            print(i, " | ambiguity = 7:", spike[i])
            print("OpenAngle,CVD,AverageDistance,LengthVolumeRatio,LengthAreaRatio,JunctionArea,Length,Area,Volume,ConvexHullVolume,ConvexHullRatio")
            print([dataset_11[g, i] for g in range(dataset_11.shape[0])])
        elif (ambiguity[i] == 8):
            count_ambiguity[7] += 1
            print(i, " | ambiguity = 8:", spike[i])


    print("count_ambiguity:")
    for j in range(0, k):
        print(count_ambiguity[j]-1)
#----------------------------------------------------------------------------------------------------------------------
    # 40/70/80/90 - 4
    p = np.ones(4)
    print("probability: 40/70/80/90")
    for j in range(0, k):
        for odds in range(0, 4):
            p[odds] = 0
        for i in range(0, number_of_elements):
            if result[j][i] <= 0.4:
                p[0] += 1
            elif (result[j][i] >= 0.7) & (result[j][i] < 0.8):
                p[1] += 1
            elif (result[j][i] >= 0.8) & (result[j][i] < 0.9):
                p[2] += 1
            elif (result[j][i] >= 0.9):
                p[3] += 1
        print("for ", j+1, ":", p)
#----------------------------------------------------------------------------------------------------------------------
    x = np.zeros(number_of_elements)
    y_2 = np.zeros(number_of_elements)
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
    for i in range(0, number_of_elements):
        max = 0.0
        membership = 0
        for j in range(0, k):
            x[i] = i + 1
            if (max < result[j][i]):
                max = result[j][i]
                membership = max+j
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
        print('for ', j+1, ':')
        exec(f"max_{j+1} = 0")
        exec(f"min_{j+1} = 1000")
        exec(f"num_{j + 1}_max = 0")
        exec(f"num_{j + 1}_min = 0")
        for mm in range(0, len(eval(f'membership_{j+1}'))):
            if (eval(f"max_{j+1}") < eval(f'membership_{j+1}')[mm]):
                exec(f"max_{j+1} = {eval(f'membership_{j+1}')[mm]}")
                exec(f"num_{j + 1}_max = {eval(f'membership_{j+1}_number')[mm]}")
            if (eval(f"min_{j+1}") > eval(f'membership_{j+1}')[mm]):
                exec(f"min_{j+1} = {eval(f'membership_{j+1}')[mm]}")
                exec(f"num_{j + 1}_min = {eval(f'membership_{j+1}_number')[mm]}")
        print(eval(f'num_{j+1}_min'), ' | ',  "min = ", eval(f'min_{j+1}'), ' | ', spike[eval(f'num_{j+1}_min')])
        print(eval(f'num_{j+1}_max'), ' | ',  "max = ", eval(f'max_{j+1}'), ' | ', spike[eval(f'num_{j+1}_max')], )
#-----------------------------------------------------------------------------------------------------------------------
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
    cluster7 = []
    cluster7_num = []
    cluster8 = []
    cluster8_num = []

    cluster_num = -1
    for i in range(0, number_of_elements):
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
        elif cluster_num == 6:
            cluster7.append(max_m)
            cluster7_num.append(i)
        elif cluster_num == 7:
            cluster8.append(max_m)
            cluster8_num.append(i)

    print(cluster1)
    print(cluster1_num)

    print(cluster2)
    print(cluster2_num)

    print(cluster3)
    print(cluster3_num)

    print(cluster4)
    print(cluster4_num)

    print(cluster5)
    print(cluster5_num)

    print(cluster6)
    print(cluster6_num)

    print(cluster7)
    print(cluster7_num)

    print(cluster8)
    print(cluster8_num)

    # impotant = []
    # for o in range(0, 3):
    #     max__3 = 0.0
    #     count_3 = 0
    #     for p in range(0, len(cluster3)):
    #         if(cluster3[p] > max__3):
    #             max__3 = cluster3[p]
    #             count_3 = p
    #     print(max__3)
    #     impotant.append(cluster3_num[count_3])
    #     cluster3.pop(count_3)
    #     cluster3_num.pop(count_3)
    # print(impotant)
    # print(spike[impotant[0]])
    # print(spike[impotant[1]])
    # print(spike[impotant[2]])
    # print([dataset_11[g, impotant[0]] for g in range(dataset_11.shape[0])])
    # print([dataset_11[g, impotant[1]] for g in range(dataset_11.shape[0])])
    # print([dataset_11[g, impotant[2]] for g in range(dataset_11.shape[0])])