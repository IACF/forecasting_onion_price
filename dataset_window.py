import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import read_csv
import math

class Dataset:
	def __init__(self, data, look_back):
		self.__windowed_dataset = self.make_window(data, look_back)

	def make_window(self, data, look_back):
		data = data.values
		dataX, dataY = [], []
		for i in range(len(data)-look_back-1):
			a = data[i:(i+look_back), :]
			dataX.append(a)
			dataY.append(data[i + look_back, :])
		return np.array(dataX), np.array(dataY)

	def windowed_dataset(self):
		return self.__windowed_dataset
