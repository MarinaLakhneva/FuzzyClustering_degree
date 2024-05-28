import numpy as np
import pandas as pd

k = 6

# str_ = "chords/dataset"
str_ = "classic/dataset"

path_FCM = "C:/Users/Marina/degree_ML/FCM/" + str_ + "/clusters_"
path = "C:/Users/Marina/degree_ML/data/dataset/" + str_

result = pd.read_csv(path_FCM + str(k) + '/FCM.csv', header=None, index_col=None).values
dataset = pd.read_csv(path + '.csv', header=None, index_col=None).values
n = dataset.shape[1]

count = np.zeros(k)
x = np.zeros(n)

membership_1 = []
membership_1_number = []
membership_2 = []
membership_2_number = []
membership_3 = []
membership_3_number = []
membership_4 = []
membership_4_number = []
membership_5 = []
membership_5_number = []
membership_6 = []
membership_6_number = []
# membership_7 = []
# membership_7_number = []
# membership_8 = []
# membership_8_number = []


cluster = -1
for i in range(0, n):
    max = 0.0
    membership = 0
    for j in range(0, k):
        x[i] = i + 1
        if (max < result[j][i]):
            max = result[j][i]
            membership = max + j
            cluster = j
    if cluster == 0:
        count[cluster] += 1
        membership_1.append(max)
        membership_1_number.append(i)
    elif cluster == 1:
        count[cluster] += 1
        membership_2.append(max)
        membership_2_number.append(i)
    elif cluster == 2:
        count[cluster] += 1
        membership_3.append(max)
        membership_3_number.append(i)
    elif cluster == 3:
        count[cluster] += 1
        membership_4.append(max)
        membership_4_number.append(i)
    elif cluster == 4:
        count[cluster] += 1
        membership_5.append(max)
        membership_5_number.append(i)
    elif cluster == 5:
        count[cluster] += 1
        membership_6.append(max)
        membership_6_number.append(i)
    # elif cluster == 6:
    #     count[cluster] += 1
    #     membership_7.append(max)
    #     membership_7_number.append(i)
    # elif cluster == 7:
    #     count[cluster] += 1
    #     membership_8.append(max)
    #     membership_8_number.append(i)


# print("k=1", membership_1_number)
# print("k=2", membership_2_number)
# print("k=3", membership_3_number)
# print("k=4", membership_4_number)
# print("k=5", membership_5_number)
# print("k=6", membership_6_number)


# m = np.vstack([dataset[:, idx] for idx in membership_6_number]).transpose()
# data = pd.DataFrame(m)
# data.to_csv("data/dataset/" + str_ + "_6.csv", index=False, header=False)

all_memberships = []
all_memberships = np.concatenate([membership_1_number, membership_2_number, membership_3_number,
                                  membership_4_number, membership_5_number, membership_6_number])
print(*all_memberships, sep=', ')