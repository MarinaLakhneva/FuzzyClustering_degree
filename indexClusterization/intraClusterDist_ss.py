import pandas as pd
def intraClusterDistances_sumsSquares(k, path_FCM):
    m_Q3 = []
    for c in range(2, k+1):
        distance = pd.read_csv(path_FCM + str(c) + '/distance.csv', header=None, index_col=None).values
        n = distance.shape[1]

        dict = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
        }
        count = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
        }


        min = 1000
        number = 0
        for i in range(0, n):
            for j in range(0, c):
                if(distance[j][i] < min):
                    min = distance[j][i]
                    number = j+1
            dict[number] += min
            count[number] += 1
            min = 1000

        Q3 = 0
        for j in range(1, c+1):
            Q3 += dict[j]/count[j]
        print(dict)
        m_Q3.append(Q3)
    return m_Q3