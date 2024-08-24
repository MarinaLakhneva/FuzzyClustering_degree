# проверка каждого с каждым
# difference = 0.1
# ambiguity = np.ones((number_of_clusters, number_of_elements))
# for i in range(0, number_of_elements):
#     membership_comparisons = 0
#     for j in range(0, number_of_clusters):
#         for a in range(0, number_of_clusters):
#             membership_comparisons = result[j][i]
#             if(result[a][i] != membership_comparisons):
#                 if(np.abs(membership_comparisons - result[a][i]) < difference):
#                     ambiguity[j][i] += 1
#
#
# frame_ambiguity = pd.DataFrame(ambiguity)
# frame_ambiguity.to_csv('ambiguityClasters.csv', indexClusterization=False, header=False)

# import numpy as np
# matrix = np.array([[1, 2, 3],
#                    [4, 5, 6],
#                    [7, 8, 9]])
#
# # Массив индексов для перестановки столбцов
# new_order = [2, 0, 1]
#
# # Переставляем столбцы в соответствии с новым порядком
# matrix_permuted = matrix[:, new_order]
#
# print(matrix_permuted)


import numpy as np
x = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

# chord
y = np.array([0.02266734770615795, 0.016403557358961363, 0.012985183556979587,
              0.010784168942633796, 0.009253053614906583, 0.007486965641433933,
              0.006724086239492887, 0.006202611668789534, 0.0056421736024886045,
              0.005378068884622969, 0.004870865619948707, 0.004740180616817705,
              0.004582415527847291])
# classic
# y = np.array([5185.511437105444, 3007.2929029218503, 2282.72724221728,
#      1928.8951397672777, 1213.6515089634072, 1100.174554705399,
#      1018.5766061948871, 890.4267461183011, 845.5958595486169,
#      808.5256010018331, 763.8849489963535, 733.0546061935781,
#      708.1107901325968])

def derivative(x_data, y_data):
    N = len(x_data)
    delta_x = [x_data[i+1] - x_data[i] for i in range(N - 1)]
    x_prim = [(x_data[i+1] + x_data[i]) / 2. for i in range(N - 1)]
    y_prim = [(y_data[i+1] - y_data[i]) / delta_x[i] for i in range(N - 1)]
    return x_prim, y_prim


x_f, y_f = derivative(*derivative(x, y))


import matplotlib.pyplot as plt
fig, ax1 = plt.subplots()
ax1.plot(x, y, color="red", label="wcss", marker="D")
ax1.tick_params(axis='y', labelcolor="red")
plt.legend(loc='center right')
plt.grid(True)
plt.axvline(x=6, color="black", linestyle='dashed')
plt.title("Метод локтя", fontsize=16, fontweight='bold')
ax2 = ax1.twinx()
polyline = np.linspace(1, 14, 50)
ax2.plot(x_f, y_f, color="blue", label="кривизна", linestyle='dashed', marker="o")
ax2.tick_params(axis='y', labelcolor="blue")
plt.title("Метод локтя", fontsize=16, fontweight='bold')
plt.grid(True)
plt.legend()
plt.show()