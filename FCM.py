import numpy as np
import pandas as pd

# k - количество кластеров 1<j<k
# d - размерность вектора данных 1<l<d
# n - мощность выборки

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
    cluster_center_for_PCA.to_csv("result_FCM/clusters_"+str(k)+"/cluster_center.csv", index=False, header=False)
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

def solution(k, n, data, d, table, m, E):
    max = 1000
    iteration = 0

    while(max > E):
        coordinates = 0
        distance = 0
        affiliation = 0
        iteration = iteration + 1

        coordinates = calculating_the_coordinates_of_the_cluster_center(k, n, data, d, table, m)
        distance = distance_calculation(k, n, data, d, coordinates, m)
        affiliation = calculating_the_degree_of_affiliation(k, n, m, distance)

        max = 0.0
        for j in range(0, k):
            for i in range(0, n):
                difference = affiliation[j][i]-table[j][i]
                if (difference > max):
                    max = difference
        table = affiliation
    dist = pd.DataFrame(distance)
    dist.to_csv("result_FCM/clusters_"+str(k)+"/distance.csv", index=False, header=False)
    return table


def main(number_of_clusters):
    # # удалила шипики которых нет в 0.025 0.025 0.1 dataset
    # import glob
    #
    # metrics_d = pd.read_csv("data/metrics.csv")
    # print(len(metrics_d))
    # to_delete = []
    # for index, p in enumerate(metrics_d['Spine File'].to_numpy()):
    #     if p.replace("/", "\\") not in glob.glob('0.025 0.025 0.1 dataset/*/*.off', recursive=True):
    #         to_delete.append(index)
    #
    # for n_drop in range(0, len(to_delete)):
    #     metrics_d = metrics_d.drop(to_delete[n_drop])
    # metrics_d.to_csv("data/metrics_update.csv", index=False)

    metrics = pd.read_csv("data/metrics_update.csv")
    property = metrics['OldChordDistribution']
    dataset = np.zeros((len(property[0].split()), len(property)))

    for i in range(0, len(property)):
        for j in range(0, len(property[0].split())):
            dataset[j][i] = list(map(float, property[i][1:-1].split()))[j]

    dataset_for_PCA = pd.DataFrame(dataset)
    dataset_for_PCA.to_csv("result_FCM/clusters_"+str(number_of_clusters)+"/dataset.csv", index=False, header=False)

    eps = 0.0001
    degree_of_fuzziness = 2
    number_of_elements = len(property)
    number_of_dataset = len(property[0].split())

    #заполняем таблицу принадлежности случайными значениями
    table_of_accessories = np.random.rand(number_of_clusters, number_of_elements)
    table_of_accessories /= np.sum(table_of_accessories, axis=0)

    result = solution(number_of_clusters,
             number_of_elements,
             dataset,
             number_of_dataset,
             table_of_accessories,
             degree_of_fuzziness,
             eps)

    frame = pd.DataFrame(result)
    frame.to_csv("result_FCM/clusters_"+str(number_of_clusters)+"/result_FCM.csv", index=False, header=False)

if __name__ == '__main__':
    #1
    clusters = 3
    main(clusters)