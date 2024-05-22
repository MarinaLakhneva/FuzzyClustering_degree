import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import multivariate_normal

k = 8

str_ = "chords/dataset"
# str_ = "classic/dataset"


path_FCM = "C:/Users/Marina/degree_ML/FCM/" + str_ + "/clusters_"


#gauss
# data = pd.read_csv("data/dataset/" + str_ + ".csv", header=None, index_col=None).values
#
# x = data.transpose() # (331, 100)
# mean_ = np.mean(x, axis=0) # (100)
# cov_ = np.cov(data, bias=True) # (100, 100))
#
# gauss_ = np.random.multivariate_normal(mean_, cov=cov_, size=data.shape[1]).transpose()
#
# for lst in gauss_:
#     for i, val in enumerate(lst):
#         lst[i] = max(val, 0)
# print(gauss_.shape)
# gauss_data = pd.DataFrame(gauss_)
# gauss_data.to_csv("data/dataset/" + str_ + "_gauss.csv", index=False, header=False)
#-----------------------------------------------------------------------------------------------------------------------
#gauss_C
for m in range(1, k+1):
    data = pd.read_csv("data/dataset/" + str_ + "_" + str(m) + ".csv", header=None, index_col=None).values

    mean_ = pd.read_csv(path_FCM + str(k) + '/cluster_center.csv', header=None,index_col=None).values[:, m-1]
    cov_ = np.cov(data, bias=True)

    gauss_ = np.random.multivariate_normal(mean_, cov=cov_, size=data.shape[1]).transpose()

    for lst in gauss_:
        for i, val in enumerate(lst):
            lst[i] = max(val, 0)
    print(gauss_.shape)
    gauss_data = pd.DataFrame(gauss_)
    gauss_data.to_csv("data/dataset/" + str_ + "_gauss" + str(m) + ".csv", index=False, header=False)

matrices = []
for i in range(1, k+1):
    filename = f'C:/Users/Marina/degree_ML/data/dataset/' + str_ + '_gauss' + str(i) + '.csv'
    matrix = pd.read_csv(filename, header=None)
    matrices.append(matrix)

result_matrix = pd.concat(matrices, axis=1)

gauss_data = pd.DataFrame(result_matrix)
gauss_data.to_csv("data/dataset/" + str_ + "_gauss_" + str(k) + ".csv", index=False, header=False)

data_gauss = pd.read_csv("data/dataset/" + str_ + "_gauss_" + str(k) + ".csv", header=None, index_col=None).values
index = [8, 23, 24, 28, 42, 56, 69, 71, 76, 84, 85, 95, 101, 102, 122, 127, 133, 141, 146, 155, 156, 157, 159, 174, 176, 177, 182, 186, 194, 197, 199, 207, 210, 216, 230, 231, 246, 274, 297, 326, 149, 150, 153, 162, 163, 166, 171, 179, 184, 203, 208, 214, 222, 223, 224, 232, 234, 243, 244, 245, 252, 258, 259, 261, 263, 264, 267, 271, 273, 275, 277, 282, 289, 298, 299, 300, 303, 309, 311, 318, 320, 6, 10, 16, 19, 21, 25, 26, 31, 33, 38, 43, 45, 57, 68, 72, 79, 89, 92, 98, 99, 103, 105, 115, 120, 121, 125, 126, 131, 136, 137, 138, 147, 164, 183, 206, 225, 242, 249, 256, 257, 266, 276, 9, 27, 44, 48, 54, 55, 134, 142, 148, 151, 160, 165, 173, 178, 180, 181, 190, 192, 193, 198, 202, 204, 205, 209, 211, 213, 215, 218, 220, 228, 240, 253, 254, 269, 270, 272, 280, 283, 284, 285, 286, 287, 288, 291, 292, 294, 301, 307, 312, 315, 316, 317, 4, 91, 93, 96, 106, 139, 167, 175, 185, 189, 191, 196, 200, 219, 221, 226, 227, 229, 237, 239, 248, 295, 305, 306, 329, 1, 3, 5, 7, 12, 13, 18, 20, 29, 30, 35, 47, 49, 53, 58, 59, 61, 63, 65, 74, 75, 80, 82, 87, 88, 100, 108, 110, 111, 112, 117, 123, 124, 128, 132, 135, 140, 143, 168, 188, 236, 238, 247, 251, 255, 262, 278, 293, 296, 304, 308, 313, 319, 322, 323, 328, 14, 15, 36, 40, 62, 66, 67, 97, 104, 113, 114, 144, 152, 158, 195, 212, 217, 235, 281, 321, 0, 2, 11, 17, 22, 32, 34, 37, 39, 41, 46, 50, 51, 52, 60, 64, 70, 73, 77, 78, 81, 83, 86, 90, 94, 107, 109, 116, 118, 119, 129, 130, 145, 154, 161, 169, 170, 172, 187, 201, 233, 241, 250, 260, 265, 268, 279, 290, 302, 310, 314, 324, 325, 327]
matrix_permuted = data_gauss[:, index]

gauss_true = pd.DataFrame(matrix_permuted)
gauss_true.to_csv("data/dataset/" + str_ + "_gauss_" + str(k) + "_true.csv", index=False, header=False)
