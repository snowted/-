def popularity(train,test,N):
    item_popularity=dict()
    for user,item in train.items():
        for item in items.keys():
            if item not in items.keys():
                item_popularity[item]=0
            item_popularity[item]+=1
    ret=0
    n=0
    for user in train.keys():
        rank=GetRecommendation(user,N)
        for item,pui in rank:
            ret+=math.log(1+item_popularity[item])
            n+=1
    ret/=n*1.0
    return tet
            
