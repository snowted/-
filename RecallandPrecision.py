def Recall(train,test,N):
    hit=0
    all=0
    for user in train.keys():
        tu=test[user]
        rank=GetRecommendation(user,N)
        for item,pui in rank:
            if item in tu:
                hit+=1
            all+=len(tu)
        return hit/(all*1.0)
def Precision(train,test,N):
    hit=0
    all=0
    for user in train.keys:
        tu=test[user]
        rank=GetRecommendation(user,N)
        for item,pui in rank:
            if item in tu:
                hit+=1
            all+=N
        return hit/(all*1.0)
