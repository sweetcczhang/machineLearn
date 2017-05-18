# _*_ coding:utf-8 _*_

import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
from sklearn import datasets


def filematrix(filename):
    fr = open(filename, 'r')
    array0lines = fr.readlines()
    numberOfLines = len(array0lines)
    returnMat = np.zeros((numberOfLines,3))
    classLabelVector = [] #开辟容器
    index = 0
    for line in array0lines:
        # 清洗数据
        line =line.strip()
        listFromLine = line.split('\t')
        # 将评价转化为数字
        if listFromLine[3] =='largeDoses':
            listFromLine[3] = 3
        elif listFromLine == 'smallDoses':
            listFromLine[3] = 2
        else:
            listFromLine[3] = 1
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[3]))
        index += 1
    return returnMat, classLabelVector


def distEclud(vecA, vecB):
    return np.sqrt(sum(np.power(vecA-vecB,2)))


# 给定数据集构建一个包含k个随机质的集合
def randCent(dataSet,k):
    n = np.shape(dataSet)[1] # 计算列数
    centroids = np.mat(np.zeros(k,n))
    for j in range(n):
        minJ = min(dataSet[:,j])
        rangeJ = float(max(dataSet[:,j])-minJ)
        centroids[:,j] = minJ + rangeJ*np.random.rand(k,1)
    return centroids

def KMeans(dataSet, k, disMeas = distEclud, creatCent = randCent):
    m = np.shape(dataSet)[0]
    clusterAssment = np.mat(np.zeros((m,2))) # 建立簇分配结果矩阵。第一列存索引，第二列存误差
    centroids = creatCent(dataSet,k) # 聚类点
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = np.inf #无穷大
            minIndex = -1
            for j in range(k):
                distJI = disMeas(centroids[j, :], dataSet[i, :]) # 计算个点与新聚类中心的距离
                if distJI < minDist: # 存储最小值，存储最小值所在位置
                    minDist = distJI
                    minIndex = j
            if clusterAssment[i,0] != minIndex:
                clusterChanged = True
            clusterAssment[i, :] = minIndex, minDist**2
        print centroids
        for cent in range(k):
            # nonzeros(a=k) 返回数组a中值不为k的元素的下标
            ptsInClust = dataSet[np.nonzero(clusterAssment[:, 0].A == cent)[0]]
            centroids[cent, :] = np.mean(ptsInClust,axis=0)
    return centroids, clusterAssment