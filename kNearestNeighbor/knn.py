# _*_ coding :utf-8 _*_
import numpy as np
import operator

def createDataSet():
    """
    创建数据集
    :return:
    """
    group = np.array([[1.0, 1.1],
                      [1.1, 1.3],
                      [1.3, 1.0],
                      [0.9, 1.0],
                      [0.89, 1.12],
                      [1.0, 1.0],
                      [0.1, 0.14],
                      [0.4, 0.12],
                      [0.6, 0.34],
                      [0.2, 0.22],
                      [0.12, 0.1],
                      [0.31, 0.32],
                      [0, 0.1]])
    labels = ['A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B']
    return group, labels

def knn_classfy(inputdata,sample_data_set,labels,k):
    """
    knn算法的分类
    :param inputdata:待分类的输入数据
    :param sample_data_set: 待训练的样本数据
    :param labels:结果类型为标签
    :param k: k-近邻算法的k值
    :return: 返回该分类输入数据所对应的类型
    """
    # 样本数据的数据，对应为样本矩阵的行数
    sample_data_count = sample_data_set.shape[0]
    print  sample_data_set

    formated_inputdata = np.tile(inputdata,(sample_data_count,1))

    distances = (((formated_inputdata-sample_data_set)**2).sum(axis=1))**0.5

    sorted_data_indexs = distances.argsort()

    label_count_dict ={}

    for i in range(k):
        label =labels[sorted_data_indexs[i]]
        label_count_dict[label] = label_count_dict.get(label,0)+1
    sorted_label_count_list = sorted(label_count_dict.iteritems(),
                                     key=operator.itemgetter(1),
                                     reverse=True)
    return sorted_label_count_list[0][0]



