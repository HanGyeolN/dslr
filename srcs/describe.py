import math
import sys
from TrainData import TrainData

class Analysis():
  def sum(self, data: list) -> float:
    ret = 0
    for i in data:
      ret += i
    return (ret)

  def get_std(self, data: list) -> float:
    """
    표준편차를 반환한다.
    """
    mean = self.sum(data) / len(data)
    sum = 0
    for i in data:
      sum += (i - mean) * (i - mean)
    variance = sum / len(data)
    return (math.sqrt(variance))

  def describe(self, data_list: list) -> dict:
    """
    데이터의 요약 정보를 반환한다.
    리스트 사이에 None이 있는 경우 제거된다.
    """
    if (len(data_list) == 0):
      raise Exception("Empty list")
    if (type(data_list[0]) != type(0) and type(data_list[0]) != type(0.0)):
      raise Exception("Invalid type")
    data_list = [x for x in data_list if x is not None]
    data_sorted = sorted(data_list)
    return {
      "Count": len(data_list),
      "Mean": self.sum(data_sorted) / len(data_list),
      "Std": self.get_std(data_sorted),
      "Min": data_sorted[0],
      "25%": data_sorted[int(len(data_list) * 0.25)],
      "50%": data_sorted[int(len(data_list) * 0.50)],
      "75%": data_sorted[int(len(data_list) * 0.75)],
      "Max": data_sorted[-1]
    }

  def describe_all(self, data):
    ret = {}
    for key in data:
      try:
        ret[key] = analysis.describe(train_data.data[key])
      except Exception as e:
        continue
    str = f"{'':<10}"
    for key in ret:
      if len(key) > 17:
        key = key[:12] + ".."
      str += f"{key:>17.15s}"
    print(str)
    keys = ret[key].keys()
    for key in keys:
      str = ""
      str += f"{key:<10s}"
      for k in ret:
        str += f"{ret[k][key]:>17.6f}"
      print(str)

if __name__ == "__main__":
  if len(sys.argv) != 2:
    raise Exception("Invalid arguments")
  file_path = sys.argv[1]
  train_data = TrainData()
  train_data.read_csv(file_path)
  train_data.convert_type()
  analysis = Analysis()
  analysis.describe_all(train_data.data)
