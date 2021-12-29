# import numpy as np

# a = np.array([1,2,3])  # rank1 array
# print(a)
# print(type(a))
# print(a.shape)
# print(a[0], a[1], a[2])

# b = np.array([[1,2,3],[4,5,6]])  #rank2 array
# ls = [[1,2,3], [4,5,6]]

# # print(b)
# # print(b.shape)
# print(ls[1,2])

# a = np.zeros((100,100))
# print(a.shape)

# a = np.ones((4,2))
# print(a)

# a = np.full((4,5), 1876)
# print(a)

# a = np.eye(3)
# print(a)

# a = np.random.randint(2,100, (2,2))
# print(a)

# x = np.array([[1,2],[3,4]])
# y = np.array([[5,6],[7,8]])

# print(np.multiply(y,x))
# print(np.divide(y,x))


# print(np.sqrt(x))

# print(x.ndim)
# print(x.shape)

# print(np.dot(x,y))

import numpy as np
import matplotlib.pyplot as plt

# x = np.arange(0, 3*np.pi,0.1)
# y = np.sin(x)
# y = np.cos(x)
# plt.plot(x,y)
# plt.show()

# x = np.arange(0, 3*np.pi,0.1)
# y_sin= np.sin(x)
# y_cos = np.cos(x)
#
# plt.plot(x,y_sin)
# plt.plot(x,y_cos)
#
# plt.xlabel('x axis label')
# plt.ylabel('y axis label')
# plt.title('Sine and Cosine Graph')
# plt.legend(['sin','cos'])
#
#
# plt.show()

# import pandas as pd
# data = pd.read_csv('train.csv')
# print(data.head())

import pandas as pd

df = pd.read_csv('train.csv')

import folium
from folium import plugins

stationArr = df[['Y', 'X']].values

m = folium.Map(location=[stationArr[0][0], stationArr[0][1]], zoom_start=15)
m.add_child(plugins.HeatMap(stationArr[:50000], radius=15))
m.save('abc.html')
