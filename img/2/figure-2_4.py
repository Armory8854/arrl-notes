# importing package
import matplotlib.pyplot as plt
import numpy as np

# Create data
## 570 kHz Line
x1 = [540, 570, 600]
y1 = [0, 50, 0]

## 800 kHz Line
x2 = [770, 800, 830]
y2 = [0, 75, 0]

## 1000 kHz Line
x3 = [970, 1000, 1030]
y3 = [0, 60, 0]

## 1310 kHz Line
x4 = [1280, 1310, 1340]
y4 = [0, 30, 0]

# plot lines
plt.plot(x1, y1)
plt.ylim([0, 100])
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)

# Set Labels
plt.title("Figure 2.4 - How A Receiver Sees The Radio Spectrum")
plt.xlabel("AM Band Frequency in kHz")
plt.ylabel("Signal Strength")

plt.savefig('/home/gary/Documents/notes/ARRL/img/2/figure-2_4.png')
