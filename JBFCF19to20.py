import os
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import seaborn as sns
sns.set_theme(style="darkgrid")
data = yf.download('JBFCF','2020-01-01','2020-11-01') # Get the data of the Jolibee's stock 
#data is now a data frame
data.Close.plot(label='JBFCF2020')
data2 = yf.download('JBFCF','2010-01-01','2020-01-01')
data2.Close.plot(label='JBFCF2019')
plt.legend()
plt.plot()
plt.show()
