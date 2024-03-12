path_FCM = "FCM/clusters_"
path_PCA = "PCA/clusters_"

def DWSVF(k, XB, PBMF, MPC):
    m_DWSVF = []

    for c in range(0, k - 1):
        sum = PBMF[c]+XB[c]+1/MPC[c]
        arg1 = ((sum-PBMF[c])/sum) * PBMF[c]
        arg2 = ((sum-XB[c])/sum) *XB[c]
        arg3 = ((sum-(1/MPC[c]))/sum) * 1/MPC[c]
        dwsvf = arg1+arg2+arg3
        m_DWSVF.append(dwsvf)
    print(m_DWSVF)
    return m_DWSVF