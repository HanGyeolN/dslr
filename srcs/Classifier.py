from calendar import c
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
      self.logi_regs[category].train(x, self.labels[category], epoch = 10)

  def save(self, filepath: str):
    """
    분류 모델을 저장한다.
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
