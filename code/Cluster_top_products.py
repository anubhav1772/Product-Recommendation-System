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
