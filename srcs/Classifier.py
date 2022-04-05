from distutils.log import Log
from typing import Dict
from TrainData import TrainData
from LogisticRegression import LogisticRegression
import json

class Classifier():
  def __init__(self):
    self.logi_regs: Dict[str, LogisticRegression] = {}
    self.categories: Dict[str, int] = {}
    self.labels: Dict[str, list] = {}
  # def train()

  def train(self, x: TrainData, y: list, category_dict: dict, epoch: int = 1000):
    """
    x: 훈련에 사용될 데이터
    y: 분류결과
    category_dict: 범주 표
    """
    self.categories = category_dict
    # 카테고리 갯수만큼 LogisticRegression 분류기를 생성 
    # (이진 분류밖에 못하니까 여러 클래스로 분류하려면 여러개가 있어야함)
    if len(self.logi_regs) == 0:
      # 분류기가 load되지 않았으면 새로 만들어야함.
      for category in self.categories.keys():
        self.logi_regs[category] = LogisticRegression()
    
    # 분류기 별 정답지 생성
    for category in self.categories.keys():
      target_index = self.categories[category]
      self.labels[category] = []
      for i in y:
        if (i == target_index):
          self.labels[category].append(1)
        else:
          self.labels[category].append(0)
    # 학습
    for category in self.logi_regs.keys():
      self.logi_regs[category].train(x, self.labels[category], epoch = epoch)

  def predict(self, x: list):
    """
    어떤 범주에 속할지 예측한다.
    """
    result = {}
    for name in self.logi_regs.keys():
      result[name] = self.logi_regs[name].predict(x)
    print(result)
    
  def load(self, filepath: str):
    """
    분류기에 필요한 데이터들을 불러온다.
    """
    fp = open(filepath, "rt")
    load_data = json.load(fp)
    for name in load_data["models"].keys():
      self.logi_regs[name] = LogisticRegression(model = load_data["models"][name])
    self.categories = load_data["categories"].copy()
    fp.close()

  def save(self, filepath: str):
    """
    분류 모델을 저장한다.
    {
      "models": {
        "model-name-01": {
          "bias": 0,
          "weight": [1.0, 2.0, ...]
        }, ...
      },
      "categories": {
        "cate00": 0,
        "cate01": 1,
        "cate02": 2,
        ...
        }
      }
    }
    """
    models = {}
    for category in self.logi_regs:
      models[category] = {
        "bias": 0,
        "weight": self.logi_regs[category].model.weight
      }
    classifier_dict = {
      "models": models,
      "categories": self.categories
    }
    fp = open(filepath, "wt")
    json.dump(classifier_dict, fp)
    fp.close()
