import numpy as np
import pandas as pd

# k - количество кластеров 1<j<k
# d - размерность вектора данных 1<l<d
# n - мощность выборки

path_FCM = "FCM/clusters_"

def calculating_the_degree_of_affiliation(k, n, m, dist):
    u_ij = np.zeros((k, n))
    extent = 1/(1-m)

    for i in range(0, n):
        for j in range(0, k):
            sum = 0.0
            for t in range(0, k):
                sum += (dist[j][i]/dist[t][i])**2
            u_ij[j][i] = sum**extent

    return u_ij

def calculating_the_coordinates_of_the_cluster_center(k, n, data, d, table, m):
    c_jl = np.zeros((d, k))

    for j in range(0, k):
        for l in range(0, d):
            nomerstor = 0.0
            denomerstor = 0.0
            for i in range(0, n):
                nomerstor += table[j][i]**m * data[l][i]
                denomerstor += table[j][i]**m
            c_jl[l][j] = nomerstor/denomerstor

    cluster_center_for_PCA = pd.DataFrame(c_jl)
    cluster_center_for_PCA.to_csv(path_FCM+str(k)+"/cluster_center.csv", index=False, header=False)
    return c_jl

# евклидово расстояние
def distance_calculation(k, n,  data, d, c_ij, m):
    dist = np.zeros((k, n))

    for j in range(0, k):
        for i in range(0, n):
            sum = 0.0
            for l in range(0, d):
                sum += (data[l][i] - c_ij[l][j])**m
            dist[j][i] = np.sqrt(sum)
    return dist

def normalize(h_):
    return h_ / np.sum(h_)

def distance_bhattacharyya(k, n,  data, c_ij):
    dist = np.zeros((k, n))
    for j in range(0, k):
        for i in range(0, n):
            res = 1 - np.sum(np.sqrt(np.multiply(normalize(data[:, i]), normalize(c_ij[:, j]))))
            dist[j][i] = res
    return dist

def solution(k, n, data, d, table, m, E):
    max = 1000
    dif = []
    x = []
    count = 0

    while(max > E):
        count += 1
        coordinates = calculating_the_coordinates_of_the_cluster_center(k, n, data, d, table, m)
        # ВЫБЕРИ МЕТОД ПО КОТОРОМУ ВЫЧИСЛЯТЬ РАССТОЯНИЯ
        # distance = distance_calculation(k, n, data, d, coordinates, m)
        distance = distance_bhattacharyya(k, n, data, coordinates)
        affiliation = calculating_the_degree_of_affiliation(k, n, m, distance)

        max = 0.0
        for j in range(0, k):
            for i in range(0, n):
                difference = affiliation[j][i]-table[j][i]
                if (difference > max):
                    max = difference
        table = affiliation
        x.append(count)
        dif.append(max)

    dist = pd.DataFrame(distance)
    dist.to_csv(path_FCM+str(k)+"/distance.csv", index=False, header=False)

    # print(count)
    # print("difference: ", dif)

    # import matplotlib.pyplot as plt
    # plt.plot(x, dif, 'ro-', alpha=0.6)
    # plt.grid(True)
    # plt.title("eps = "+str(E)+", k=3")
    # plt.xlabel("number iteration", fontweight='bold', fontsize="large")
    # plt.ylabel("difference", fontweight='bold', fontsize="large")
    # plt.show()

    return table

def fcm(k, dataset, n, d):
    print(k)

    eps = 0.001
    degree_of_fuzziness = 2

    # заполняем таблицу принадлежности случайными значениями
    table_of_accessories_ = np.random.rand(k, n)
    table_of_accessories_ /= np.sum(table_of_accessories_, axis=0)

    table_of_accessories_ = pd.DataFrame(table_of_accessories_)
    table_of_accessories_.to_csv(path_FCM+str(k)+"/table_of_accessories.csv", index=False, header=False)
    table_of_accessories = pd.read_csv(path_FCM + str(k) + '/table_of_accessories.csv', header=None, index_col=None).values

    result = solution(k, n, dataset, d, table_of_accessories, degree_of_fuzziness, eps)
    frame_result = pd.DataFrame(result)
    frame_result.to_csv(path_FCM+str(k)+"/FCM.csv", index=False, header=False)