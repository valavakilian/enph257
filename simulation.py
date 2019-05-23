import numpy as np
from numpy import pi
import matplotlib.pyplot as mpl
from datetime import*

# This seeks to find the temperature over time of an aluminum rod subject to certain thermal conditions

output_file = "simulation_" + str(datetime.now().time()).replace(":","_") + ".txt"

# this is where constants are. Temperatures given are in Celsius, while length measurements are in meters.
tempAmbient = 293.15 #ambient temperature, K
power = 4.5 #thermal power, W
rodLength = 0.3 #rod length, m
rodRadius = 0.01 #rod radius, m
deltax = 0.005 #slice length, m
deltat = 0.01 #time between iterations, s
emissivity = 1 #emissivity, dimensionless

stfb = 5.67 * (10 ** (-8))

#intrinsic properties
thermalCond = 205.0 #thermal conductivity of aluminum, W/(mK)
density = 2700.0 #density, kg/m^3
specificHeat = 902.0 #specific heat, J/(kgK)
emissivity = 1.0 #emissivity, dimensionless
chtCoeff = 12.0 #convective heat transfer coefficient, W/(m^2K)

# this code creates a numpy array with the initial temperature
temp = np.repeat(tempAmbient, rodLength/deltax)
tempprev = temp

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

# iterates until the temperature distribution has reached themral equilibrium, as found by the L2 norm of dT.
with open(output_file, 'w') as f:
    while(runcounter < 3600):
        runcounter = runcounter + deltat
        tempprev = temp
        temp = nextTemp(deltat, temp, deltax, power)
        time.append(runcounter)
        t1.append(temp[int(.01/deltax)])
        t2.append(temp[int(.08/deltax)])
        t3.append(temp[int(.15/deltax)])
        t4.append(temp[int(.22/deltax)])
        t5.append(temp[int(.29/deltax)])
        f.write(str(runcounter) + "  " + str(temp[int(.01/deltax)]) + "  " + str(temp[int(.08/deltax)]) + "  " + str(temp[int(.15/deltax)]) + "  " + str(temp[int(.22/deltax)]) + "  " + str(temp[int(.29/deltax)]) + "\n")
        if(int(runcounter/960) % 2 is 1):
            power = 0.0
        else:
            power = 4.5

ktoc = np.repeat(273.15, len(time))
t1 = t1 - ktoc
t2 = t2 - ktoc
t3 = t3 - ktoc
t4 = t4 - ktoc
t5 = t5 - ktoc
mpl.plot(time, t1, 'b', time, t2, 'r', time, t3, 'y', time, t4, 'm', time, t5, 'g')
mpl.grid(True)
mpl.ylabel('Temperature, T (K)')
mpl.xlabel('time, t (s)')
mpl.show()
