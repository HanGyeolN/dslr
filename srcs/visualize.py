from cProfile import label
import sys
import matplotlib.pyplot as plt
from TrainData import TrainData
import seaborn as sns
from pandas import DataFrame

def show_groups_hist(data: dict, feature: str) -> None:
    plt.hist(list(filter(None, data["Ravenclaw"][feature])), bins = 10, alpha = 0.7, label="Ravenclaw", color="blue")
    plt.hist(list(filter(None, data["Slytherin"][feature])), bins = 10, alpha = 0.9, label="Slytherin", color="green")
    plt.hist(list(filter(None, data["Gryffindor"][feature])), bins = 10, alpha = 0.8, label="Gryffindor", color="red")
    plt.hist(list(filter(None, data["Hufflepuff"][feature])), bins = 10, alpha = 0.7, label="Hufflepuff", color="yellow")
    plt.title(feature)
    plt.legend()
    plt.show()

def show_all_hist(data: dict) -> None:
  for index in list(data["Ravenclaw"].keys())[5:]:
    show_groups_hist(data, index)

def sol0(train_data: TrainData) -> None:
  """
  Q. Which Hogwarts course has a homogeneous score distribution between all four houses?
  """
  data = train_data.group_by("Hogwarts House")
  show_groups_hist(data, "Care of Magical Creatures")

def show_all_scatter(data: dict) -> None:
  features = list(data["Ravenclaw"].keys())[5:]
  groups = list(data.keys())
  for f1 in range(len(features)):
    for f2 in range(f1 + 1, len(features)):
      for group in groups:
        # fig, (ax0, ax1) = plt.subplots(1, 2)
        # ax0.hist(list(filter(None, data[features[f1]])), alpha=0.7)
        # ax0.hist(list(filter(None, data[features[f2]])), alpha=0.7)
        plt.scatter(data[group][features[f1]], data[group][features[f2]], label=group)
      plt.xlabel(features[f1])
      plt.ylabel(features[f2])
      plt.legend()
      plt.show()


def sol1(train_data: TrainData) -> None:
  """
  What are the two features that are similar?
  """
  data = train_data.group_by("Hogwarts House")
  groups = list(data.keys())
  # show_all_scatter(data)
  for group in groups:
    plt.scatter(data[group]["Potions"], data[group]["Care of Magical Creatures"], label = group)
  plt.xlabel("Potions")
  plt.ylabel("Care of Magical Creatures")
  plt.legend()
  plt.show()

def sol2(train_data: TrainData) -> None:
  """
  From this visualization, what features are you going to use for your logistic regression?
  """
  df = DataFrame(train_data.data)
  print(df)


if __name__ == "__main__":
  if (len(sys.argv) != 2):
    raise Exception("Invalid arguments")
  train_data = TrainData()
  train_data.read_csv(sys.argv[1])
  train_data.convert_type()
  sol2(train_data)
