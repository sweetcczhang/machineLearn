# _*_ coding utf-8 _*_

from numpy import *
import operator
import csv

def toInt(array1):
    array1 = mat(array1)
    m, n = shape(array1)
    print m,n
    newArray = zeros((m, n))
    for i in range(m):
        for j in range(n):
            newArray[i, j]=int(array1[i, j])


    return newArray

def normalizing(array1):
    m, n = shape(array1)
    for i in range(m):
        for j in range(n):
            if array1[i, j] != 0:
                array1[i, j] = 1

    return array1


def loadTrainData():
    l = []
    with open('train.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            l.append(line)
    l.remove(l[0])
    #print l
    l = array(l)
    labels = l[:,0]
    #print labels
    data = l[:, 1:]
    #print data[:,1:4]
    print 'zcc'
    print toInt(labels)
    return normalizing(toInt(data)),toInt(labels)


def loadTestData():
    l = []
    with open('test.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            l.append(line)
    l.remove(l[0])
    l = array(l)
    return normalizing(toInt(l))

def loadTestReult():
    l = []
    with open('sample_submission.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            l.append(line)
    l.remove(l[0])
    labels = array(l)
    return normalizing(toInt(labels))

def classify(intX, dataSet, labels, k):
    intX = mat(intX)
    dataSet = mat(dataSet)
    labels = mat(labels)
    dataSize = dataSet.shape[0]
    diffMat = tile(intX, (dataSize, 1))-dataSet
    sqDiffMat = array(diffMat)**2
    sqDistance = sqDiffMat.sum(axis=1)
    distances = sqDistance**0.5
    sortDistance = distances.argsort()
    classCount={}
    for i in range(k):
        votelabel = labels[0,sortDistance[i]]
        classCount[votelabel] = classCount.get(votelabel, 0)+1
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def saveResult(result):
    with open('result.csv','wb') as myFile:
        myWrite=csv.writer(myFile)
        j = 1
        for i in result:
            tmp =[]
            tmp.append(j)
            tmp.append(i)
            myWrite.writerow(tmp)
            j=j+1

def handWritingClassTest():
    trainData, TrainLabel = loadTrainData()
    testData = loadTestData()
    m, n=shape(testData)
    errorCount=0
    resultList=[]
    for i in range(m):
        classifierResult = classify(testData[i], trainData, TrainLabel, 5)
        resultList.append(classifierResult)
        print 'the classifier cam' \
              'e back with:%d' %(classifierResult)
    print 'finish the train'
    saveResult(resultList)


#handWritingClassTest()
# newa = zeros((5,7))
# print newa

