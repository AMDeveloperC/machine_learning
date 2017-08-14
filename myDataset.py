import numpy as np

class TopicDataset:


	def __init__(self, d):
		self.data = np.array(d)


	def printData(self):
		for d in self.data:
			print d
