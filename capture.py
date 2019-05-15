# ls /dev/tty.*

import serial
from datetime import*

output_file = "enph257pretest2.txt"
port = "COM6"
rate = 9600
timeout = 1 # seconds

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
