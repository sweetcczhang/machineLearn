# machineLearn
统计学习方法学习

### 决策树的C4.5算法实现
以信息增益作为划分训练数据集的特征，存在偏向于选择取值较多的特征的问题。使用信息增益比（information gain ratio）可以对这一问题进行校正。这是特征选择的另一准则。
1、计算给定数据集的香浓熵，熵越大，数据越混乱。
def calcShannonEnt(dataSet):

    输入：数据集
    输出：数据集的香浓熵
    描述：计算给定数据集的香浓熵；熵越大，数据集的混乱程度越大
    :param dataSet:
    :return:

2、按照给定特征划分数据集；去除选择维度中等于选择值得项
 
    输入：数据集，选择维度，选择值
    输出：划分数据集
    描述：按照给定特征划分数据集；去除选择维度中等于选择值的项
    :param dataSet:
    :param axis:
    :param value:
    :return:
3、选择最好的数据集划分维度

    输入：数据集
    输出：最好划分维度
    描述：选择最好的数据集划分维度
    :param dataSet:
    :return:
4、递归创建决策树

    输入：数据集、特征标签
    输出：决策树
    描述：递归构建决策树，利用上述函数
    :param dataSet:
    :param labels:
    :return:
5、使用决策树进行分类

    输入：决策树，分类标签，测试数据
    输出：决策结果
    描述：跑决策树
    :param inputTree:
    :param featLabels:
    :param testVec:
    :return:




