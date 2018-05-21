
"""
Created on Mon Feb 26 23:40:08 2018
@author: Anubhav Singh
"""
from visualize import tocluster3
from sklearn.cluster import KMeans
from preprocessing_data import cust_prod
import pandas as pd

model = KMeans(n_clusters=4,random_state=42)
model.fit(tocluster3)
centers = model.cluster_centers_
c_preds = model.predict(tocluster3)
# print(centers)
# print (c_preds)
clusters = pd.DataFrame({'clusters':list(c_preds)})
cust_prod = cust_prod.join(clusters)

###################################################################
'''
import numpy as np
import matplotlib.pyplot as plt

f1 = tocluster3[4]
f2 = tocluster3[1]
X = np.array(list(zip(f1, f2)))
# print (X)
# plt.scatter(tocluster3[4], tocluster3[1], c='black', s=7)
# plt.show()

# Euclidean Distance Caculator
def dist(a, b, ax=1):
    return np.linalg.norm(a - b, axis=ax)

# Number of clusters
k = 4
# X coordinates of random centroids
C_x = np.random.randint(0, np.max(X), size=k)
# Y coordinates of random centroids
C_y = np.random.randint(0, np.max(X), size=k)
C = np.array(list(zip(C_x, C_y)), dtype=np.float32)
# print(C)

# Plotting along with the Centroids
# plt.scatter(f1, f2, c='#050505', s=7)
# plt.scatter(C_x, C_y, marker='*', s=200, c='g')
'''
