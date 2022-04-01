from Classifier import Classifier
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

y, category_dict = data.categorize("Hogwarts House")
house_classifier = Classifier()
house_classifier.train(x, y, category_dict)
house_classifier.save("test")


# logisreg = LogisticRegression() # Ravenclaw 판별기
# logisreg.train(x, y)
