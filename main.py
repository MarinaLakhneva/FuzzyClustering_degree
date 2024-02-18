import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main(number_of_clusters):
    metrics = pd.read_csv("data/metrics_update.csv")
    property = metrics['OldChordDistribution']

    dataset = np.zeros((len(property[0].split()), len(property)))
    for i in range(0, len(property)):
        for j in range(0, len(property[0].split())):
            dataset[j][i] = list(map(float, property[i][1:-1].split()))[j]

    number_of_elements = len(property)
    result = pd.read_csv('result_FCM/clusters_'+str(number_of_clusters)+'/result_FCM.csv', header=None, index_col=None).values
#----------------------------------------------------------------------------------------------------------------------
    difference = 0.1
    ambiguity = np.ones(number_of_elements)
    for i in range(0, number_of_elements):
        max_membership = 0
        for j in range(0, number_of_clusters):
            if(max_membership < result[j][i]):
                max_membership = result[j][i]
        for j in range(0, number_of_clusters):
            if(max_membership != result[j][i]):
                if((max_membership - result[j][i]) < difference):
                    ambiguity[i] += 1

    spike = metrics['Spine File']
    count_ambiguity = np.ones(number_of_clusters)
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

    print("count_ambiguity:")
    for j in range(0, number_of_clusters):
        print(count_ambiguity[j])
#----------------------------------------------------------------------------------------------------------------------
    # 40/70/80/90 - 4
    p = np.ones(4)
    print("probability: 40/70/80/90")
    for j in range(0, number_of_clusters):
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
    count = np.zeros(number_of_clusters)
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
    cluster = -1
    for i in range(0, number_of_elements):
        max = 0.0
        membership = 0
        for j in range(0, number_of_clusters):
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
        y_2[i] = membership
    print("количество шипиков в каждом кластере", count)

    for j in range(0, number_of_clusters):
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
#--------------------------------------------------гистограмма---------------------------------------------------------
    # for j in range(0, number_of_clusters):
    #     plt.title('cluster '+str(j))
    #     plt.xlabel('probability')
    #     plt.ylabel('number of spikes')
    #     plt.hist(eval(f'membership_{j+1}'), color='pink')
    #     plt.legend()
    #     plt.show()
    #     plt.savefig('/Users/Marina/degree_ML/charts/clusters_'+str(number_of_clusters)+'/hist.png')
#------------------------------------------------------PCA-------------------------------------------------------------
    from sklearn.preprocessing import StandardScaler

    data = dataset.transpose()
    data = StandardScaler().fit_transform(data)

    from sklearn.decomposition import PCA

    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(data)

    x = np.zeros(number_of_elements)
    y = np.zeros(number_of_elements)
    for i in range(0, number_of_elements):
        x[i] = principalComponents[i][0]
        y[i] = principalComponents[i][1]

# ------------------------------------------------------TSN-------------------------------------------------------------
#     from sklearn.manifold import TSNE
#
#     data = dataset.transpose()
#     data = StandardScaler().fit_transform(data)
#
#     tsne = TSNE(n_components=2, random_state=0)
#     projections = tsne.fit_transform(data)
#
#
#     x = np.zeros(number_of_elements)
#     y = np.zeros(number_of_elements)
#     for i in range(0, number_of_elements):
#         x[i] = projections[i][0]
#         y[i] = projections[i][1]

#---------------------------------------------------графики------------------------------------------------------------

    for k in range(0, number_of_clusters):
        fig = plt.figure(figsize=(20, 10))
        ax = fig.add_subplot(1, 1, 1)
        ax.set_xlabel('Principal Component 1', fontsize=15)
        ax.set_ylabel('Principal Component 2', fontsize=15)
        ax.set_title('Cluster ' + str(k + 1), fontsize=20)
        probability = np.zeros(len(result[0]))
        for j in range(0, len(result[0])):
            probability[j] = result[k][j]
        ax.scatter(x, y, s=60, alpha=0.5, c=probability, cmap="PuRd", edgecolors="black")
        plt.savefig('/Users/Marina/degree_ML/charts/clusters_'+str(number_of_clusters)+'/cluster_'+str(k+1)+'.png')
        #plt.show()


    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title('Clusters ', fontsize=20)
    ax.set_xlabel('Principal Component 1', fontsize=15)
    ax.set_ylabel('Principal Component 2', fontsize=15)
    colors = ['#ea9999', '#ffe599', '#b6d7a8', '#9fc5e8', '#d9d2e9']
    for k in range(0, number_of_clusters):
        probability = np.zeros(len(result[0]))
        for j in range(0, len(result[0])):
            probability[j] = result[k][j]
        ax.scatter(x, y, s=60, alpha=probability, color=colors[k], edgecolors="black")
    ax.legend(["1", "2", "3", "4", "5"])
    for k in range(0, number_of_clusters):
        ax.get_legend().legend_handles[k].set_alpha(1)
    center_x = np.zeros(number_of_clusters)
    center_y = np.zeros(number_of_clusters)
    #ВЫБЕРИ МЕТОД СОКРАЩЕНИЯ РАЗМЕРНОСТИ
    center = pd.read_csv('result_PCA/clusters_'+str(number_of_clusters)+'/center_PCA.csv', header=None, index_col=None).values
    for k in range(0, number_of_clusters):
        center_x[k] = center[k][0]
        center_y[k] = center[k][1]
    center_color = ['#ea9999', '#ffe599', '#b6d7a8']
    #center_color = ['#ea9999', '#ffe599', '#b6d7a8', '#9fc5e8', '#d9d2e9']
    plt.scatter(center_x, center_y,  s=60, marker="^", color=center_color, edgecolors="red")
    plt.savefig('/Users/Marina/degree_ML/charts/clusters_'+str(number_of_clusters)+'/clusters'+str(number_of_clusters)+'.png')
    plt.show()

    distance = pd.read_csv('result_FCM/clusters_'+str(number_of_clusters)+'/distance.csv', header=None, index_col=None).values
    dist_1 = []
    dist_2 = []
    dist_3 = []
    dist_4 = []
    dist_5 = []

    for i in range(0, number_of_elements):
        count_cluster = 0
        min_dist = 1000
        for k in range(0, number_of_clusters):
            if(min_dist > distance[k][i]):
                min_dist = distance[k][i]
                count_cluster = k+1
        if(count_cluster == 1):
            dist_1.append(min_dist)
        elif(count_cluster == 2):
            dist_2.append(min_dist)
        elif(count_cluster == 3):
            dist_3.append(min_dist)
        elif(count_cluster == 4):
            dist_4.append(min_dist)
        elif (count_cluster == 5):
            dist_5.append(min_dist)

    plt.xlabel('Number of clusters')
    plt.ylabel('distance')
    plt.title('Intracluster distance')
    y_dist_1 = np.ones(len(dist_1))
    y_dist_2 = np.ones(len(dist_2))
    y_dist_3 = np.ones(len(dist_3))
    y_dist_4 = np.ones(len(dist_4))
    y_dist_5 = np.ones(len(dist_5))

    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    s5 = 0
    for d_1 in range(0, len(dist_1)):
        s1 += dist_1[d_1]
    plt.plot(y_dist_1, dist_1, color="#ea9999")
    for d_2 in range(0, len(dist_2)):
        y_dist_2[d_2] = 2
        s2 += dist_2[d_2]
    plt.plot(y_dist_2, dist_2, color="#ffe599")
    for d_3 in range(0, len(dist_3)):
        y_dist_3[d_3] = 3
        s3 += dist_3[d_3]
    plt.plot(y_dist_3, dist_3, color="#b6d7a8")
    for d_4 in range(0, len(dist_4)):
        y_dist_4[d_4] = 4
        s4 += dist_4[d_4]
    plt.plot(y_dist_4, dist_4, color="#9fc5e8" )
    for d_5 in range(0, len(dist_5)):
        y_dist_5[d_5] = 5
        s5 += dist_5[d_5]
    plt.plot(y_dist_5, dist_5, color="#d9d2e9")
    plt.legend([round(s1), round(s2), round(s3)])
    plt.legend([round(s1), round(s2), round(s3), round(s4), round(s5)])
    plt.show()

if __name__ == '__main__':
    clusters = 3
    main(clusters)



