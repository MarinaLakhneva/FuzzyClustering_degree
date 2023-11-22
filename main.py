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
    print(u_ij)

def calculating_the_coordinates_of_the_cluster_center(k, n, dataset, d, table, m):
    c_jl = np.zeros((d, k))

    for j in range(0, k): # 2
        for l in range(0, d): # 2 -> 3
            nomerstor = 0.0
            denomerstor = 0.0
            for i in range(0, n): # 4
                nomerstor += table[j][i]**m * dataset[l][i]
                denomerstor += table[j][i]**m
            c_jl[l][j] = nomerstor/denomerstor

    distance_calculation(k, n, dataset, d, c_jl, m)

# евклидово расстояние
def distance_calculation(k, n,  dataset, d, c_ij, m):
    dist = np.zeros((k, n))

    for j in range(0, k):
        for i in range(0, n):
            sum = 0.0
            for l in range(0, d):
                sum += (dataset[l][i] - c_ij[l][j])**m
            dist[j][i] = np.sqrt(sum)

    calculating_the_degree_of_affiliation(k, n, m, dist)


def main():
    # degree_of_fuzziness = 2
    # number_of_clusters = 2
    # number_of_elements = 4
    # number_of_dataset = 3
    #
    # dataset = [[1, 2, 4, 7], [3, 5, 8, 9], [2, 1, 4, 9]]
    # table_of_accessories = [[0.8, 0.7, 0.2, 0.1], [0.2, 0.3, 0.8, 0.9]]

    filename = "metrics.csv"
    metrics = pd.read_csv(filename)
    property = metrics['OldChordDistribution']

    dataset = np.zeros((len(property[0].split()), len(property)))

    for i in range(0, len(property)):
        for j in range(0, len(property[0].split())):
            dataset[j][i] = list(map(float, property[i][1:-1].split()))[j]

    degree_of_fuzziness = 2
    number_of_clusters = 5
    number_of_elements = len(property)
    number_of_dataset = len(property[0].split())

    #заполняем таблицу принадлежности случайными значениями
    table_of_accessories = np.random.rand(number_of_clusters, number_of_elements)
    table_of_accessories /= np.sum(table_of_accessories, axis=0)

    calculating_the_coordinates_of_the_cluster_center(number_of_clusters,
                                                      number_of_elements,
                                                      dataset,
                                                      number_of_dataset,
                                                      table_of_accessories,
                                                      degree_of_fuzziness)


if __name__ == '__main__':
  main()