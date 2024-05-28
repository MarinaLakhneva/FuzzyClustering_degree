import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import multivariate_normal

k = 6

# str_ = "chords/dataset"
str_ = "classic/dataset"

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
index = [51, 83, 177, 185, 193, 5, 10, 21, 22, 48, 60, 102, 140, 147, 154, 181, 189, 195, 200, 201, 215, 218, 245, 248, 252, 275, 278, 283, 293, 309, 312, 314, 315, 325, 0, 1, 6, 7, 8, 13, 17, 24, 26, 29, 30, 34, 43, 47, 49, 54, 56, 62, 65, 70, 81, 82, 85, 93, 96, 100, 104, 108, 110, 111, 114, 125, 131, 137, 141, 142, 143, 149, 152, 155, 156, 157, 158, 163, 164, 165, 169, 174, 182, 184, 186, 191, 196, 202, 203, 207, 208, 213, 219, 221, 226, 233, 236, 239, 247, 250, 251, 253, 254, 257, 263, 264, 266, 269, 271, 272, 274, 285, 288, 297, 298, 304, 306, 308, 313, 317, 319, 322, 324, 326, 9, 11, 16, 18, 19, 32, 33, 38, 41, 42, 44, 46, 50, 52, 68, 69, 71, 74, 76, 77, 78, 84, 90, 91, 94, 97, 98, 99, 103, 105, 112, 119, 120, 121, 124, 128, 129, 133, 144, 150, 153, 159, 168, 171, 173, 176, 198, 204, 206, 214, 220, 224, 227, 228, 232, 235, 241, 249, 259, 267, 268, 277, 279, 282, 284, 287, 290, 296, 299, 303, 310, 311, 20, 25, 28, 40, 66, 72, 87, 89, 113, 122, 126, 136, 148, 151, 162, 175, 194, 211, 216, 234, 242, 244, 256, 265, 280, 281, 292, 300, 316, 320, 2, 3, 4, 12, 14, 15, 23, 27, 31, 35, 36, 37, 39, 45, 53, 55, 57, 58, 59, 61, 63, 64, 67, 73, 75, 79, 80, 86, 88, 92, 95, 101, 106, 107, 109, 115, 116, 117, 118, 123, 127, 130, 132, 134, 135, 138, 139, 145, 146, 160, 161, 166, 167, 170, 172, 178, 179, 180, 183, 187, 188, 190, 192, 197, 199, 205, 209, 210, 212, 217, 222, 223, 225, 229, 230, 231, 237, 238, 240, 243, 246, 255, 258, 260, 261, 262, 270, 273, 276, 286, 289, 291, 294, 295, 301, 302, 305, 307, 318, 321, 323, 327, 328]
matrix_permuted = data_gauss[:, index]

gauss_true = pd.DataFrame(matrix_permuted)
gauss_true.to_csv("data/dataset/" + str_ + "_gauss_" + str(k) + "_true.csv", index=False, header=False)
