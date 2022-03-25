from srcs.TrainData import TrainData


class Model():
  def __init__(self):
    self.bias = 0
    self.weight = []

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
  def __init__(self):
    self.norms = []
    self.model = Model()

  def dot(self, As: list, Bs: list) -> float:
    ret = 0.0
    if len(As) != len(Bs):
      raise Exception("length error")
    for i in range(len(As)):
      ret += As[i] * Bs[i]
    return (ret)

  def estimate(self, x):
    return self.dot(self.weight, x) + self.bias

  