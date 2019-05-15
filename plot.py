import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

import glob

filename = "enph257pretest1.txt"

# arrays for each sensor and one for time
# each sensor shares the same timestamp
sensor0 = []
sensor1 = []
sensor2 = []
sensor3 = []
sensor4 = []
powerresistor = []
time = []

with open(self.filename,'r') as f:
    for line in f:
        if(line[0] is not ';'):
            line_split = line.split(' ')
            if (len(line_split) != 7):
                continue

            sensor0.append((float(line_split[0])))
            sensor1.append((float(line_split[1])))
            sensor2.append((float(line_split[2])))
            sensor3.append((float(line_split[3])))
            sensor4.append((float(line_split[4])))
            powerresistor.append((float(line_split[5])))
            time.append((float(line_split[6])))

# convert to numpy arrays for plotting
time = np.array(time)
sensor0 = np.array(sensor0)
sensor1 = np.array(sensor1)
sensor2 = np.array(sensor2)
sensor3 = np.array(sensor3)
sensor4 = np.array(sensor4)
powerresistor = np.array(powerresistor)
