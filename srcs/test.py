from TrainData import TrainData
from describe import Analysis

ana = Analysis()
data = TrainData()
data.read_csv("./datasets/dataset_train.csv")
data.convert_type()
# y = data.data["Hogwart House"]
ret = data.get_numerics()
ret.pop("Index")
# x = ret

