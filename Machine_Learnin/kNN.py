from numpy import *
import operator

def createDataSet():
    group = array([[1,0,1,1],[1,0,1,0],[0,0],[0,0,1]] )
    labels = ['A','A','B','B']
    return group, labels

def classify0(inx, dataSet, labels, k):# 参数为 输入向量, 训练样本集, 标签向量, 选择最近邻居的数目
    dataSetSize = dataSet.shape[0]
    # 以下三行为距离计算
    diffMat = tile(inx, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    # 以下为选择距离最小的k个点
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[1]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(),
        # 排序
        key = operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


group,labels = createDataSet()
print(group,labels)

classify0([0,0], group, labels, 3)