# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 22:40:38 2018

@author: Anubhav Singh

"""
from visualize import tocluster3
from KMeans import c_preds, centers
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8, 8))
colors = ['orange','blue','purple','green']
colored = [colors[k] for k in c_preds]
plt.scatter(tocluster3[4], tocluster3[1], color=colored)
# print (list(enumerate(centers)))
for x, y in enumerate(centers):
    plt.plot(y[0], y[1], 'o', markersize=8, color='red', alpha=0.9, label=str(x))   
    
plt.xlabel('x_values')
plt.ylabel('y_values')
plt.legend()
plt.show()

