# _*_ coding utf-8 _*_

from numpy import *
import operator
import csv
import pandas as pd


df=pd.read_csv('train.csv')
print df.head()



def loadResult():
     l = []
     with open('result.csv') as myfile:
         lines = csv.reader(myfile)
         for line in lines:
             l.append(line)
     l.remove(l[0])
     l = array(l)
     print l
     data=l[:,1]
     print data
     return data

def saveResult(result):
    with open('result1.csv','wb') as myFile:
        myWrite=csv.writer(myFile)
        j =1
        for i in result[0]:
            tmp =[]
            tmp.append(j)
            print int(i)
            tmp.append(int(i))
            myWrite.writerow(tmp)
            j +=1



def toInt(array1):
    array1 = mat(array1)
    #print array1
    m, n = shape(array1)
    print m,n
    newArray = zeros((m, n))
    for i in range(m):
        for j in range(n):
            newArray[i, j]=float(array1[i, j])
            newArray[i, j] =int(newArray[i, j])
    return newArray


#saveResult(toInt(loadResult()))
#print int(3.5)
#print float('3.5')