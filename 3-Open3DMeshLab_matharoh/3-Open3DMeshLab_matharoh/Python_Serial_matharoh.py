# Name - Harsahib Matharoo
# Student ID - 400185871
# Python version: 3.8.3

# the starting step of serial communication
import serial
import math
#   Currently set COM3 as serial port at 115.2kbps 8N1
# using the third port in this case here

s = serial.Serial("COM3", 115200)
print("Opening: " + s.name)
f = open("ToFdata4.txt", "a")
g = open("ToFdata4.xyz", "a")

s.write(b'1')     #This program will send a '1' or 0x31 

count = 0

# 320 because 32 measurements every full 360 degree rotation times 10

# since the angle was selected to be 11.25 degrees
for i in range (320):
         a = s.readline()
         conv = a.decode()
         f.write(conv)
         g.write(conv)
         print(conv)
        

print("Closing: " + s.name)
s.close()
f.close()
g.close()
