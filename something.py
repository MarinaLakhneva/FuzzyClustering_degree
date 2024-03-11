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