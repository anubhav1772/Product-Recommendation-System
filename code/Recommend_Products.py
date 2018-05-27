"""
Created on Mon May 21 21:17:01 2018
@author: anubh

"""

from UserBasedCF import prime_aisle_candidate, sim_users
from preprocessing_data import product, aisles, mt
import pandas as pd

print('\n\nPrime aisles category from which products will be recommended to {0}:\n{1}'.format(sim_users[0],prime_aisle_candidate))

prod_aisle_merged_table = pd.merge(product, aisles, on=['aisle_id', 'aisle_id'])
rec_prod = []
K = len(sim_users)
for i in range(0,len(prime_aisle_candidate)):
    for j in range(1,K):
         prod_list = mt[(mt['user_id']==sim_users[j]) & (mt['aisle']==prime_aisle_candidate[i]) & (mt['reordered']==1)]['product_name'].tolist() 
         if prod_list != [] :
             rec_prod = list(set(rec_prod).union(set(prod_list)))

print('\n\nProducts that will be recommended to user {0}:\n{1}'.format(sim_users[0],rec_prod))


            

    
    