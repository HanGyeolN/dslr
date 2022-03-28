from TrainData import TrainData
from describe import Analysis
from LogisticRegression import LogisticRegression

ana = Analysis()
data = TrainData()
data.read_csv("./datasets/dataset_train.csv")
data.convert_type()
data.drop_na()
# ana.describe_all(data.data)

x = data.get_numerics()
x.pop("Index")

y = data.categorize("Hogwarts House")
for i in range(len(y)):
  if y[i] != 0:
    y[i] = 1

logisreg = LogisticRegression()
logisreg.train(x, y)
