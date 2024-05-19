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