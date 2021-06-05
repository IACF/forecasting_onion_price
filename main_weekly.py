#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import read_csv
import math
import statistics
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error
from keras.layers.core import Dense, Activation, Dropout
import time  # helper libraries

from dataset_window import Dataset


def convertCash(cash):
	cash = cash.replace('.', '')
	cash = cash.replace(',', '.')
	return float(cash)

def clearNanMM(moving_average, price):
        moving_average[0] = price[0]
        moving_average[1] = (price[0] + price[1])/2
        moving_average[2] = (price[0] + price[1] + price[2])/3
        return moving_average;


def create_dataset(dataset, look_back=1):
	dataX, dataY = [], []
	for i in range(len(dataset)-look_back):
		a = dataset[i:(i+look_back), :]
		dataX.append(a)
		dataY.append(dataset[i + look_back, 0])

	return np.array(dataX), np.array(dataY)

#Carregando os dados
data = pd.read_csv("Preços_semanais.csv")
data['DATA'] = pd.to_datetime(data.DATA, format='%d/%m/%y')
data.set_index('DATA', inplace=True)
index = data.index.values
data['PREÇO_DOLAR'] = data['PREÇO_DOLAR'].apply(convertCash)

import talib as ta

data['MEDIA_MOVEL'] = ta.EMA(data['PREÇO'], timeperiod=4)
data['MEDIA_MOVEL'] = clearNanMM(data['MEDIA_MOVEL'], data['PREÇO'])

# In[2]:


scaler_price = MinMaxScaler(feature_range=(0,1))
scaler_dollar = MinMaxScaler(feature_range=(0,1))
scaler_media_movel = MinMaxScaler(feature_range=(0,1))
data['PREÇO'] = scaler_price.fit_transform(data['PREÇO'].to_numpy().reshape(-1, 1))
data['PREÇO_DOLAR'] = scaler_dollar.fit_transform(data['PREÇO_DOLAR'].to_numpy().reshape(-1, 1))
data['MEDIA_MOVEL'] = scaler_dollar.fit_transform(data['MEDIA_MOVEL'].to_numpy().reshape(-1, 1))


# In[3]:


window = 4
shape_dataset = 154
epochs = 1000

x,y = create_dataset(data.values, window)
print(x.shape)


# In[4]:


train_x, test_x = x[0:shape_dataset, :], x[shape_dataset:, :]

train_y, test_y = y[0:shape_dataset], y[shape_dataset:]

print(test_y.shape)


# In[5]:


model = Sequential()
model.add(LSTM(25, input_shape=(4, 3)))
model.add(Dropout(0.1))
model.add(Dense(1))
model.compile(loss='mse', optimizer='adam')
model.fit(train_x, train_y, epochs=epochs, verbose=1)

trainPredict = model.predict(train_x)
testPredict = model.predict(test_x)


# In[6]:


print(test_x)
trainPredict = model.predict(train_x)
testPredict = model.predict(test_x)


# In[7]:


trainPredict = scaler_price.inverse_transform(trainPredict)
train_y = scaler_price.inverse_transform([train_y])

testPredict = scaler_price.inverse_transform(testPredict)
test_y = scaler_price.inverse_transform([test_y])



arr1 = index[158:];

df = pd.DataFrame(testPredict, columns=['preco'])
df['data'] = arr1

# In[8]:


#calculate mean absolute error
mape_train = mean_absolute_percentage_error(train_y[0], trainPredict)
print('Train Score: %.2f MAPE' % (mape_train))
mape_test = mean_absolute_percentage_error(test_y[0], testPredict)
print('Test Score: %.2f MAPE' % (mape_test))
print('\n -----------------------------------------\n')
#calculate mean absolute error
mae_train = mean_absolute_error(train_y[0], trainPredict)
print('Train Score: %.2f MAE' % (mae_train))
mae_test = mean_absolute_error(test_y[0], testPredict)
print('Test Score: %.2f MAE' %(mae_test))
print('\n -----------------------------------------\n')
# calculate root mean squared error
rmse_train = math.sqrt(mean_squared_error(train_y[0], trainPredict))
print('Train Score: %.2f RMSE' % (rmse_train))
rmse_test = math.sqrt(mean_squared_error(test_y[0], testPredict))
print('Test Score: %.2f RMSE' % (rmse_test))


# In[9]:


def sanitize_date(date):
    return date.month

def price_of_month(group):
    return group.iloc[-1,:]

prices = pd.DataFrame({
    'price': test_y.reshape(-1),
    'date': index[158:]
})

prices['month'] = prices.date.apply(sanitize_date)

prices_groupped = prices.groupby('month')

prices_by_month = prices_groupped.apply(price_of_month)

prices_by_month = prices_by_month.set_index('month')

price_json = prices_by_month.to_json(orient='index', date_format='iso', indent=4)


with open('price.json', 'w') as price_file:
    price_file.write(price_json)


# In[10]:


import talib as ta

mma = ta.EMA(testPredict.reshape(-1).astype('double'), timeperiod = 4)


# In[11]:


fig = plt.figure(figsize=(8, 6), dpi=600)
plt.plot(index[158:], testPredict, label='Preço previsto')
plt.plot(index[158:], test_y.reshape(-1, 1), label='Preço observado')
plt.ylabel('Preço de cebola (R$)')
plt.xlabel('Data')
plt.legend()
plt.show()
fig.savefig('weekly_predict.png')
