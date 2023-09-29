def get_pre():
	from sklearn.externals import joblib
	import numpy as np
	from sklearn import decomposition
	t1 = time.clock()
	pre_model = joblib.load('./model/face_rating.pkl')
	t2 = time.clock()
	print('\npre_model:\n {}'.format(t2-t1))
	t1 = time.clock()
	features = np.loadtxt('./data/features_ALL.txt', delimiter=',')
	t2 = time.clock()
	print('\nfeatures:\n {}'.format(t2-t1))
	t1 = time.clock()
	my_features = np.loadtxt('./results/my_features.txt', delimiter=',')
	t2 = time.clock()
	print('\nmy_features:\n {}'.format(t2-t1))
	t1 = time.clock()
	pca = decomposition.PCA(n_components=20)
	t2 = time.clock()
	print('\npca:\n {}'.format(t2-t1))
	t1 = time.clock()
	pca.fit(features)
	t2 = time.clock()
	print('\npca.fit:\n {}'.format(t2-t1))
	if len(my_features.shape) > 1:
		pass
	else:
		feature_transfer = pca.transform(my_features.reshape(1, -1))
		print('照片中的人颜值得分为(满分为5分)：')
		print((pre_model.predict(feature_transfer)))
import warnings
warnings.filterwarnings('ignore')
import time

get_pre()
start = time.process_time()
print(start)