

def RMSE(records):
    return math.sqrt(sum([(rui-pui)*(rui-pui) for u,i,rui,pui in records])/float(len(records)))
def MAE(records):
    return sum([lbs(rui-pui) for u,i,rui,pui in records])/float(len(records))
