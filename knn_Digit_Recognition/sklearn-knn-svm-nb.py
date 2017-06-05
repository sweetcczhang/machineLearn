# _*_ coding:utf-8 _*_

from numpy import *
import csv


def toInt(data):
    data = mat(data)
    m, n = shape(data)
    newData = zeros((m, n))
    for i in range(m):
        for j in range(n):
            newData[i, j] = int(data[i, j])

    return newData

def normalizing(data):
    m, n = shape(data)
    for i in range(m):
        for j in range(n):
            if data[i, j] !=0:
                data[i, j] = 1

    return data

def loadTestData():
    l=[]
    with open('test.csv') as file:
         lines=csv.reader(file)
         for line in lines:
             l.append(line)#28001*784
    l.remove(l[0])
    data=array(l)
    return normalizing(toInt(data))  #  data 28000*784
    #return testData


def loadTrainData():
    l=[]
    with open('train.csv') as file:
         lines=csv.reader(file)
         for line in lines:
             l.append(line) #42001*785
    l.remove(l[0])
    l=array(l)
    label=l[:,0]
    data=l[:,1:]
    return normalizing(toInt(data)),toInt(label)  #label 1*42000  data 42000*784
    #return trainData,trainLabel


#result是结果列表
#csvName是存放结果的csv文件名
def saveResult(result,csvName):
    with open(csvName,'wb') as myFile:
        myWriter=csv.writer(myFile)
        j=1
        for i in result:
            tmp=[]
            tmp.append(j)
            tmp.append(int(i))
            myWriter.writerow(tmp)
            j +=1

from sklearn.neighbors import KNeighborsClassifier


def knnClassify(trainData, trainLabel, testData):
    knnClf = KNeighborsClassifier()  # default k=5, defined by yourself:KNeighborsClassifier(k_neigbors=10)
    knnClf.fit(trainData, ravel(trainLabel))
    testLabel=knnClf.predict(testData)
    saveResult(testLabel, 'sklearn_knn_result.csv')
    return testLabel

from sklearn import svm

def svmClassify(trainData, trainLabel, testData):
    svmClf = svm.SVC(5.0) # default:C=1.0,kernel = 'rbf'. you can try kernel:‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’
    svmClf.fit(trainData, ravel(trainLabel))
    testLabel = svmClf.predict(testData)
    saveResult(testLabel, 'sklearn_svm_result.csv')
    return testLabel


from sklearn.naive_bayes import GaussianNB


#调用scikit的朴素贝叶斯算法包,GaussianNB和MultinomialNB
def GaussianNBClassify(trainData, trainLabel, testData):

    nbClf = GaussianNB()         #nb for 高斯分布的数据
    nbClf.fit(trainData, ravel(trainLabel))
    testLabel = nbClf.predict(testData)
    saveResult(testLabel, 'sklearn_nb_result.csv')
    return testLabel


from sklearn.naive_bayes import MultinomialNB


def MultionomialNBClassify(trainData, trainLabel, testData):
    nbClt = MultinomialNB(alpha=0.1)
    nbClt.fit(trainData, ravel(trainLabel))
    testLabel = nbClt.predict(testData)
    saveResult(testLabel, 'sklearn_MultionalNB_alpha_Result.csv')
    return testLabel

def digitRecognition():
    trainData, trainLabel = loadTrainData()
    testData = loadTestData()
    # 使用不同算法

    #result1 = knnClassify(trainData, trainLabel, testData)
    result2 = svmClassify(trainData, trainLabel, testData)
    #result3 = GaussianNBClassify(trainData, trainLabel, testData)
    #result4 = MultionomialNBClassify(trainData, trainLabel, testData)

digitRecognition()