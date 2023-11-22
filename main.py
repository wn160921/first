import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import torch
import torch.optim as optim
import datetime
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

features = pd.read_csv("temps0.csv")
years = features['year']
months = features['month']
days = features['day']

dates = [str(int(year))+"-"+str(int(month))+"-"+str(int(day)) for year,month,day in zip(years,months,days)]
dates = [datetime.datetime.strptime(date, '%Y-%m-%d') for date in dates]
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2,ncols=2)
ax1.plot(dates, features['actual'])
ax1.set_xlabel('')
ax1.set_ylabel('temperature')
ax1.set_title('max temp')

ax2.plot(dates, features['temp_1'])
ax2.set_xlabel('')
ax2.set_ylabel('temperature')
ax2.set_title('previous max temp')

ax3.plot(dates, features['temp_2'])
ax3.set_xlabel('')
ax3.set_ylabel('temperature')
ax3.set_title('two days prior max temp')

ax4.plot(dates, features['friend'])
ax4.set_xlabel('')
ax4.set_ylabel('temperature')
ax4.set_title('friend temp')

plt.tight_layout(pad=2)
