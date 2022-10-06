# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 15:09:35 2022

@author: soph_
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import csv
from scipy.interpolate import make_interp_spline


x = []
y = []

with open(r'\Users\soph_\Documents\phs\QCM\ZnTPP.csv') as zntppfile:
    lines = csv.reader(zntppfile, delimiter=',')
    next(lines, None)
    for row in lines:  # read each line using for loop
        x.append(int(row[1]))
        y.append(float(row[4]))
print(x)
#X_Y_Spline = make_interp_spline(x,y)

# returns evenly spaced numbers over specified interval
#X_ = np.linspace(x.min(), x.max(), 500)
#Y_ = X_Y_Spline(X_)

# plotting graph
print(x[0])
print(x[len(x)-1])
print(len(y))

#temps = np.arange(int(x[0]), int(x[len(x)-1]), 5.0, dtype='int')
#plt.xticks(np.arange(min(x),max(x)+1, 5.0)) # :(
#plt.xticks(np.arange(int(x[0]), int(x[len(x)-1]), 5.0))
plt.title("QCM ZnTPP in UHV")
plt.xlabel('Temperature')
plt.ylabel('Thickness difference')


plt.plot(x,y)

#tick_spacing = 1
#fig, ax = plt.subplots(1,1)
# ax.plot(x,y)
# ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
plt.show()
