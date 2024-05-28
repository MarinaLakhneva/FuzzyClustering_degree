import numpy as np
import skfuzzy as fuzz
import pandas as pd

k = 7

path_accessories = "FCM/accessories/clusters_"

# str_ = "classic/dataset"
str_ = "chords/dataset"

path_FCM = "FCM/" + str_ + "/clusters_"

dataset = pd.read_csv("data/dataset/" + str_ + ".csv", header=None, index_col=None).values
n = dataset.shape[1]
table_of_accessories = pd.read_csv(path_accessories + str(k) + '/table_of_accessories.csv', header=None, index_col=None).values

cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(
    data=dataset,
    c=k,
    m=2,
    error=0.001,
    maxiter=1000,
    init=table_of_accessories
)

print(u)
frame_result = pd.DataFrame(u)
frame_result.to_csv(path_FCM + str(k) + "/FCM_cMEANS_1000.csv", index=False, header=False)


# from sklearn.cluster import KMeans
#
# kmeans = KMeans(n_clusters=k, init=table_of_accessories, n_init=1, max_iter=1000, tol=0.001)
# kmeans.fit(dataset)
# print(kmeans.inertia_)
# frame_result = pd.DataFrame(u)
# frame_result.to_csv(path_FCM + str(k) + "/FCM_cMEANS_1000.csv", index=False, header=False)