import numpy as np

datapath = "1st.txt"

file1 = open(datapath, 'r')
Lines = file1.readlines()
Lines = np.array([int(line.strip("\n")) for line in Lines])

# part 1
print(np.sum(np.roll(Lines,-1) - Lines > 0))

# part 2
moving_avgs = [a+b+c for (a,b,c) in list(zip(Lines,np.roll(Lines,-1),np.roll(Lines,-2)))]
print(np.sum((np.roll(moving_avgs,-1) - moving_avgs) > 0))
