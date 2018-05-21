import pandas as pd
aisles = pd.read_csv('aisles/aisles.csv')
prior = pd.read_csv('order_products__prior/order_products__prior.csv')
prior = prior[0:1000000]
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

mt = pd.merge(merged_table, aisles, on=['aisle_id', 'aisle_id'])
# mt = mt[0:20]
userid_col = mt.sort_values('user_id')[['user_id']].drop_duplicates()
userid_col = userid_col.reset_index(drop=True)
# dataframe for all purchases made by each user
cust_prod = pd.crosstab(mt['user_id'], mt['aisle']) 
cust_prod = cust_prod.reset_index(drop=True)
cust_prod = cust_prod.join(userid_col)

###############################################################################
# print (cust_prod.shape)
# print (mt.head(20))
# pvalue_count = mt['product_name'].value_counts()
# print (len(mt['product_name'].unique()))
# print (len(mt['aisle'].unique()))
# aisle_val_count = mt['aisle'].value_counts()


