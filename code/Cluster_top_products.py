"""
Created on Fri Mar  2 12:46:20 2018

@author: Anubhav Singh
"""
from preprocessing_data import cust_prod
from KMeans import c_preds
# import matplotlib.pyplot as plt

  
clust_prod = cust_prod.copy()
clust_prod['cluster'] = c_preds
# print (clust_prod.head(5))
# print (clust_prod.shape)
# c1_count = len(clust_prod[clust_prod['cluster']==0])
# print c1_count

global aisle_bucket
# [0:-2] for not considering 'user_id' and 'clusters' , i.e. last two columns of aisle_bucket 
aisle_bucket = list(clust_prod.columns)[0:-2] 

# function that return top aisles list of each cluster passed as parameter
def topProducts(top_prods_series, ci):
    cluster_top_prods = []
    for i in range(10):
        for j in range(len(aisle_bucket)):
            if top_prods_series[i] == ci[aisle_bucket[j]].mean() :
                cluster_top_prods.append(aisle_bucket[j])
    return cluster_top_prods

c0 = clust_prod[clust_prod['cluster']==0].drop(['cluster','user_id'], axis=1) 
c1 = clust_prod[clust_prod['cluster']==1].drop(['cluster','user_id'], axis=1)
c2 = clust_prod[clust_prod['cluster']==2].drop(['cluster','user_id'], axis=1)
c3 = clust_prod[clust_prod['cluster']==3].drop(['cluster','user_id'], axis=1)

# mean values of top ten aisles of each cluster
clust0_top_prods = c0.mean().sort_values(ascending=False)[0:10]
clust1_top_prods = c1.mean().sort_values(ascending=False)[0:10]
clust2_top_prods = c2.mean().sort_values(ascending=False)[0:10]
clust3_top_prods = c3.mean().sort_values(ascending=False)[0:10]

# top ten aisles of each cluster
clust0_top_prods_list = topProducts(clust0_top_prods, c0)
clust1_top_prods_list = topProducts(clust1_top_prods, c1)
clust2_top_prods_list = topProducts(clust2_top_prods, c2)
clust3_top_prods_list = topProducts(clust3_top_prods, c3)

########################################################################
'''
f, arr = plt.subplots(2, 2, sharex=True, figsize=(15, 15))
arr[0,0].bar(range(len(clust_prod.drop('cluster', axis=1).columns)), c0, color='r')
arr[0,1].bar(range(len(clust_prod.drop('cluster', axis=1).columns)), c1, color='b')
arr[1,0].bar(range(len(clust_prod.drop('cluster', axis=1).columns)), c2, color='g')
arr[1,1].bar(range(len(clust_prod.drop('cluster', axis=1).columns)), c3, color='y')
plt.show()
print (c0.sort_values(ascending=False)[0:10])
print ("")
print (c1.sort_values(ascending=False)[0:10])
print ("")
print (c2.sort_values(ascending=False)[0:10])
print ("")
print (c3.sort_values(ascending=False)[0:10])
print ("")
import pandas as pd
cluster_means = [[c0['fresh fruits'],
                  c0['fresh vegetables'],
                  c0['packaged vegetables fruits'], 
                  c0['yogurt'], 
                  c0['packaged cheese'], 
                  c0['milk'],
                  c0['water seltzer sparkling water'],
                  c0['chips pretzels']],
                 [c1['fresh fruits'],
                  c1['fresh vegetables'],
                  c1['packaged vegetables fruits'], 
                  c1['yogurt'], 
                  c1['packaged cheese'], 
                  c1['milk'],
                  c1['water seltzer sparkling water'],
                  c1['chips pretzels']],
                 [c2['fresh fruits'],
                  c2['fresh vegetables'],
                  c2['packaged vegetables fruits'], 
                  c2['yogurt'], 
                  c2['packaged cheese'], 
                  c2['milk'],
                  c2['water seltzer sparkling water'],
                  c2['chips pretzels']],
                 [c3['fresh fruits'],
                  c3['fresh vegetables'],
                  c3['packaged vegetables fruits'], 
                  c3['yogurt'], 
                  c3['packaged cheese'], 
                  c3['milk'],
                  c3['water seltzer sparkling water'],
                  c3['chips pretzels']]]
cluster_means = pd.DataFrame(cluster_means, columns = ['fresh fruits','fresh vegetables','packaged vegetables fruits','yogurt','packaged cheese','milk','water seltzer sparkling water','chips pretzels'])
print (cluster_means)'''