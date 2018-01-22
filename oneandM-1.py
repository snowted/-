#将数据集分成训练集和测试集的过程
def SplitData(data,M,k,seed):
    test=[]
    train=[]
    random.seed(seed)
    for user,item in data:
        if random.randint(0,M)==k:
            test.append([user,item])
        else:
            train.append([user,item])
    return train,test
