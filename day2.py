import numpy as np

datapath = "data2.txt"

file1 = open(datapath, 'r')
Lines = file1.readlines()
Lines = [(line.strip("\n")) for line in Lines]

htot = 0# forward
deptot = 0# up/down
aim = 0

for line in Lines:
    length = int(line.split(" ")[1])
    if "forward" in line:
        htot = htot + length
    if "down" in line:
        deptot = deptot + length
    if "up" in line:
        deptot = deptot - length
print(deptot*htot)       
        
# Part 2
htot = 0# forward
deptot = 0# up/down
aim = 0

for line in Lines:
    length = int(line.split(" ")[1])
    if "forward" in line:
        htot = htot + length
        deptot = deptot + aim * length
    if "down" in line:
        aim = aim + length
    if "up" in line:
        aim = aim - length
print(deptot*htot)
