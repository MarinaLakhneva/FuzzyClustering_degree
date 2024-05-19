import pandas as pd
import numpy as np

str_ = "chords/dataset"
# str_ = "chords/dataset_gauss"
# str_ = "chords/dataset_gauss_C"

# str_ = "classic/dataset"
# str_ = "classic/dataset_gauss"
# str_ = "classic/dataset_gauss_C"

#chords
metrics = pd.read_csv("data/metrics_update.csv")
OldChordDistribution_metric = metrics['OldChordDistribution']

dataset_gauss_C = np.zeros((len(OldChordDistribution_metric[0].split()), len(OldChordDistribution_metric)))
for i in range(0, len(OldChordDistribution_metric)):
    for j in range(0, len(OldChordDistribution_metric[0].split())):
        dataset_gauss_C[j][i] = list(map(float, OldChordDistribution_metric[i][1:-1].split()))[j]

dataset_for_PCA = pd.DataFrame(dataset_gauss_C)
dataset_for_PCA.to_csv("data/dataset/" + str_ + ".csv", index=False, header=False)
#-----------------------------------------------------------------------------------------------------------------------
#classic
# metrics = pd.read_csv("data/metrics_update_drop.csv", usecols=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]).transpose()
# dataset_for_PCA = pd.DataFrame(metrics)
# dataset_for_PCA.to_csv("data/dataset/" + str_ + ".csv", index=False, header=False)