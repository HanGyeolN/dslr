from TrainData import TrainData
from describe import Analysis

ana = Analysis()
data = TrainData()
data.read_csv("./datasets/dataset_train.csv")
data.convert_type()
ret = data.get_numerics()
# print(ret.data)
ana.describe_all(ret.data)
# print(ret.data)
