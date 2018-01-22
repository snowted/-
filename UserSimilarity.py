def UserSimilarity(train):
    W=dict()
    for u in train.keys():
        for v in train.keys():
            if u==v:
                continue
            W[u][v]=len(train[u]&train[v])
            W[u][v]/=math.sqrt(len(train[u])*len(train[v])*1.0)
    return W
