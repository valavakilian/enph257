import numpy as np
from numpy import pi
import matplotlib.pyplot as mpl
from datetime import*
import tqdm
from tqdm import *
from scipy.optimize import curve_fit


def func( x, emissivity, chtCoeff, power_val, specificHeat):
    time_data_length = 3600 / 3676 / 10
    time, x, t2, t3, t4 ,t5 = simulate(emissivity, chtCoeff, power, specificHeat, len(ds0))
    return x

def simulate(emissivity, chtCoeff, power_val, specificHeat, time_data_length):
    # This seeks to find the temperature over time of an aluminum rod subject to certain thermal conditions

    #output_file = "simulation_" + str(datetime.now().time()).replace(":","_") + ".txt"

    # this is where constants are. Temperatures given are in Celsius, while length measurements are in meters.
    tempAmbient = 295.15 #ambient temperature, K
    power = power_val #thermal power, W
    rodLength = 0.3 #rod length, m
    rodRadius = 0.01 #rod radius, m
    deltax = 0.005 #slice length, m
    deltat = 3600 / time_data_length / 10 #time between iterations, s

    #print(int(3600 / deltat))
    #emissivity = 0 #emissivity, dimensionless
    tempStart = 273 + 23.24 #initial temperature, K

    stfb = 5.67 * (10 ** (-8))

    #intrinsic properties
    #thermalCond = 205.0 #thermal conductivity of aluminum, W/(mK)
    density = 2700.0 #density, kg/m^3
    specificHeat = 902.0 #specific heat, J/(kgK)
    #emissivity = 0.1 #emissivity, dimensionless
    #chtCoeff = 12.0 #convective heat transfer coefficient, W/(m^2K)
    onOff = 10.2

    # this code creates a numpy array with the initial temperature
    temp = np.repeat(tempStart, rodLength/deltax)
    tempprev = temp

    # input(emissivity)
    # input(chtCoeff)
    # input(power)
    # input(specificHeat)



    # this function calculates the next iteration of temperature
    def nextTemp(dt, temp, dx, power):
        temptemp = np.repeat(tempAmbient, rodLength/dx)
        temptemp[0] = temp[0] - dt * thermalCond*(temp[0]-temp[1])/(specificHeat*density*deltax**2) + (power - (2 * pi * rodRadius * dx + pi * rodRadius ** 2)* (chtCoeff*(temp[0] - tempAmbient) + emissivity * stfb * (temp[0]**4 - tempAmbient**4)))*dt/ (specificHeat * density * pi * rodRadius ** 2 * dx)

        for i in range(1, len(temp)-1):
            # Second derivative approximation, multiplied by k/cp
            temptemp[i] = temp[i]  + dt * (thermalCond / (specificHeat*density) * (temp[i - 1] - 2 * temp[i] + temp[i + 1]) / (deltax ** 2))

        temptemp[-1] = temp[-1] + dt * thermalCond * (temp[-2] - temp[-1])/(specificHeat * density * deltax ** 2) - (2 * pi * rodRadius * dx + pi * rodRadius ** 2) *dt * (chtCoeff * (temp[-1] - tempAmbient) + emissivity * stfb * ((temp[-1]) ** 4 - (tempAmbient) ** 4)) / (specificHeat * density * rodRadius ** 2 * dx * pi)

        for i in range(1, len(temp) - 1):
            temptemp[i] = temptemp[i] - 2 * dt * (chtCoeff * (temp[i] - tempAmbient) + emissivity * stfb * ((temp[i]) ** 4 - (tempAmbient) ** 4)) / (specificHeat * density * rodRadius)

        return temptemp

    # runcounter indicates the time elapsed

    runcounter = 0
    time = [0]
    t1 = [temp[int(.01/deltax)]]
    t2 = [temp[int(.08/deltax)]]
    t3 = [temp[int(.15/deltax)]]
    t4 = [temp[int(.22/deltax)]]
    t5 = [temp[int(.29/deltax)]]

    #pbar = tqdm( total = 3600 / deltat) 


    # iterates until the temperature distribution has reached themral equilibrium, as found by the L2 norm of dT.
    #with open(output_file, 'w') as f:
    k = 0
    while(runcounter < 3600):
        runcounter = runcounter + deltat
        k += 1
        tempprev = temp
        temp = nextTemp(deltat, temp, deltax, power)
        time.append(runcounter)
        t1.append(temp[int(.01/deltax)])
        t2.append(temp[int(.08/deltax)])
        t3.append(temp[int(.16/deltax)])
        t4.append(temp[int(.22/deltax)])
        t5.append(temp[int(.29/deltax)])
        #f.write(str(runcounter) + "  " + str(temp[int(.01/deltax)]) + "  " + str(temp[int(.08/deltax)]) + "  " + str(temp[int(.15/deltax)]) + "  " + str(temp[int(.22/deltax)]) + "  " + str(temp[int(.29/deltax)]) + "\n")
        if(int(runcounter/(60 * onOff)) % 2 is 1):
            power = 0.0
        else:
            power = power_val

        #pbar.update(1)

    #print(k)
    #print("__________________________________")

    ktoc = np.repeat(273.15, len(time))
    t1 = t1 - ktoc
    t2 = t2 - ktoc
    t3 = t3 - ktoc
    t4 = t4 - ktoc
    t5 = t5 - ktoc

    return time, t1, t2, t3, t4 ,t5


#################################################################
# From here we plot the data 


data_file = "Horizontal_experiment_16_00_45.539108.txt"


# arrays for each sensor and one for time
# each sensor shares the same timestamp

# data
ds0 = []
ds1 = []
ds2 = []
ds3 = []
ds4 = []
dstime = []

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

# convert to numpy arrays for plotting


# mpl.plot(dstime, ds0, "b.", markersize = 1, label = "Data Sensor 0")
# mpl.plot(dstime, ds1, "r.", markersize = 1, label = "Data Sensor 1")
# mpl.plot(dstime, ds2, "y.", markersize = 1, label = "Data Sensor 2")
# mpl.plot(dstime, ds3, "m.", markersize = 1, label = "Data Sensor 3")
# mpl.plot(dstime, ds4, "g.", markersize = 1, label = "Data Sensor 4")

# mpl.grid(True)
#################################################################



emissivity = 0.135
chtCoeff = 8.75
power = 6.05
specificHeat = 902.0
thermalCond = 205.0

# time, t1, t2, t3, t4 ,t5 = simulate(emissivity, chtCoeff, power, specificHeat, len(ds0))

# print(len(t1), len(ds0), len(time))

# t1 = [t1[index] for index in range(0, 10 * len(ds0) - 1) if index % 10 == 0]
# t2 = [t2[index] for index in range(0, 10 * len(ds0) - 1) if index % 10 == 0]
# t3 = [t3[index] for index in range(0, 10 * len(ds0) - 1) if index % 10 == 0]
# t4 = [t4[index] for index in range(0, 10 * len(ds0) - 1) if index % 10 == 0]
# t5 = [t5[index] for index in range(0, 10 * len(ds0) - 1) if index % 10 == 0]

# time = [time[index] for index in range(0, len(time) - 1) if index % 10 == 0]

# print(len(t1), len(ds0), len(time))


# mpl.plot(time, t1, 'b', time, t2, 'r', time, t3, 'y', time, t4, 'm', time, t5, 'g')
# mpl.grid(True)
# mpl.ylabel('Temperature, T (K)')
# mpl.xlabel('time, t (s)')
# mpl.show()

t1 = np.repeat(273 + 23.24, 3676)
print(len(t1))
print(len(ds0))
popt, pcov = curve_fit(func, t1, ds0)