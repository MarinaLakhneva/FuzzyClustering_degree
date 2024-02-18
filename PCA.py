import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as geek

def main(file1_in, file2_in, file1_out, file2_out):
    file1 = pd.read_csv(file1_in, header=None, index_col=None).values
    file2 = pd.read_csv(file2_in, header=None, index_col=None).values

    f1 = file1.transpose()
    f2 = file2.transpose()
    gfg = geek.concatenate((f1, f2), axis=0)

    gfgT = gfg.transpose()
    opa = pd.DataFrame(gfgT)
    opa.to_csv(file1_out, index=False, header=False)

    data = gfgT.transpose()
    data = StandardScaler().fit_transform(data)

    from sklearn.decomposition import PCA

    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(data)

    result = pd.DataFrame(principalComponents)
    result.to_csv(file2_out, index=False, header=False)


if __name__ == '__main__':
    #2
    k = 3
    filename1_in = "result_FCM/clusters_"+str(k)+"/cluster_center.csv"
    filename2_in = "result_FCM/clusters_"+str(k)+"/dataset.csv"
    filename1_out = "result_PCA/clusters_"+str(k)+"/datasetPLUScenter_PCA.csv"
    filename2_out = "result_PCA/clusters_"+str(k)+"/center_PCA.csv"
    main(filename1_in, filename2_in, filename1_out, filename2_out)