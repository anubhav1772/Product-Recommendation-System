from sklearn.neighbors import NearestNeighbors 
from Cluster_top_products import clust_prod 
from Cluster_top_products import clust0_top_prods_list, clust1_top_prods_list, clust2_top_prods_list, clust3_top_prods_list  
from preprocessing_data import mt

# function to find k similar users given the user_id and aisles purchased count matrix 'mat'
def findksimilarusers(user_id, metric, k):
    similarities=[]
    indices=[]
    aisle_bucket = [] # aisle candidate to be recommended to the user
    user_clust = clust_prod[clust_prod['user_id']==user_id]['cluster']
    df = clust_prod[clust_prod['cluster']==user_clust.tolist()[0]]
    # user_id_df = df.iloc[:,-2]
    mat = df.iloc[:,0:-1] # excluding cluster column
    mat = mat.set_index('user_id')
    mat.index.name = None
    model = NearestNeighbors(metric = metric, algorithm = 'brute') 
    model.fit(mat)
    print (model)

    distances, indices = model.kneighbors(mat.iloc[user_id, :].values.reshape(1, -1), n_neighbors = k+1)
    similarities = 1-distances.flatten()
    print ('{0} most similar users for User {1}:\n'.format(k,user_id))
    for i in range(0, len(indices.flatten())):
        if indices.flatten()[i] == user_id:
            aisle_bucket = aisle_bucket + list(set(mt[mt["user_id"]==indices.flatten()[i]]["aisle"]))
            continue;
        else:
            aisle_bucket = list(set(aisle_bucket).union(set(mt[mt["user_id"]==indices.flatten()[i]]["aisle"].values.tolist())))
            print ('{0}: User {1}, with similarity of {2}'.format(i, indices.flatten()[i], similarities.flatten()[i]))
            
    return user_clust, similarities, indices, aisle_bucket

user_id = 10
user_clust, similarities, indices, aisle_bucket = findksimilarusers(user_id , 'correlation', 4)

prime_aisle_candidate = aisle_bucket

if (user_clust == 0).tolist()[0] :
    prime_aisle_candidate = list(set(prime_aisle_candidate).intersection(set(clust0_top_prods_list)))
elif (user_clust == 1).tolist()[0] :
    prime_aisle_candidate = list(set(prime_aisle_candidate).intersection(set(clust1_top_prods_list)))
elif (user_clust == 2).tolist()[0] :
    prime_aisle_candidate = list(set(prime_aisle_candidate).intersection(set(clust2_top_prods_list)))
else :
    prime_aisle_candidate = list(set(prime_aisle_candidate).intersection(set(clust3_top_prods_list)))
    
    


    
     
    

#####################################################################################################################

#####################################################################################################################
'''
mat = np.asarray(cust_prod)
mat = pd.DataFrame(mat)
# cos_sim = 1- pairwise_distance(mat, metric = "cosine")
# x = pd.DataFrame(cos_sim)

#get pearson similarities for ratings matrix M
# pearson_sim = 1-pairwise_distances(mat, metric="correlation")
# x = pd.DataFrame(pearson_sim)

# cust_prod.iloc[971,:]
import numpy as np
from sklearn.metrics.pairwise import pairwise_distances
# findKSimilarUser(3, mat, 'correlation', 4 )

aisles = pd.read_csv('aisles/aisles.csv')
prior = pd.read_csv('order_products__prior/order_products__prior.csv')

# prior = prior[0:10000]
# print (prior.shape)
# print (prior.head(20))
train = pd.read_csv( 'order_products__train/order_products__train.csv')
# print (train.head(20))
order = pd.read_csv('orders/orders.csv')
# print (order.shape)
product = pd.read_csv('products/products.csv')
# print (product.head(10))
# print (order.shape)

merged_table = pd.merge(prior, product, on=['product_id', 'product_id'])
merged_table = pd.merge(merged_table, order, on=['order_id', 'order_id'])
merged_table = merged_table.sort_values('user_id')
merged_table = merged_table[merged_table["user_id"]<=10000]

# products = findOverAllProductList()
# dataframe for all purchases made by each user
# print(merged_table.isnull().any())
# print (merged_table[merged_table['product_name'].isnull()])
cust_prod = pd.crosstab(merged_table['user_id'], merged_table['aisle_id'])

# function to find all products in the used dataset
def findOverAllProductList():
    overall_product_bucket = []
    i = 1
    while(i<=10000):
        if len(overall_product_bucket)==0:
            overall_product_bucket = overall_product_bucket + list(set(merged_table[merged_table["user_id"]==i]["product_name"]))
        else:
            overall_product_bucket = list(set(overall_product_bucket).union(set(merged_table[merged_table["user_id"]==i]["product_name"].values.tolist())))
    return overall_product_bucket
    
user_bucket = merged_table[merged_table["user_id"]==503]["product_name"].values.tolist()

common_bucket = []
common_bucket = common_bucket + user_bucket
common_bucket = common_bucket + ["Banana"]
'''