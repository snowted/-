def UserSimilarity(train):
    item_users=dict()
    for u,items in train.items():
        for i in items.keys():
            if i not in item_users:
                item_user[i]=set()
            item_users[i].add(u)
    C=dict()
    N=dict()
    for i,users in item_users.items():
        for u in users:
            N(u）+=1
            for v in users:
              if u==v:
                  continue
              C[u][v]+=1
    W=dict()
    for u,related_users in C.items():
              for v,cuv in related_users.items():
                  W[u][v]=cuv/math.sqrt(N[u]*N[v])
    return W
              
