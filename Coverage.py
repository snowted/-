def Coverage(train,test,N):
    recommend_item=set()
    all_items=set()
    for user in train.keys():
        for item in train[user].key():
            all_items.add(item)
        rank=GetRecommendation(user,N)
        for item,pui in rank:
            recommend_items.add(item)
    return len(recommden_items)/(len(all_items)*1.0)
        
