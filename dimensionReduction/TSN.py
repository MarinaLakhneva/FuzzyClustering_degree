import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as geek
from sklearn.manifold import TSNE

path_FCM = "C:/Users/Marina/degree_ML/FCM/clusters_"
path_TSN = "C:/Users/Marina/degree_ML/dimensionReduction/TSN/clusters_"

def metricTSN(k):
    filename1_in = path_FCM+str(k)+"/cluster_center.csv"
    filename2_in = path_FCM+str(k)+"/dataset_gauss_C.csv"
    filename1_out = path_TSN+str(k)+"/datasetPLUScenter_TSN.csv"
    filename2_out = path_TSN+str(k)+"/center_TSN.csv"

    file1 = pd.read_csv(filename1_in, header=None, index_col=None).values
    file2 = pd.read_csv(filename2_in, header=None, index_col=None).values

    f1 = file1.transpose()
    f2 = file2.transpose()
    gfg = geek.concatenate((f1, f2), axis=0)

    gfgT = gfg.transpose()
    opa = pd.DataFrame(gfgT)
    opa.to_csv(filename1_out, index=False, header=False)

    data = gfgT.transpose()
    data = StandardScaler().fit_transform(data)

    tsne = TSNE(n_components=2, random_state=0)
    projections = tsne.fit_transform(data)

    result = pd.DataFrame(projections)
    result.to_csv(filename2_out, index=False, header=False)




