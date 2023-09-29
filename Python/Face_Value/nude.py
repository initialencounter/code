import numpy as np
from sklearn import decomposition
features = np.loadtxt('./data/features_ALL.txt', delimiter=',')
# features = np.loadtxt('./data/features_ALL.txt', delimiter=',')
#features = preprocessing.scale(features)
features_train = features[0:-50]
features_test = features[-50:]

pca = decomposition.PCA(n_components=20)
pca.fit(features_train)
features_train = pca.transform(features_train)
features_test = pca.transform(features_test)

ratings = np.loadtxt('./data/ratings.txt', delimiter=',')
#ratings = preprocessing.scale(ratings)
ratings_train = ratings[0:-50]
ratings_test = ratings[-50:]
