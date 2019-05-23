import matplotlib.pyplot as plt
from drawnow import drawnow
import numpy as np

sensor_0_list = []
sensor_1_list = []
sensor_2_list = []
sensor_3_list = []
sensor_4_list = []


def makeFig():
    for sensor_list in list_of_sensors:
        #print(sensor_list)
        
        plt.plot(xList,sensor_list, ".") # I think you meant this


plt.ion() # enable interactivity
fig=plt.figure() # make a figure

xList=list()
yList=list()

f = open("experiment_14_23_57.756337.txt", "r")

i = 0
for line in f:
    i += 1
    line_split = line.split("  ")

    t = line_split[0]
    s0 = line_split[1]
    s1 = line_split[2]
    s2 = line_split[3]
    s3 = line_split[4]
    s4 = line_split[5]

    sensor_0_list.append(s0)
    sensor_1_list.append(s1)
    sensor_2_list.append(s2)
    sensor_3_list.append(s3)
    sensor_4_list.append(s4)

    list_of_sensors = []

    xList.append(i)
    list_of_sensors.append(sensor_0_list)
    list_of_sensors.append(sensor_1_list)
    list_of_sensors.append(sensor_2_list)
    list_of_sensors.append(sensor_3_list)
    list_of_sensors.append(sensor_4_list)

    plt.ylim(15,75)
    drawnow(makeFig)
    #makeFig()      The drawnow(makeFig) command can be replaced
    #plt.draw()     with makeFig(); plt.draw()
    plt.pause(0.001)