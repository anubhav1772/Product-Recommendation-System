# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 19:32:22 2018

@author: anubh
"""
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def get_unique_count(x):
    return len(np.unique(x))

orders_df = pd.read_csv('orders/orders.csv')
# print (orders_df.shape)
'''a column in orders.csv file called eval_set tells us as 
   to which of the three datasets (prior, train or test) the given row goes to'''
row_count = orders_df.eval_set.value_counts()
print (row_count)
plt.figure(figsize=(13,9))
# sns.set_style("whitegrid")
sns.barplot(row_count.index, row_count.values, alpha=0.8)
plt.ylabel('Number of Occurrences', fontsize=12)
plt.xlabel('Eval set type', fontsize=12)
plt.title('Count of rows in each dataset', fontsize=15)
plt.xticks(rotation='vertical')
plt.show()

# count of orders placed by unique users
# prior = train + test
print (orders_df.groupby("eval_set")["user_id"].aggregate(get_unique_count))