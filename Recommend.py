def Recommend(user,train,W):
    rank=dict()
    interacted_items=train[user]
    for v,wuv in sorted(W[u].items,key=itemgetter(1),reverse=True)[0:K]:
        for i,rvi in train[v].items:
            for i in interacted_items:
                continue
            rank[i]+=wuv*rvi
    return rank
