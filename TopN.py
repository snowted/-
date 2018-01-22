#
def PrecisionRecall(test,N):
    #初始化数值
    hit =0
    n_recall = 0
    n_precision =0
    
    for user,items in test.items():
        rank=Recommend(user,N)
        #得到用户推荐列表
        hit+=len(rank&items)
        #求rank和items的与值，求得总长度
        n_recall+=len(items)
        
        n_precision+=N
    return [hit/(1.0*n_recall),hit/(1.0*n_precision)]
