import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from datetime import datetime

data_file = "experiment_14_23_57.756337.txt"
simulation_file = "simulation_16_25_21.966117.txt"

# arrays for each sensor and one for time
# each sensor shares the same timestamp

# data
ds0 = []
ds1 = []
ds2 = []
ds3 = []
ds4 = []
dstime = []

# data
ss0 = []
ss1 = []
ss2 = []
ss3 = []
ss4 = []
sstime = []

initial_time = -1

with open(data_file,'r') as f:
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

            dstime.append(float(seconds-initial_time))
            ds0.append((float(line_split[1])))
            ds1.append((float(line_split[2])))
            ds2.append((float(line_split[3])))
            ds3.append((float(line_split[4])))
            ds4.append((float(line_split[5])))

# convert to numpy arrays for plotting
dstime = np.array(dstime)
ds0 = np.array(ds0)
ds1 = np.array(ds1)
ds2 = np.array(ds2)
ds3 = np.array(ds3)
ds4 = np.array(ds4)

with open(simulation_file,'r') as g:
    for line in g:
        if(line[0] is not ';'):
            line_split = line.split('  ')
            if (len(line_split) != 6):
                continue

            sstime.append(float(line_split[0]))
            ss0.append((float(line_split[1]))-273.15)
            ss1.append((float(line_split[2]))-273.15)
            ss2.append((float(line_split[3]))-273.15)
            ss3.append((float(line_split[4]))-273.15)
            ss4.append((float(line_split[5]))-273.15)

# convert to numpy arrays for plotting
sstime = np.array(sstime)
ss0 = np.array(ss0)
ss1 = np.array(ss1)
ss2 = np.array(ss2)
ss3 = np.array(ss3)
ss4 = np.array(ss4)


plt.plot(dstime, ds0, "b.", markersize = 1, label = "Data Sensor 0")
plt.plot(dstime, ds1, "r.", markersize = 1, label = "Data Sensor 1")
plt.plot(dstime, ds2, "y.", markersize = 1, label = "Data Sensor 2")
plt.plot(dstime, ds3, "m.", markersize = 1, label = "Data Sensor 3")
plt.plot(dstime, ds4, "g.", markersize = 1, label = "Data Sensor 4")

plt.plot(sstime, ss0, "b", label = "Simulation Sensor 0")
plt.plot(sstime, ss1, "r", label = "Simulation Sensor 1")
plt.plot(sstime, ss2, "y", label = "Simulation Sensor 2")
plt.plot(sstime, ss3, "m", label = "Simulation Sensor 3")
plt.plot(sstime, ss4, "g", label = "Simulation Sensor 4")

plt.legend(loc = 'best')
plt.xlabel("Time (seconds)")
plt.ylabel("Temperature (Celsius)")
plt.grid(True)

plt.show()
