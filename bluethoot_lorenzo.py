
import serial
import numpy as np
import sys
import ctypes
def convert(int):
    b = 0
    for i in range(0, 10, 1):
        bit = int & 1 << i
        if not bit:
            b = b | (1 << i)
    b = b+1
    int = b * -1
    return int


header = 160
tail = 192
byte_to_receiv = 194
serialPort = serial.Serial(port = "COM9", baudrate=115200,
                           bytesize=8, timeout=None, stopbits=serial.STOPBITS_ONE)
serial = []
acc_vect = []
X = []
Y = []
Z = []
while(1):

    if(serialPort.in_waiting > 0):

        serial = serialPort.read(194)
        #print(serial)
        byte =[]

        if (serial[0] == header and serial[193] == tail and len(serial) == byte_to_receiv):
            print("new valid set of data")
            byte = [serial[i:i + 2] for i in range(1, len(serial) - 2, 2)]
            #print(byte)
        else:
            print("condition not satisfied")

        vect = []

        for value in byte:
            sign = value[1] & 0b10000000
            a = (value[0] | value[1] << 8) >> 6
            if sign:
                a = convert(a)
            vect.append(a)

        for i in range (0,len(vect),3):
            X.append(vect[i])
            Y.append(vect[i+1])
            Z.append(vect[i+2])

        acc_vect.append(vect)
        # Print the contents of the serial data
        l = len(Z)
        print(Z[l-3:l])
        print(l)

