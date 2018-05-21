# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 22:43:28 2018
@author: Anubhav Singh

"""
from pca_module import pca_
import matplotlib.pyplot as plt
import pandas as pd


tocluster1 = pd.DataFrame(pca_[[2, 1]])
# print (tocluster.shape)
# print (tocluster.head())
fig = plt.figure(figsize=(12, 12))
plt.plot(tocluster1[2], tocluster1[1], 'o', markersize=3, color='blue', alpha=1, label='class21')
plt.xlabel('x_values')
plt.ylabel('y_values')
plt.legend()
plt.show()


tocluster2 = pd.DataFrame(pca_[[3, 1]])
fig = plt.figure(figsize=(12, 12))
plt.plot(tocluster2[3], tocluster2[1], 'o', markersize=3, color='blue', alpha=1, label='class31')
plt.xlabel('x_values')
plt.ylabel('y_values')
plt.legend()
plt.show()


tocluster3 = pd.DataFrame(pca_[[4, 1]])
fig = plt.figure(figsize=(12, 12))
plt.plot(tocluster3[4], tocluster3[1], 'o', markersize=3, color='blue', alpha=1, label='class41')
plt.xlabel('x_values')
plt.ylabel('y_values')
plt.legend()
plt.show()

tocluster4 = pd.DataFrame(pca_[[3, 2]])
fig = plt.figure(figsize=(12, 12))
plt.plot(tocluster4[3], tocluster4[2], 'o', markersize=3, color='red', alpha=1, label='class32')
plt.xlabel('x_values')
plt.ylabel('y_values')
plt.legend()
plt.show()

tocluster5 = pd.DataFrame(pca_[[4, 2]])
fig = plt.figure(figsize=(12, 12))
plt.plot(tocluster5[4], tocluster5[2], 'o', markersize=3, color='red', alpha=1, label='class42')
plt.xlabel('x_values')
plt.ylabel('y_values')
plt.legend()
plt.show()

tocluster6 = pd.DataFrame(pca_[[3, 4]])
fig = plt.figure(figsize=(12, 12))
plt.plot(tocluster6[4], tocluster6[3], 'o', markersize=3, color='green', alpha=1, label='class43')
plt.xlabel('x_values')
plt.ylabel('y_values')
plt.legend()
plt.show()






