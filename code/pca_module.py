from preprocessing_data import cust_prod
import pandas as pd
from sklearn.decomposition import PCA


pca = PCA(n_components=6)
pca.fit(cust_prod.iloc[:,0:-1])
pca_new = pca.transform(cust_prod.iloc[:,0:-1])
pca_ = pd.DataFrame(pca_new)
# print (pca_.head())

'''
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

X_std = StandardScaler().fit_transform(cust_prod)
mean_vec = np.mean(X_std, axis=0)
cov_mat = (X_std - mean_vec).T.dot((X_std - mean_vec)) / (X_std.shape[0]-1)

# print('Covariance matrix \n%s' %cov_mat)

cov_mat = np.cov(X_std.T)
eig_vals, eig_vecs = np.linalg.eig(cov_mat)

# print('Eigenvectors \n%s' %eig_vecs)
# print('\nEigenvalues \n%s' %eig_vals)

for ev in eig_vecs:
    np.testing.assert_array_almost_equal(1.0, np.linalg.norm(ev))
    
# Make a list of (eigenvalue, eigenvector) tuples
eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]

# Sort the (eigenvalue, eigenvector) tuples from high to low
eig_pairs.sort(key=lambda x: x[0], reverse=True)

# Visually confirm that the list is correctly sorted by decreasing eigenvalues
# print('Eigenvalues in descending order:')
# for i in eig_pairs:
#    print(i[0])

tot = sum(eig_vals)
var_exp = [(i / tot)*100 for i in sorted(eig_vals, reverse=True)]
cum_var_exp = np.cumsum(var_exp)
with plt.style.context('seaborn-whitegrid'):
    plt.figure(figsize=(6, 8))

    plt.bar(range(134), var_exp, alpha=1, align='center',
            label='individual explained variance')
    plt.step(range(134), cum_var_exp, where='mid',
             label='cumulative explained variance')
    plt.ylabel('Explained variance ratio')
    plt.xlabel('Principal components')
    plt.legend(loc='best')
    plt.tight_layout()'''
