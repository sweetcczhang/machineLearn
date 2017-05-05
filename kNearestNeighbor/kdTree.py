# _*_ coding:utf-8 _*_
import sys
reload(sys)
sys.setdefaultencoding('utf8')


# kd-tree每个节点中主要包含的数据结构如下
class KdNode(object):
    def __init__(self, dom_elt, split, left, right):
        self.dom_elt = dom_elt   # k维向量节点（k维空间中的一个样本点）
        self.split = split       # 整数（进行分割维度的序号）
        self.left = left         # 该节点分割超平面左子空间构成的kd-tree
        self.right = right       # 该节点分割超平面右子空间构成的kd-tree


class KdTree(object):
    def __init__(self, data):
        k = len(data[0])  # 数据维度
        def CreateNode(split, data_set):  # 按照第split维划分数据集exset创建KdNode
            if not data_set:               # 数据集为空
                return None
            # key参数的值为一个函数，此函数只有一个参数且返回一个值用来进行比较
            # operator模块提供的itemgetter函数用于获取对象的哪些维的数据，参数需要获取的数据在对象的序号
            # data_set.sort(key=itemgetter(split)    #按要进行分割的那一维数据排序
            data_set.sort(key=lambda x: x[split])
            split_pos = len(data_set) // 2  # //为Python中的整数除法
            median = data_set[split_pos]   # 中位数分割点
            split_next = (split + 1) % k   # cycle coordinates

            # 递归的创建kd树
            return KdNode(median, split, CreateNode(split_next, data_set[:split_pos]),
                          CreateNode(split_next, data_set[split_pos+1:]))
        self.root = CreateNode(0, data)


# KDTree的前序遍历

def preorder(root):
    print root.dom_elt
    if root.left:
        preorder(root.left)
    if root.right:
        preorder(root.right)

if __name__ == "__main__":
    data = [[2,3],[5,4],[9,6],[4,7],[8,1],[7,2]]
    kd = KdTree(data)
    preorder(kd.root)