from math import exp, log1p
from TrainData import TrainData

class Model():
  def __init__(self, model: dict = {"bias": 0, "weight": []}):
    self.bias = model["bias"]
    self.weight = model["weight"].copy()
 
class Normalizer():
  def __init__(self):
    self.min = 0
    self.max = 0
  
  def norm(self, data: list) -> list:
    """
    리스트를 정규화해서 반환합니다.
    """
    self.min = min(data)
    self.max = max(data)
    ret = []
    for x in data:
      ret.append((x - self.min) / (self.max - self.min))
    return ret

  def recover(self, x: float) -> float:
    """
    정규화 된 값을 복원해서 반환합니다.
    """
    return x * (self.max - self.min) + self.min

  def recover(self, xs: list) -> list:
    """
    정규화 된 값을 복원해서 반환합니다.
    """
    ret = []
    for x in xs:
      ret.append(self.recover(x))
    return ret

class LogisticRegression():
  def __init__(self, norms: list = [], model: dict = {}):
    self.norms = norms.copy()
    if len(model) == 0:
      self.model = Model()
    else:
      self.model = Model(model)
  
  def load(self, model: dict):
    """
    bias와 weight를 주어진 값으로 설정한다.
    """
    self.norms = []
    self.model = model.copy()

  def sigmoid(self, x: float) -> float:
    """
    예측한 log-odd를 0 ~ 1 사이의 값(확률)으로 변환한다
    x값이 너무 커지면 에러
    """
    if (x > 100):
      return 0.0000000000000001
    elif (x < -100):
      return 0.9999999999999999
    else:
      return 1 / (1 + exp(-x))

  def predict(self, x: list) -> float:
    """
    확률을 예측한다.
    """
    # ret = self.dot(self.mode.weight, x) + self.bias
    ret = self.dot(self.model.weight, x)
    return self.sigmoid(ret)

  def loss(self, x: TrainData, y: list, data_len: int) -> float:
    """
    loss 값을 반환한다.
    """
    sum = 0
    for i in range(data_len):
      sum += y[i] * log1p(self.predict(x.row(i))) + (1 - y[i]) * log1p(1 - self.predict(x.row(i)))
    return -(sum / data_len)

  def accuracy(self, x: TrainData, y: list) -> float:
    """
    맞춘 횟수와 틀린 횟수를 계산해서 정확도를 반환한다.
    """
    features = list(x.data.keys())
    true_count = 0
    false_count = 0
    for i in range(len(x.data[features[0]])):
      if round(self.predict(x.row(i))) == y[i]:
        true_count += 1
      else:
        false_count += 1
    # print(f"tn: {true_count} fn: {false_count}")
    return true_count / (true_count + false_count)

  def train(self, x: TrainData, y: list, learning_rate: float = 0.01, epoch: int = 1000):
    """
    학습 
    - 데이터 정규화를 여기서 해주지는 않는다
    """
    features = list(x.data.keys())
    # features 갯수만큼 weights 생성
    if (len(self.model.weight) == 0):
      for i in range(len(features)):
        self.model.weight.append(0.0)
    
    # loss 계산
    sum = 0
    data_len = len(x.data[features[0]])
    # loss = self.loss(x, y, data_len)
    # print(f"loss: {loss}")
    
    # 각 feature 마다 계산
    for epo in range(epoch):
      n = 0
      for feature in features:
        sum = 0
        for i in range(data_len):
          sum += (self.predict(x.row(i)) - y[i]) * x.data[feature][i]
        d_loss = sum / data_len
        self.model.weight[n] += d_loss * learning_rate
        n += 1
      if epo % 10 == 0:
        print(f"epoch: {epo} loss: {self.loss(x, y, data_len)} acc: {self.accuracy(x, y)}\nweights: {self.model.weight}")
    
  def dot(self, As: list, Bs: list) -> float:
    """
    행렬간 dot 연산을 해서 반환한다.
    """
    ret = 0.0
    if len(As) != len(Bs):
      raise Exception("length error")
    for i in range(len(As)):
      ret += As[i] * Bs[i]
    return (ret)
  