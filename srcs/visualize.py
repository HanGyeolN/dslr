import sys
from TrainData import TrainData

if __name__ == "__main__":
	if (len(sys.argv) != 2):
		raise Exception("Invalid arguments")
	train_data = TrainData()
	train_data.read_csv(sys.argv[1])
	train_data.convert_type()
	data = train_data.group_by("Hogwarts House")
	