import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import read_csv
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from keras.layers.core import Dense, Activation, Dropout
import time  # helper libraries


def convertCash(cash):
    cash = cash.replace('.', '')
    cash = cash.replace(',', '.')
    return float(cash)


#Carregando os dados
data = pd.read_csv("onion_price.csv", parse_dates=['Mês'])
data.set_index('Mês', inplace=True)

data['Preço'] = data['Preço'].apply(convertCash)
data['PREÇO_DOLAR'] = data['PREÇO_DOLAR'].apply(convertCash)
data['VARIAÇÃO/MÊS'] = data['VARIAÇÃO/MÊS'].apply(convertCash)

price_series = data['Preço']
data = data.drop('Preço', axis=1)

scaler_price = MinMaxScaler(feature_range=(0,1))
price_norm_dataset = scaler_price.fit_transform(price_series.to_numpy().reshape(-1, 1))


scaler = MinMaxScaler()

dataset = scaler.fit_transform(data)

train_x, test_x = dataset[0:36, :], dataset[36:, :]

train_y, test_y = price_norm_dataset[0:36, :], price_norm_dataset[36:, :]

train_x = np.reshape(train_x, (train_x.shape[0], 1, train_x.shape[1]))
test_x = np.reshape(test_x, (test_x.shape[0], 1, test_x.shape[1]))

model = Sequential()
model.add(LSTM(25, input_shape=(1, dataset.shape[1])))
model.add(Dropout(0.1))
model.add(Dense(1))
model.compile(loss='mse', optimizer='adam')
model.fit(train_x, train_y, epochs=1000, verbose=1)

trainPredict = model.predict(train_x)
testPredict = model.predict(test_x)

trainPredict = scaler_price.inverse_transform(trainPredict)
train_y = scaler_price.inverse_transform(train_y)

testPredict = scaler_price.inverse_transform(testPredict)
test_y = scaler_price.inverse_transform(test_y)

# calculate root mean squared error
trainScore = math.sqrt(mean_squared_error(train_y, trainPredict))
print('Train Score: %.2f RMSE' % (trainScore))
testScore = math.sqrt(mean_squared_error(test_y, testPredict))
print('Test Score: %.2f RMSE' % (testScore))
