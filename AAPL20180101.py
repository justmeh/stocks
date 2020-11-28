import os
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
if os.path.exists("dataAAPL.xlsx"):
  print("dataAAPL.xlsx exists")
else:
  crtBooks = open("dataAAPL.xlsx", "x")
  print("dataAAPL.xlsx has been created")
  crtBooks.close()
data = yf.download('AAPL','2019-01-01','2020-11-01') # Get the data of the stock AAPL 
data.Close.plot() 
data.to_excel(r'dataAAPL.xlsx', sheet_name='AAPL')
plt.show()
print(data)