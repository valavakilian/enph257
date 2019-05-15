# ls /dev/tty.*

import serial

output_file = "enph257pretest1.txt"
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
                print(line.replace("\n",""))
                f.write(line)
