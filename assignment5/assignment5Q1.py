from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.decomposition import PCA

# You can add the parameter data_home to wherever to where you want to download your data
dataset = pd.read_csv('CC GENERAL.csv')
x = dataset.iloc[:,[1,2,3,4]]
y = dataset.iloc[:,-1]

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
# Fit on training set only.
scaler.fit(x)

# Apply transform to both the training set and the test set.
x_scaler = scaler.transform(x)
pca = PCA(2)
x_pca = pca.fit_transform(x_scaler)
df2 = pd.DataFrame(data=x_pca)
finaldf = pd.concat([df2,dataset[['TENURE']]],axis=1)
print(finaldf)

from sklearn.cluster import KMeans
nclusters = 3 # this is the k in kmeans
km = KMeans(n_clusters=nclusters)
km.fit(x)

# predict the cluster for each data point
y_cluster_kmeans = km.predict(x)
from sklearn import metrics
score = metrics.silhouette_score(x, y_cluster_kmeans)
print(score)

