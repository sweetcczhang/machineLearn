# _*_ coding:utf-8 _*_
import numpy as np
import kmeandeno as km


def distEclud(vecA, vecB):
    return np.sqrt(sum(np.power(vecA-vecB,2)))

def biKmeans(dataSet, k, distMeans=distEclud):
     m = np.shape(dataSet)[0];
     clusterAssment = np.mat(np.zeros((m, 2)))
     centroid0 = np.mean(dataSet,axis=0).tolist()[0]
     centList = [centroid0]
     for j in range(m):
         clusterAssment[j, 1] = distMeans(np.mat(centroid0), dataSet[j, :])**2

     while (len(centList) < k):
        lowserSSE = np.inf
        for i in range(len(centList)):
            ptsInCurrCluster = dataSet[np.nonzero(clusterAssment[:, 0].A == i)[0], :]
            centroidMat, splitClustAss = km.KMeans(ptsInCurrCluster, 2, distMeans)

            sseSplit = sum(splitClustAss[:, 1])
            sseNotSplit = sum(clusterAssment[np.nonzero(clusterAssment[:, 0].A != i)[0], 1])
            print "sseSplit:", sseSplit
            print "sseNotSplit:", sseNotSplit
            if (sseSplit + sseNotSplit)< lowserSSE:
                bestCentToSplit = i
                bestNewCents = centroidMat
                bestClustAss = splitClustAss.copy()
                lowserSSE = sseNotSplit + sseSplit
        bestClustAss[np.nonzero(bestClustAss[:, 0].A == 1)[0], 0] = len(centList)
        bestClustAss[np.nonzero(bestClustAss[:, 0].A == 0)[0], 0] = bestCentToSplit

        print 'the bestCentToSplit is: ', bestCentToSplit
        print 'the len of bestClustAss is: ', len(bestClustAss)
        centList.append(bestNewCents[1, :].tolist()[0])
        clusterAssment[np.nonzero(clusterAssment[:,0].A == bestCentToSplit)[0], :] = bestClustAss
     return np.mat(centList), clusterAssment