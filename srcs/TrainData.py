
class TrainData():
  def __init__(self):
    self.data = {}

  def pop(self, feature: str) -> None:
    """
    데이터에서 특정 feature 요소를 제거합니다.
    """
    self.data.pop(feature)
  
  def drop_na(self) -> None:
    """
    내부 데이터에서 값이 비어있는 행을 제거한다.
    """
    for feature in self.data.keys():
      idxes = []
      for i in range(len(self.data[feature])):
        if self.data[feature][i] is None:
          idxes.append(i)
      while len(idxes):
        self.del_row(idxes.pop())
      
  
  def del_row(self, index: int):
    """
    특정 행을 제거합니다.
    """
    for feature in self.data.keys():
      self.data[feature].pop(index)

  def row(self, idx: int) -> list:
    """
    특정 데이터 행을 리스트로 가져온다.
    """
    return [self.data[x][idx] for x in self.data.keys()]

  def categorize(self, feature: str) -> list:
    """
    특정 데이터 열을 숫자로 카테고리화 한 리스트를 반환한다.
    except - 값이 비어있는 경우 예외처리
    """
    data = self.data[feature]
    category = {}
    ret = []
    category_num = 0
    for el in data:
      if el not in category:
        category[el] = category_num
        category_num += 1
      ret.append(category[el])
    return ret

  def get_numerics(self):
    """
    데이터에서 숫자 데이터만 필터링해 가져옵니다.
    """
    filtered_data = TrainData()
    indexes = list(self.data.keys())
    for feature in indexes:
      feature_type = type(self.data[feature][0])
      if (feature_type == type(1) or feature_type == type(1.0)):
        filtered_data.data[feature] = self.data[feature].copy()
    return (filtered_data)
  
  def read_csv(self, filepath: str):
    """
    csv 데이터를 string 타입으로 읽어옵니다.
    """
    fd = open(filepath, 'rt')
    first_line = fd.readline()
    indexes = first_line[:-1].split(',')
    # 딕셔너러 초기화
    for idx in indexes:
      self.data[idx] = []
    # 데이터 파싱
    for line in fd.readlines():
      splited = line[:-1].split(',')
      length = len(splited)
      for i in range(length):
        self.data[indexes[i]].append(splited[i])

  def group_by(self, feature: str):
    """
    현재 데이터를 특정 feature의 그룹별로 묶어서 반환합니다.
    """
    grouped_data = {}
    groups = []
    # group 종류 뽑아내기
    for group in self.data[feature]:
      if group not in groups:
        groups.append(group)
    # 그룹별 딕셔너리 생성
    for group in groups:
      grouped_data[group] = {}
      for f in self.data:
        if f != feature:
          grouped_data[group][f] = []
    # 값 집어넣기
    for i in range(len(self.data[feature])):
      for f in self.data:
        if f != feature:
          grouped_data[self.data[feature][i]][f].append(self.data[f][i])
    return grouped_data

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
