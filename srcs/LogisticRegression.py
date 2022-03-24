class LogisticRegression():
  def __init__(self):
    self.train_count = 0
    self.learning_rate = 0.1
    self.weight = []
    self.bias = 0

  def dot(self, As: list, Bs: list) -> float:
    ret = 0.0
    if len(As) != len(Bs):
      raise Exception("length error")
    for i in range(len(As)):
      ret += As[i] * Bs[i]
    return (ret)

  def estimate(self, x):
    return self.dot(self.weight, x) + self.bias
