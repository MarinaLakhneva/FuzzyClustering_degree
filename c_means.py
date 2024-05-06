import numpy as np
import skfuzzy as fuzz
import pandas as pd

dataset = pd.read_csv('data/dataset.csv', header=None, index_col=None).values

cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(
    data=dataset,
    c=3,
    m=2,
    error=0.001,
    init=None
)
print(u)
#-----------------------------------------------------------------------------------------------------------------------
# from sklearn.cluster import KMeans
#
# kmeans = KMeans(n_clusters=3, init='random', n_init=1, tol=0.005)
# kmeans.fit(dataset)
# print(kmeans.cluster_centers_)

#-----------------------------------------------------------------------------------------------------------------------
import numpy as np

def fuzzy_c_means(data, c, m, error, maxiter):
    # Initialize the cluster centers randomly
    cntr = np.random.rand(c, data.shape[1])

    # Iterate until convergence or maximum iterations reached
    for _ in range(maxiter):
        # Calculate the membership matrix
        u = calculate_membership(data, cntr, m)

        # Update the cluster centers
        cntr_new = update_cluster_centers(data, u, m)

        # Check for convergence
        if np.linalg.norm(cntr_new - cntr) < error:
            break

        cntr = cntr_new

    return cntr

def calculate_membership(data, cntr, m):
    # Calculate the distances between data points and cluster centers
    distances = np.linalg.norm(data[:, np.newaxis] - cntr, axis=2)

    # Calculate the membership matrix
    u = 1 / distances**(2 / (m - 1))
    u /= np.sum(u, axis=1)[:, np.newaxis]

    return u

def update_cluster_centers(data, u, m):
    # Update the cluster centers
    cntr = np.dot(u**m, data) / np.sum(u**m, axis=0)[:, np.newaxis]

    return cntr

# Generate some test data
x = np.random.rand(100)
y = np.random.rand(100)
data = np.vstack((x, y)).T

# Create the fuzzy c means algorithm
cntr = fuzzy_c_means(data, c=2, m=2, error=0.005, maxiter=1000)

# Print the cluster centers
print(cntr)