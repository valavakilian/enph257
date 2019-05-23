import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from datetime import datetime

import glob

filename = "experiment_14_23_57.756337.txt"

# arrays for each sensor and one for time
# each sensor shares the same timestamp
sensor0 = []
sensor1 = []
sensor2 = []
sensor3 = []
sensor4 = []
powerresistor = []
time = []

initial_time = -1

with open(filename,'r') as f:
    for line in f:
        if(line[0] is not ';'):
            line_split = line.split('  ')
            if (len(line_split) != 7):
                continue
            current_time = line_split[0]
            time_split = current_time.split(':')
            hours = float(time_split[0])
            minutes = float(time_split[1])
            seconds = hours*60*60 + minutes*60 + float(time_split[2])
            # single_time = datetime.strptime(line_split[0], '%X')

            if initial_time == -1:
                initial_time = seconds

            time.append(float(seconds-initial_time))
            sensor0.append((float(line_split[1])))
            sensor1.append((float(line_split[2])))
            sensor2.append((float(line_split[3])))
            sensor3.append((float(line_split[4])))
            sensor4.append((float(line_split[5])))
            powerresistor.append((float(line_split[6])))


# convert to numpy arrays for plotting
time = np.array(time)
sensor0 = np.array(sensor0)
sensor1 = np.array(sensor1)
sensor2 = np.array(sensor2)
sensor3 = np.array(sensor3)
sensor4 = np.array(sensor4)
powerresistor = np.array(powerresistor)

# print(time)
# print(sensor0)
# print("time", len(time))
# print("sensor0", len(sensor0))
# print("sensor1", len(sensor0))

plt.plot(time, sensor0, "b.", markersize = 1, label = "10mm")
plt.plot(time, sensor1, "r.", markersize = 1, label = "Sensor 1")
plt.plot(time, sensor2, "y.", markersize = 1, label = "Sensor 2")
plt.plot(time, sensor3, "m.", markersize = 1, label = "Sensor 3")
plt.plot(time, sensor4, "g.", markersize = 1, label = "Sensor 4")

plt.legend(loc = 'best')
plt.xlabel("Time (seconds)")
plt.ylabel("Temperature (Celsius)")
plt.grid(True)

plt.show()
