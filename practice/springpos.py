import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from math import log
from sklearn import linear_model

data  = pd.read_csv('Assignment2.data', sep='\t')
data.head()
data.describe()

fig, (ax1) = plt.subplots( 1)
fig.suptitle('Two Cyber Physical Systems')
fig.set_figwidth(10)
fig.set_figheight(5)

ax1.plot(data.SpringPos, 'r+')
ax1.set_ylabel('Spring Position')
# ax2.plot(data.StockPrice, 'b.')
# ax2.set_ylabel('Stock Price')
# ax2.set_xlabel('time')

plt.show()