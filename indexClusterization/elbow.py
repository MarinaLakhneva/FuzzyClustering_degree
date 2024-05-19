import pandas as pd

def elbow(k, str_):
    eb = []
    for c in range(2, k+1):
        dist = pd.read_csv("FCM/" + str_ + "/clusters_" + str(c) + "/distance.csv", header=None, index_col=None).values
        n = len(dist[0])

        dict = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0,
            10: 0,
            11: 0,
            12: 0,
            13: 0,
            14: 0
        }


        for j in range(0, n):
            min = 1000
            number = 0
            for i in range(0, c):
                square = dist[i][j] * dist[i][j]
                if(min > square):
                    min = square
                    square = 0
                    number = i
            dict[number+1] += min

        m_elbow = 0
        for r in range(1, c+1):
            m_elbow += dict[r]
        eb.append(m_elbow)
    print(eb)
    return eb