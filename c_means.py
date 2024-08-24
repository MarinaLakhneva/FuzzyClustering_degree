import numpy as np
import skfuzzy as fuzz
import pandas as pd

k = 14

path_accessories = "FCM/accessories/clusters_"

str_ = "classic/dataset"
# str_ = "chords/dataset"

path_FCM = "FCM/" + str_ + "_c/clusters_"

dataset = pd.read_csv("data/dataset/" + str_ + ".csv", header=None, index_col=None).values
n = dataset.shape[1]
for j in range(1, k + 1):
    table_of_accessories = pd.read_csv(path_accessories + str(j) + '/table_of_accessories.csv', header=None, index_col=None).values

    cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(
        data=dataset,
        c=j,
        m=2,
        error=0.001,
        maxiter=47,
        init=table_of_accessories
    )

    frame_result = pd.DataFrame(u)
    frame_result.to_csv(path_FCM + str(j) + "/FCM.csv", index=False, header=False)

