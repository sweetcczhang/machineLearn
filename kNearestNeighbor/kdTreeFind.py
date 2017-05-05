# _*_ coding: utf-8 _*_
from math import sqrt
from collections import namedtuple

result = namedtuple("Result_tuple","nearest_point nearest_dist nodes_visited")

def find_nearest(tree, point):
    k = len(point) #数据维度
    def travel(kd_node,target,max_dist):
        if kd_node is None:
            return result([0]*k, float("inf"), 0)
        nodes_visited = 1
        s = kd_node.split         # 进行分割的维度
        pivot = kd_node.dom_elt   # 进行分割的“轴”

        if target[s]<=pivot[s]:             # 如果目标点第s维小于分割轴的对应值（目标离左子树）
            nearer_node = kd_node.left      # 下一个访问节点为左子树根节点
            further_node = kd_node.right    # 同时记录右子树
        else:                              # 目标离右子树更近
            nearer_node = kd_node.right     # 下一个访问节点为右子树根节点
            further_node = kd_node.left

        temp1 = travel(nearer_node, target, max_dist)       # 进行遍历找到包含目标点的区域
        nearest = temp1.nearest_point                       # 以此叶结点作为“当前最近点”
        dist = temp1.nearest_dist                           # 更新最近距离
        nodes_visited += temp1.nodes_visited
        if dist < max_dist:
            max_dist = dist    # 最近点将在以目标点为球心，max_dist为半径的超球体内

        temp_dist = abs(pivot[s] - target[s])       # 第s维上目标点与分割超平面的距离
        if max_dist < temp_dist:                    # 判断超球体是否与超平面相交
            return result(nearest, dist, nodes_visited)   # 不相交则可以直接返回，不用继续判断

        # ----------------------------------------------------------------------
        # 计算目标点与分割点的欧氏距离
        temp_dist = sqrt(sum((p1-p2) ** 2 for p1, p2 in zip(pivot, target)))

        if temp_dist < dist:
            nearest = pivot
            dist = temp_dist
            max_dist = dist
        # 检查另一个子结点对应的区域是否有更近的点
        temp2 = travel(further_node, target, max_dist)
        nodes_visited += temp2.nodes_visited
        if temp2.nearest_dist < dist:      # 如果另一个子结点内存在更近距离
            nearest = temp2.nearest_point  # 更新最近点
            dist = temp2.nearest_dist      # 更新最近距离
        return result(nearest,dist, nodes_visited)
    return travel(tree.root, point, float("inf"))