# _*_ coding:utf-8 _*_

import matplotlib
import  matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import seaborn as sns
#%matplotlib inline
matplotlib.style.use('ggplot')

from sklearn.datasets import make_blobs
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def kmeans_missing(X, n_clusters, max_iter=10):
    """Perform K-Means clustering on data with missing values.

    Args:
      X: An [n_samples, n_features] array of data to cluster.
      n_clusters: Number of clusters to form.
      max_iter: Maximum number of EM iterations to perform.

    Returns:
      labels: An [n_samples] vector of integer labels.
      centroids: An [n_clusters, n_features] array of cluster centroids.
      X_hat: Copy of X with the missing values filled in.
    """
    # Initialize missing values to their column means
    # 非数值型、正无穷和负无穷都认为是缺失数据
    missing = ~np.isfinite(X)
    mu = np.nanmean(X, axis=0, keepdims=1)  # 忽略 NaN，计算某一列的平均值
    X_hat = np.where(missing, mu, X) # Return elements, either from x or y, depending on condition.
    X_gm = X_hat.copy()

    for i in xrange(max_iter):
        if i > 0:
            # initialize KMeans with the previous set of centroids. this is much
            # faster and makes it easier to check convergence (since labels
            # won't be permuted on every iteration), but might be more prone to
            # getting stuck in local minima.
            cls = KMeans(n_clusters, init=prev_centroids)
        else:
            # do multiple random initializations in parallel
            cls = KMeans(n_clusters, n_jobs=-1)

        # perform clustering on the filled-in data
        labels = cls.fit_predict(X_hat)
        print labels
        centroids = cls.cluster_centers_
        print centroids

        # fill in the missing values based on their cluster centroids
        X_hat[missing] = centroids[labels][missing]

        # when the labels have stopped changing then we have converged
        if i > 0 and np.all(labels == prev_labels):
            break

        prev_labels = labels
        prev_centroids = cls.cluster_centers_

    return labels, centroids, X_hat, X_gm


def make_fake_data(fraction_missing, n_clusters=5, n_samples=5000,
                   n_features=3, seed=0):
    # complete data
    gen = np.random.RandomState(seed)
    X, true_labels = make_blobs(n_samples, n_features, n_clusters,
                                random_state=gen)
    # with missing values
    missing = gen.rand(*X.shape) < fraction_missing
    Xm = np.where(missing, np.nan, X)
    return X, true_labels, Xm

X, true_labels, Xm = make_fake_data(fraction_missing=0.1, n_clusters=6, seed=10)
print X
labels, centroids, X_hat, X_gm = kmeans_missing(Xm, n_clusters=6, max_iter=40)
fig = plt.figure(figsize=(18,12))
ax = fig.add_subplot(221, projection='3d')
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=true_labels, cmap='gist_rainbow')
ax.set_title('Original data')
plt.show()

ax = fig.add_subplot(222, projection='3d')
ax.scatter(Xm[:, 0], Xm[:, 1], Xm[:, 2], c=true_labels, cmap='gist_rainbow')
ax.set_title('Missing data(30% missing values)')
plt.show()

ax = fig.add_subplot(223, projection='3d')
ax.scatter(X_gm[:, 0], X_gm[:, 1], X_gm[:, 2], c=true_labels, cmap='gist_rainbow')
ax.set_title('Imputed data using global mean values')
plt.show()

ax = fig.add_subplot(224, projection='3d')
ax.scatter(X_hat[:, 0], X_hat[:, 1], X_hat[:, 2], c=true_labels, cmap='gist_rainbow')
ax.set_title('Imputed data using cluster algorithm')
plt.show()