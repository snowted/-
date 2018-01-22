from surprise import SVD  
from surprise import Dataset  
from surprise import evaluate, print_perf  
from surprise import dataset  
  
  
#加载本地数据集进行3次交叉实验  
  
#每行数据类型为user item rating,依据空格来分割  
reader=dataset.Reader(line_format='user item rating', sep=' ')  
data =Dataset.load_from_file('C:\Users\snow ted\Desktop\train.text','r')  
#定义3次交叉实验，如果不定义这句默认为5次  
data.split(n_folds=3)  
  
# We'll use the famous SVD algorithm.  
algo = SVD()  
  
# Evaluate performances of our algorithm on the dataset.  
perf = evaluate(algo, data, measures=['RMSE', 'MAE'])  
  
print_perf(perf)  
