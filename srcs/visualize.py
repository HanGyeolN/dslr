import sys
import matplotlib.pyplot as plt
from TrainData import TrainData
from describe import Analysis
import seaborn as sns
import pandas as pd

def show_groups_hist(data: dict, feature: str) -> None:
    ana = Analysis()
    groups_data = {}
    for group in ["Ravenclaw", "Slytherin", "Gryffindor", "Hufflepuff"]:
      groups_data[group] = ana.describe(list(filter(None, data[group][feature])))
    ana.describe_group(groups_data)
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
  # show_all_hist(data)

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

def sol2(filepath: str) -> None:
  """
  From this visualization, what features are you going to use for your logistic regression?
  """
  df = pd.read_csv(filepath)
  icol = [x for x in range(6, 19)]
  icol.append(1)
  sns.set(rc={'figure.figsize':(10,10)})
  fig = sns.pairplot(df[:50], hue = "Hogwarts House", dropna = True)
  fig.savefig("pairplot.png")
  plt.show()


if __name__ == "__main__":
  if (len(sys.argv) != 3):
    raise Exception("Invalid arguments")
  train_data = TrainData()
  train_data.read_csv(sys.argv[1])
  train_data.convert_type()
  if sys.argv[2] == "histogram":
    sol0(train_data)
  elif sys.argv[2] == "scatterplot":
    sol1(train_data)
  elif sys.argv[2] == "pairplot":
    sol2(sys.argv[1])
  else:
    raise Exception("Invalid plot method")
