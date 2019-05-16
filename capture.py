# ls /dev/tty.*

import serial
from datetime import*
from pylive import live_plotter
import numpy as np

output_file = "enph257pretest2.txt"
port = "COM5"
rate = 9600
timeout = 1 # seconds

size = 100
x_vec = np.linspace(0,1,size+1)[0:-1]
s0_vec = np.repeat(0.1, len(x_vec))
s1_vec = np.repeat(0.1, len(x_vec))
s2_vec = np.repeat(0.1, len(x_vec))
s3_vec = np.repeat(0.1, len(x_vec))
s4_vec = np.repeat(0.1, len(x_vec))

line0 = []
line1 = []
line2 = []
line3 = []
line4 = []

with open(output_file, 'w') as f:
    with serial.Serial(port, rate, timeout=timeout) as ser:
        while(True):
            line = ser.readline().decode()
            # print(line)
            # print(len(line))
            if (len(line) != 0):
                line = line.replace("\n","")
                full_line = str(datetime.now().time())+"  "+line+"\n"
                print(full_line)
                f.write(full_line)

                t = line.split("  ")[0]
                s0 = line.split("  ")[1]
                s1 = line.split("  ")[2]
                s2 = line.split("  ")[3]
                s3 = line.split("  ")[4]
                s4 = line.split("  ")[5]

                s0_vec[-1] = float(s0)
                s1_vec[-1] = float(s1)
                s2_vec[-1] = float(s2)
                s3_vec[-1] = float(s3)
                s4_vec[-1] = float(s4)

                line0 = live_plotter(x_vec,s0_vec,line0)
                line1 = live_plotter(x_vec,s1_vec,line1)
                line2 = live_plotter(x_vec,s2_vec,line2)
                line3 = live_plotter(x_vec,s3_vec,line3)
                line4 = live_plotter(x_vec,s4_vec,line4)

                s0_vec = np.append(s0_vec[1:],0.0)
                s1_vec = np.append(s1_vec[1:],0.0)
                s2_vec = np.append(s2_vec[1:],0.0)
                s3_vec = np.append(s3_vec[1:],0.0)
                s4_vec = np.append(s4_vec[1:],0.0)
                

