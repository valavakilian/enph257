# ls /dev/tty.*

import serial
from datetime import*
from pylive import live_plotter, multi_line_live_plotter
import numpy as np

output_file = "experiment_" + str(datetime.now().time()).replace(":","_") + ".txt"
port = "COM5"
rate = 9600
timeout = 1 # seconds

colors = ['blue', 'red', 'yellow', 'purple', 'green']

size = 60 * 60 * 1
# x_vec = np.linspace(0,1,size+1)[0:-1]
# s0_vec = np.repeat(75, len(x_vec))
# s1_vec = np.repeat(75, len(x_vec))
# s2_vec = np.repeat(75, len(x_vec))
# s3_vec = np.repeat(15, len(x_vec))
# s4_vec = np.repeat(15, len(x_vec))

x_vec = np.linspace(0,size, size + 1)[0:-1]
s0_vec = np.repeat(75, size)
s1_vec = np.repeat(75, size)
s2_vec = np.repeat(75, size)
s3_vec = np.repeat(15, size)
s4_vec = np.repeat(15, size)

lines = []
line0 = []
line1 = []
line2 = []
line3 = []
line4 = []
lines.append(line0)
lines.append(line1)
lines.append(line2)
lines.append(line3)
lines.append(line4)

first_time = True
time = 0

with open(output_file, 'w') as f:
    with serial.Serial(port, rate, timeout=timeout) as ser:
        while(True):
            line = ser.readline().decode()
            # print(line)
            # print(len(line))
            if (len(line) != 0):
                line = line.replace("\n","")
                full_line = str(datetime.now().time())+ "  " + line
                print(full_line)
                # print("________________")
                f.write(full_line)
                line_split = full_line.split("  ")
                # print(full_line.split("  "))
                # print("++++++++++++++++++++")

                t = line_split[0]
                s0 = line_split[1]
                s1 = line_split[2]
                s2 = line_split[3]
                s3 = line_split[4]
                s4 = line_split[5]

                # print(s0,s1,s2,s3,s4)
                # print("&&&&&&&&&&&&&&&&&&&&")


                s_vec = []
                s0_vec[-1] = float(s0)
                s_vec.append(s0_vec)
                s1_vec[-1] = float(s1)
                s_vec.append(s1_vec)
                s2_vec[-1] = float(s2)
                s_vec.append(s2_vec)
                s3_vec[-1] = float(s3)
                s_vec.append(s3_vec)
                s4_vec[-1] = float(s4)
                s_vec.append(s4_vec)


                #x_vec.append()
                lines = multi_line_live_plotter(x_vec, s_vec, colors, lines)
                # line0 = live_plotter(x_vec,s0_vec,line0)
                # line1 = live_plotter(x_vec,s1_vec,line1)
                # line2 = live_plotter(x_vec,s2_vec,line2)
                # line3 = live_plotter(x_vec,s3_vec,line3)
                # line4 = live_plotter(x_vec,s4_vec,line4)

                s0_vec = np.append(s0_vec[1:],0.0)
                s1_vec = np.append(s1_vec[1:],0.0)
                s2_vec = np.append(s2_vec[1:],0.0)
                s3_vec = np.append(s3_vec[1:],0.0)
                s4_vec = np.append(s4_vec[1:],0.0)
