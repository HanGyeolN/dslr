class TrainData():
  def __init__(self):
    self.index = []
    self.data = {}
  
  def read_csv(self, filepath: str):
    fd = open(filepath, 'rt')
    first_line = fd.readline()
    self.index = first_line[:-1].split(',')
    for idx in self.index:
      self.data[idx] = []
    for line in fd.readlines():
      splited = line[:-1].split(',')
      length = len(splited)
      for i in range(length):
        self.data[self.index[i]].append(splited[i])

  def group_by(self, feature: str):
    groups = []
    for group in self.data[feature]:
      if group not in groups:
        groups.append(group)
    for feature in self.data:
      self.data[]

  def is_int(self, val):
    """
    문자열이 int 타임으로 바뀔 수 있는지 확인한다.
    """
    try:
      int(val)
      return True
    except ValueError:
      return False
  
  def is_float(self, val):
    """
    문자열이 float 타임으로 바뀔 수 있는지 확인한다.
    """
    try:
      float(val)
      return True
    except ValueError:
      return False
  
  def to_int(self, val):
    """
    기본 int() 함수와 동일한데,
    빈 문자열을 int으로 변환하는 경우 None으로 변환되도록 한다.
    """
    try:
      return int(val)
    except Exception as e:
      return None
  
  def to_float(self, val):
    """
    기본 float() 함수와 동일한데,
    빈 문자열을 float으로 변환하는 경우 None으로 변환되도록 한다.
    """
    try:
      return float(val)
    except Exception as e:
      return None

  def convert_type(self):
    """
    데이터 안에 문자열에서 int, float으로 변환 가능한 부분이 있으면 변환시킨다.
    """
    for key in self.data:
      sample = self.data[key][0]
      if (self.is_int(sample)):
        for i in range(len(self.data[key])):
          self.data[key][i] = self.to_int(self.data[key][i])
      elif (self.is_float(sample)):
        for i in range(len(self.data[key])):
          self.data[key][i] = self.to_float(self.data[key][i])
      else:
        continue
