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
house_classifier.load("./test3")
house_classifier.train(x, y, category_dict, 10000)
house_classifier.save("./test4")

house_classifier.predict([41642.0,696.0960714808824,3.0201723778093963,-6.960960714808824,7.996,-365.1518504531068,393.13818539298967,4.207690767250213,1046.7427360602487,3.6689832316813447,0.3738525472517433,-244.48172,-13.62])

# logisreg.train(x, y)
