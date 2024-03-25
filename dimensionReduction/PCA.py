import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as geek

path_FCM = "FCM/clusters_"
path_PCA = "PCA/clusters_"

def pca(k):
    filename1_in = path_FCM+str(k)+"/cluster_center.csv"
    filename2_in = path_FCM+str(k)+"/dataset.csv"
    filename1_out = path_PCA+str(k)+"/datasetPLUScenter_PCA.csv"
    filename2_out = path_PCA+str(k)+"/center_PCA.csv"

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

    from sklearn.decomposition import PCA

    pca = PCA(n_components=3)
    principalComponents = pca.fit_transform(data)

    result = pd.DataFrame(principalComponents)
    result.to_csv(filename2_out, index=False, header=False)
    return result