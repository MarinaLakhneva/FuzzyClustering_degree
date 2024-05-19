import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import multivariate_normal

k = 6

str_ = "chords/dataset"
# str_ = "classic/dataset"


path_FCM = "C:/Users/Marina/degree_ML/FCM/" + str_ + "/clusters_"


#gauss
data = pd.read_csv("data/dataset/" + str_ + ".csv", header=None, index_col=None).values

x = data.transpose() # (331, 100)
mean_ = np.mean(x, axis=0) # (100)
cov_ = np.cov(data, bias=True) # (100, 100))

gauss_ = np.random.multivariate_normal(mean_, cov=cov_, size=data.shape[1]).transpose()

for lst in gauss_:
    for i, val in enumerate(lst):
        lst[i] = max(val, 0)
print(gauss_.shape)
gauss_data = pd.DataFrame(gauss_)
gauss_data.to_csv("data/dataset/" + str_ + "_gauss.csv", index=False, header=False)
#-----------------------------------------------------------------------------------------------------------------------
#gauss_C
# for m in range(1, k+1):
#     data = pd.read_csv("data/dataset/" + str_ + "_" + str(m) + ".csv", header=None, index_col=None).values
#
#     mean_ = pd.read_csv(path_FCM + str(k) + '/cluster_center.csv', header=None,index_col=None).values[:, m-1]
#     cov_ = np.cov(data, bias=True)
#
#     gauss_ = np.random.multivariate_normal(mean_, cov=cov_, size=data.shape[1]).transpose()
#
#     for lst in gauss_:
#         for i, val in enumerate(lst):
#             lst[i] = max(val, 0)
#     print(gauss_.shape)
#     gauss_data = pd.DataFrame(gauss_)
#     gauss_data.to_csv("data/dataset/" + str_ + "_gauss" + str(m) + ".csv", index=False, header=False)
#
# matrices = []
# for i in range(1, k+1):
#     filename = f'C:/Users/Marina/degree_ML/data/dataset/' + str_ + '_gauss' + str(i) + '.csv'
#     matrix = pd.read_csv(filename, header=None)
#     matrices.append(matrix)
#
# result_matrix = pd.concat(matrices, axis=1)
#
# gauss_data = pd.DataFrame(result_matrix)
# gauss_data.to_csv("data/dataset/" + str_ + "_gauss_" + str(k) + ".csv", index=False, header=False)
#
# data_gauss = pd.read_csv("data/dataset/" + str_ + "_gauss_" + str(k) + ".csv", header=None, index_col=None).values
# index = [0, 1, 6, 7, 8, 13, 17, 24, 26, 29, 30, 34, 43, 47, 49, 54, 56, 62, 65, 70, 81, 82, 85, 93, 96, 100, 104, 108, 110, 111, 114, 126, 132, 138, 142, 143, 144, 150, 153, 156, 157, 158, 159, 164, 165, 166, 170, 175, 176, 183, 185, 187, 192, 197, 203, 204, 208, 209, 214, 220, 222, 227, 234, 237, 240, 248, 251, 252, 254, 255, 258, 264, 265, 267, 270, 272, 273, 286, 289, 298, 299, 305, 307, 309, 314, 318, 320, 323, 325, 327, 5, 10, 21, 22, 48, 60, 102, 141, 148, 155, 182, 190, 196, 201, 202, 216, 219, 246, 249, 253, 276, 279, 284, 294, 310, 313, 315, 316, 326, 9, 11, 16, 18, 19, 32, 33, 38, 41, 42, 44, 46, 50, 52, 68, 69, 71, 74, 76, 77, 78, 84, 90, 91, 94, 97, 98, 99, 103, 105, 112, 116, 119, 120, 121, 125, 129, 130, 134, 145, 151, 154, 160, 169, 172, 174, 177, 199, 205, 207, 215, 221, 225, 228, 229, 233, 236, 242, 250, 260, 268, 269, 278, 280, 283, 285, 288, 291, 297, 300, 304, 311, 312, 2, 3, 4, 12, 14, 15, 23, 27, 31, 35, 36, 37, 39, 45, 53, 55, 57, 58, 59, 61, 63, 64, 67, 73, 75, 79, 80, 86, 88, 92, 95, 101, 106, 107, 109, 115, 117, 118, 124, 128, 131, 133, 135, 136, 139, 140, 146, 147, 161, 162, 167, 168, 171, 173, 179, 180, 181, 184, 188, 189, 191, 193, 198, 200, 206, 210, 211, 213, 218, 223, 224, 226, 230, 231, 232, 238, 239, 241, 244, 247, 256, 259, 261, 262, 263, 271, 274, 275, 277, 287, 290, 292, 295, 296, 302, 303, 306, 308, 319, 322, 324, 328, 329, 51, 83, 178, 186, 194, 20, 25, 28, 40, 66, 72, 87, 89, 113, 122, 123, 127, 137, 149, 152, 163, 195, 212, 217, 235, 243, 245, 257, 266, 281, 282, 293, 301, 317, 321]
#
# matrix_permuted = data_gauss[:, index]
#
# gauss_true = pd.DataFrame(matrix_permuted)
# gauss_true.to_csv("data/dataset/" + str_ + "_gauss_" + str(k) + "_true.csv", index=False, header=False)
