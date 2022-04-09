from Classifier import Classifier
from TrainData import TrainData
from describe import Analysis
from LogisticRegression import LogisticRegression

ana = Analysis()
train_data = TrainData()
train_data.read_csv("./datasets/dataset_train.csv")
train_data.convert_type()
train_data.drop_na()

valid_data = TrainData()
valid_data.read_csv("./datasets/dataset_valid.csv")
valid_data.convert_type()
valid_data.drop_na()
y_ans = valid_data.data["Hogwarts House"]
validset = valid_data.get_numerics()
validset.pop("Index")
# print(validset.data)
# ana.describe_all(data.data)

x = train_data.get_numerics()
x.pop("Index")

y, category_dict = train_data.categorize("Hogwarts House")
house_classifier = Classifier()
house_classifier.load("./test4")
# house_classifier.train(x, y, category_dict, 1000)
# house_classifier.save("./test4")

y_pred = house_classifier.predict_many(validset)
print(y_pred)
print(y_ans)

# logisreg.train(x, y)
