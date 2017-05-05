# _*_ coding:utf-8 _*_

import csv
import random
import math

def loadCsv(filename):
    lines = csv.reader(open(filename, "rb"))
    dataset = list(lines)
    print len(dataset)
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]
        print dataset[i]
    return dataset


def splitDataset(dataset,splitRatio):
    trainSize = int(len(dataset)*splitRatio)
    trainSet = []
    copy = list(dataset)
    while len(trainSet) < trainSize:
        index = random.randrange(len(copy))
        trainSet.append(copy.pop(index))
    return [trainSet, copy]


def separateByClass(dataset):
    separated = {}
    for i in range(len(dataset)):
        vector = dataset[i]
        if (vector[-1] not in separated):
            separated[vector[-1]] = []
        separated[vector[-1]].append(vector)
    return separated


def mean(numbers):
    return sum(numbers)/float(len(numbers))


def stdev(numbers):
    avg = mean(numbers)
    variance = sum([pow(x-avg, 2) for x in numbers])/float(len(numbers)-1)
    return math.sqrt(variance)


def summarize(dataset):
    summarizes = [(mean(attribute), stdev(attribute)) for attribute in zip(*dataset)]
    del summarizes[-1]
    return summarizes


def summarzieByClass(dataset):
    separated = separateByClass(dataset)
    summaries = {}
    for classValue, instances in separated.iteritems():
        summaries[classValue] = summarize(instances)
    return summaries


def calculateProbability(x, mean, stdev):
    exponent = math.exp(-(math.pow(x-mean, 2)/(2*math.pow(stdev, 2))))
    return (1/(math.sqrt(2 * math.pi) * stdev)) * exponent


def calculateClassProbabilities(summaries, inputVector):
    probabilities = {}
    for classValue, classSummaries in summaries.iteritems():
        probabilities[classValue] = 1
        for i in range(len(classSummaries)):
            mean, stdev = classSummaries[i]
            x = inputVector[i]
            probabilities[classValue] *= calculateProbability(x, mean, stdev)
    return probabilities


def predict(summaries, inputVector):
    probabilities = calculateClassProbabilities(summaries, inputVector)
    bestLabel, bestProb = None, -1
    for classValue, probability in probabilities.iteritems():
        if bestLabel is None or probability > bestProb:
            bestProb = probabilities
            bestLabel = classValue
    return bestLabel




dataset = [[1, 20, 3, 1], [2, 21, 4, 0], [3, 22, 5, 1], [4, 22, 6, 0]]
summary = summarzieByClass(dataset)
print('Summary by class value:{0}').format(summary)










dataset = [[1, 20, 0], [2, 21, 1], [3, 22, 0]]
summary = summarize(dataset);
print('Attribute summmaries:{0}').format(summary)
# filename = 'pima-indians-diabetes.data.csv'
# dataset = loadCsv(filename)
# print('Loaded data file {0} with {1} rows').format(filename, len(dataset))
# print dataset
