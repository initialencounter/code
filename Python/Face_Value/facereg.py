# 环境python3.7
# pip install dlib==19.22.1,opencv-python==4.5.3.56,numpy==1.21.2,scikit-learn==0.22.1
import shutil
import warnings

warnings.filterwarnings('ignore')
import os
import time
import cv2
import math
import dlib
import numpy
import itertools
import numpy as np
from os import listdir
from sklearn import decomposition
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestRegressor


class face_value():
    def __init__(self):
        self.features_path = '/Users/mac/PycharmProjects/pythonProject1/Face_Value/data/features_ALL.txt'  # 特征路径
        self.ratings_path = '/Users/mac/PycharmProjects/pythonProject1/Face_Value/data/ratings.txt'  # 分数路径
        self.model_path = '/Users/mac/PycharmProjects/pythonProject1/Face_Value//model/face_rating.pkl'  # 模型路径
        self.pre_path = '/Users/mac/PycharmProjects/pythonProject1/Face_Value/model/shape_predictor_68_face_landmarks.dat'  # 模型路径
        self.landmark_path = '/Users/mac/PycharmProjects/pythonProject1/Face_Value/results/landmarks.txt'  # 关键点路径
        self.my_features_path = "/Users/mac/PycharmProjects/pythonProject1/Face_Value/results/my_features.txt"  # 特征点路径
        self.break_ = True

    # 训练
    def train(self):
        # 特征和对应的分数路径
        # features_path = '/Users/mac/PycharmProjects/pythonProject1/Face_Value/data/features_ALL.txt'
        # ratings_path = '/Users/mac/PycharmProjects/pythonProject1/Face_Value/data/ratings.txt'

        # 载入数据
        # 共500组数据
        # 其中前480组数据作为训练集，后20组数据作为测试集
        features = np.loadtxt(self.features_path, delimiter=',')
        features_train = features[0: -20]
        features_test = features[-20:]
        ratings = np.loadtxt(self.ratings_path, delimiter=',')
        ratings_train = ratings[0: -20]
        ratings_test = ratings[-20:]

        # 训练模型
        # 这里用PCA算法对特征进行了压缩和降维。
        # 降维之后特征变成了20维，也就是说特征一共有500行，每行是一个人的特征向量，每个特征向量有20个元素。
        # 用随机森林训练模型
        pca = decomposition.PCA(n_components=20)
        pca.fit(features_train)
        features_train = pca.transform(features_train)
        features_test = pca.transform(features_test)
        regr = RandomForestRegressor(n_estimators=50, max_depth=None, min_samples_split=10, random_state=0)
        regr = regr.fit(features_train, ratings_train)
        joblib.dump(regr, self.model_path, compress=1)

        # 训练完之后提示训练结束
        print('Generate Model Successfully!')

    # 人脸关键点提取脚本
    def get_land(self, img):
        # 模型路径
        PREDICTOR_PATH = self.pre_path
        # 使用dlib自带的frontal_face_detector作为人脸提取器
        detector = dlib.get_frontal_face_detector()
        # 使用官方提供的模型构建特征提取器
        predictor = dlib.shape_predictor(PREDICTOR_PATH)
        face_img = img
        # face_img = cv2.cvtColor(face_img,cv2.COLOR_BGR2GRAY)
        # 使用detector进行人脸检测，rects为返回的结果
        rects = detector(face_img, 1)
        # 如果检测到人脸
        if len(rects) == 1:
            with open(self.landmark_path, 'w') as f:
                f.truncate()
                for faces in range(len(rects)):
                    # 使用predictor进行人脸关键点识别
                    landmarks = numpy.matrix([[p.x, p.y] for p in predictor(face_img, rects[faces]).parts()])
                    face_img = face_img.copy()
                    # 使用enumerate函数遍历序列中的元素以及它们的下标
                    for idx, point in enumerate(landmarks):
                        pos = (point[0, 0], point[0, 1])
                        f.write(str(point[0, 0]))
                        f.write(',')
                        f.write(str(point[0, 1]))
                        f.write(',')
                    f.write('\n')
                f.close()
                # 成功后提示
            # print('Get landmarks successfully')
        else:
            print('No face or faces >1 !')
            self.break_ = False
        return len(rects)
    # 特征生成脚本
    def get_fetre(self):
        if self.break_:
            # 具体原理请参见参考论文

            def facialRatio(points):
                x1 = points[0]
                y1 = points[1]
                x2 = points[2]
                y2 = points[3]
                x3 = points[4]
                y3 = points[5]
                x4 = points[6]
                y4 = points[7]
                dist1 = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                dist2 = math.sqrt((x3 - x4) ** 2 + (y3 - y4) ** 2)
                ratio = dist1 / dist2
                return ratio

            def generateFeatures(pointIndices1, pointIndices2, pointIndices3, pointIndices4, allLandmarkCoordinates):
                size = allLandmarkCoordinates.shape
                if len(size) > 1:
                    allFeatures = numpy.zeros((size[0], len(pointIndices1)))
                    for x in range(0, size[0]):
                        landmarkCoordinates = allLandmarkCoordinates[x, :]
                        ratios = []
                        for i in range(0, len(pointIndices1)):
                            x1 = landmarkCoordinates[2 * (pointIndices1[i] - 1)]
                            y1 = landmarkCoordinates[2 * pointIndices1[i] - 1]
                            x2 = landmarkCoordinates[2 * (pointIndices2[i] - 1)]
                            y2 = landmarkCoordinates[2 * pointIndices2[i] - 1]
                            x3 = landmarkCoordinates[2 * (pointIndices3[i] - 1)]
                            y3 = landmarkCoordinates[2 * pointIndices3[i] - 1]
                            x4 = landmarkCoordinates[2 * (pointIndices4[i] - 1)]
                            y4 = landmarkCoordinates[2 * pointIndices4[i] - 1]
                            points = [x1, y1, x2, y2, x3, y3, x4, y4]
                            ratios.append(facialRatio(points))
                        allFeatures[x, :] = numpy.asarray(ratios)
                else:
                    allFeatures = numpy.zeros((1, len(pointIndices1)))
                    landmarkCoordinates = allLandmarkCoordinates
                    ratios = []
                    for i in range(0, len(pointIndices1)):
                        x1 = landmarkCoordinates[2 * (pointIndices1[i] - 1)]
                        y1 = landmarkCoordinates[2 * pointIndices1[i] - 1]
                        x2 = landmarkCoordinates[2 * (pointIndices2[i] - 1)]
                        y2 = landmarkCoordinates[2 * pointIndices2[i] - 1]
                        x3 = landmarkCoordinates[2 * (pointIndices3[i] - 1)]
                        y3 = landmarkCoordinates[2 * pointIndices3[i] - 1]
                        x4 = landmarkCoordinates[2 * (pointIndices4[i] - 1)]
                        y4 = landmarkCoordinates[2 * pointIndices4[i] - 1]
                        points = [x1, y1, x2, y2, x3, y3, x4, y4]
                        ratios.append(facialRatio(points))
                    allFeatures[0, :] = numpy.asarray(ratios)
                return allFeatures

            def generateAllFeatures(allLandmarkCoordinates):
                a = [18, 22, 23, 27, 37, 40, 43, 46, 28, 32, 34, 36, 5, 9, 13, 49, 55, 52, 58]
                combinations = itertools.combinations(a, 4)
                i = 0
                pointIndices1 = []
                pointIndices2 = []
                pointIndices3 = []
                pointIndices4 = []
                for combination in combinations:
                    pointIndices1.append(combination[0])
                    pointIndices2.append(combination[1])
                    pointIndices3.append(combination[2])
                    pointIndices4.append(combination[3])
                    i = i + 1
                    pointIndices1.append(combination[0])
                    pointIndices2.append(combination[2])
                    pointIndices3.append(combination[1])
                    pointIndices4.append(combination[3])
                    i = i + 1
                    pointIndices1.append(combination[0])
                    pointIndices2.append(combination[3])
                    pointIndices3.append(combination[1])
                    pointIndices4.append(combination[2])
                    i = i + 1
                return generateFeatures(pointIndices1, pointIndices2, pointIndices3, pointIndices4,
                                        allLandmarkCoordinates)

            landmarks = numpy.loadtxt(self.landmark_path, delimiter=',', usecols=range(136))
            featuresALL = generateAllFeatures(landmarks)
            numpy.savetxt(self.my_features_path, featuresALL, delimiter=',', fmt='%.04f')
            # print("Generate Feature Successfully!")
        else:
            pass

    # 颜值预测脚本
    def get_pre(self):
        if self.break_:
            pre_model = joblib.load(self.model_path)
            features = np.loadtxt(self.features_path, delimiter=',')
            my_features = np.loadtxt(self.my_features_path, delimiter=',')
            pca = decomposition.PCA(n_components=20)
            pca.fit(features)
            predictions = []
            if len(my_features.shape) > 1:
                pass
                # for i in range(len(my_features)):
                #     feature = my_features[i, :]
                #     feature_transfer = pca.transform(feature.reshape(1, -1))
                #     predictions.append(pre_model.predict(feature_transfer))
                # print('照片中的人颜值得分依次为(满分为5分)：')
                # k = 1
                # for pre in predictions:
                #     print('第%d个人：' % k, end='')
                #     print(str(pre) + '分')
                #     k += 1
                # return predictions
            else:
                feature = my_features
                feature_transfer = pca.transform(feature.reshape(1, -1))
                pre = pre_model.predict(feature_transfer)
                print('颜值:{}'.format(pre))
                return pre
        else:
            pre = 0
            return pre

def move_files(srcfile,dstpath):
    if not os.path.isfile(srcfile):
        with open("/Users/mac/PycharmProjects/pythonProject1/Face_Value/results/note.txt",'a') as f:
            f.write('{}\n'.format(str(srcfile)))
    else:
        fpath,fname=os.path.split(srcfile)
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)
        shutil.move(srcfile,dstpath+fname)


if __name__ == '__main__':
    dirlist = listdir('/Users/mac/Pictures/img/Telegram')
    face_dict = {}
    num = 1
    nu = 1
    for i in dirlist[365:366]:
        try:
            start = time.clock()
            obj = face_value()
            # obj.train()
            img = cv2.imread('/Users/mac/Pictures/img/Telegram/' + i)
            faces = obj.get_land(img)
            obj.get_fetre()
            face_num = obj.get_pre()
            if obj.break_:
                # print('pass:{}'.format(nu))
                # nu+=1
                pass
                face_dict[float(face_num)] = ('/Users/mac/Pictures/img/Telegram/' + i)
                end = time.clock()
                print('第{}张图片:{}\n检测到{}张人脸\n用时{}s\n'.format(num,i,faces,int(end - start)))
                num+=1
            else:
                print('i%s'('错误！'))
                # move_files('/Users/mac/Pictures/img/Telegram/' + i,'/Users/mac/Pictures/img/delete/')
                # num+=1
        except:
            print('666666')

    print(face_dict)
