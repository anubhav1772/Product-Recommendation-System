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
    
    
