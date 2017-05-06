# _*_ coding:utf-8 _*_

"""
    朴素贝叶斯算法教程

    1.处理数据：从CSV文件中载入数据，然后划分为训练集和测试集。

    2.提取数据特征：提取训练数据集的属性特征，以便我们计算概率并做出预测。

    3.单一预测：使用数据集的特征生成单个预测。

    4.多重预测：基于给定测试数据集和一个已提取特征的训练数据集生成预测。

    5.评估精度：评估对于测试数据集的预测精度作为预测正确率。

    6.合并代码：使用所有代码呈现一个完整的、独立的朴素贝叶斯算法的实现。

"""
import csv
import random
import math


def loadCsv(filename):
    """
     处理数据：将加载进来的字符串数据类型的数据转换成我们可用的数字类型
    :param filename:文件名
    :return:
    """
    lines = csv.reader(open(filename, "rb"))
    dataset = list(lines)
    print len(dataset)
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]
    return dataset


def splitDataset(dataset,splitRatio):
    """
    将数据按照一定的比例划分为训练数据集和测试数据集
    :param dataset：未划分的数据集
    :param splitRatio:测试数据集与训练数据集划分的比例
    :return:返回训练数据集和测试数据集
    """
    trainSize = int(len(dataset)*splitRatio)
    trainSet = []
    copy = list(dataset)
    while len(trainSet) < trainSize:
        index = random.randrange(len(copy))
        trainSet.append(copy.pop(index))
    return [trainSet, copy]


"""
提取数据特征
我们将数据特征的获取划分为以下的子任务：
        1.按类别划分数据
        2.计算均值
        3.计算标准差
        4.提取数据集特征
        5.按类别提取属性特征
"""
def separateByClass(dataset):
    """
    按类别划分数据
    :param dataset:
    :return:
    """
    separated = {}
    for i in range(len(dataset)):
        vector = dataset[i]
        if (vector[-1] not in separated):
            separated[vector[-1]] = []
        separated[vector[-1]].append(vector)
    return separated


def mean(numbers):
    """
    计算均值
    :param numbers:
    :return:
    """
    return sum(numbers)/float(len(numbers))


def stdev(numbers):
    """
    计算方差
    :param numbers:
    :return:
    """
    avg = mean(numbers)
    variance = sum([pow(x-avg, 2) for x in numbers])/float(len(numbers)-1)
    return math.sqrt(variance)


def summarize(dataset):
    """
    计算每个属性的均值和方差
    :param dataset:
    :return:
    """
    summarizes = [(mean(attribute), stdev(attribute)) for attribute in zip(*dataset)]
    del summarizes[-1]
    return summarizes


def summarzieByClass(dataset):
    """
    按照类别提取均值和方差
    :param dataset:
    :return:
    """
    separated = separateByClass(dataset)
    summaries = {}
    for classValue, instances in separated.iteritems():
        summaries[classValue] = summarize(instances)
    return summaries


"""
预测

我们可以将这部分划分成以下任务：
1.计算高斯概率密度函数
2.计算对应类的概率
3.单一预测
4.评估精度
"""
def calculateProbability(x, mean, stdev):
    """
    计算高斯概率密度函数
    :param x:
    :param mean:
    :param stdev:
    :return:
    """
    exponent = math.exp(-(math.pow(x-mean, 2)/(2*math.pow(stdev, 2))))
    return (1/(math.sqrt(2 * math.pi) * stdev)) * exponent


def calculateClassProbabilities(summaries, inputVector):
    """
    计算所属类的概率
    :param summaries:
    :param inputVector:
    :return:
    """
    probabilities = {}
    for classValue, classSummaries in summaries.iteritems():
        probabilities[classValue] = 1
        for i in range(len(classSummaries)):
            mean, stdev = classSummaries[i]
            x = inputVector[i]
            probabilities[classValue] *= calculateProbability(x, mean, stdev)
    return probabilities


def predict(summaries, inputVector):
    """
    单一预测
    :param summaries:
    :param inputVector:
    :return:
    """
    probabilities = calculateClassProbabilities(summaries, inputVector)
    bestLabel, bestProb = None, -1
    for classValue, probability in probabilities.iteritems():
        if bestLabel is None or probability > bestProb:
            bestProb = probabilities
            bestLabel = classValue
    return bestLabel


def getPredictions(summaries, testSet):
    """
    多重预测
    :param summaries:
    :param testSet:
    :return:
    """
    predictions = []
    for i in range(len(testSet)):
        result = predict(summaries, testSet[i])
        predictions.append(result)
    return predictions


def getAccuracy(testSet, predictions):
    """
    计算预测的精度
    :param testSet:
    :param predictions:
    :return:
    """
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0


def main():
    filename = 'pima-indians-diabetes.data.csv'
    splitRatio = 0.67
    dataset = loadCsv(filename)
    trainingSet, testSet = splitDataset(dataset, splitRatio)
    print('Split {0} rows into train={1} and test={2} rows').format(len(dataset), len(trainingSet), len(testSet))
    # prepare model
    summaries = summarzieByClass(trainingSet)
    # test model
    predictions = getPredictions(summaries, testSet)
    accuracy = getAccuracy(testSet,predictions)
    print ('Accuracy:{0}%').format(accuracy)

main()
# summaries = {0:[(1, 0.5)], 1:[(20, 5.0)]}
# inputVector = [1.1, '?']
# probabilities = calculateClassProbabilities(summaries, inputVector)
# print('Probabilities for each class: {0}').format(probabilities)


# dataset = [[1, 20, 3, 1], [2, 21, 4, 0], [3, 22, 5, 1], [4, 22, 6, 0]]
# summary = summarzieByClass(dataset)
# print('Summary by class value:{0}').format(summary)
# dataset = [[1, 20, 0], [2, 21, 1], [3, 22, 0]]
# summary = summarize(dataset);
# print('Attribute summmaries:{0}').format(summary)
# filename = 'pima-indians-diabetes.data.csv'
# dataset = loadCsv(filename)
# print('Loaded data file {0} with {1} rows').format(filename, len(dataset))
# print dataset
