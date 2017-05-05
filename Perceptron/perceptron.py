# _*_ coding :utf-8 _*_
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import copy

training_set = [[(3, 3), 1], [(4, 3), 1], [(1, 1), -1]]
w = [0, 0]
b = 0
history = 0


def update(item):
    global w, b, history
    w[0] += 1 * item[0][0] * item[1]
    w[1] += 1 * item[0][1] * item[1]
    b += 1 * item[1]
    print w, b
    history.append([copy.copy(w), b])


def cal(item):
    res = 0
    for i in range(len(item[0])):
        res += item[0][i] * w[i]
        res += b
        res *= item[1]
    return res


def check():

    flag = False
    for item in training_set:
        if cal(item) <= 0:
            flag =True
            update(item)
    if not flag:
        print "RESTFUL: w:" + str(w) + "b: " + str(b)
    return flag

if __name__ == "__main__":
    for i in range(1000):
        if not check(): break
