# _*_ coding :utf-8 _*_
import kdTree as kd1
import kdTreeFind as kf
from time import clock
from random import random
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def random_point(k):
    return [random() for _ in range(k)]



def random_points(k, n):
    return [random_point(k) for _ in range(n)]


if __name__ == "__main__":
    data = [[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2]]  # samples

    kd = kd1.KdTree(data)

    ret = kf.find_nearest(kd, [3.0, 4.5])
    print ret

    N = 400000
    t0 = clock()
    kd2 = kd1.KdTree(random_points(3, N))
    ret2 = kf.find_nearest(kd2, [0.1, 0.5, 0.8])
    t1 = clock()
    print "time: ", t1 - t0, "s"
    print ret2