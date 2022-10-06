import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
from scipy.interpolate import make_interp_spline
import os 


os.chdir(r'C:\Users\soph_\Documents\phs\QCM')


x = []
y = []

with open(r'\Users\soph_\Documents\phs\QCM\ZnTPP.csv') as zntppfile:
    lines = csv.reader(zntppfile, delimiter=',')
    next(lines, None)
    for row in lines:  # read each line using for loop
        x.append(int(row[1]))
        y.append(float(row[4]))

#graph visualisation
plt.title("QCM ZnTPP in UHV")
plt.xlabel('Temperature ($^\circ$ C)')
plt.ylabel('Thickness difference')
plt.plot(x,y)
plt.savefig('ZnTPP_QCM.png')