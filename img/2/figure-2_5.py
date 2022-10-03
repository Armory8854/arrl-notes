# importing package
import matplotlib.pyplot as plt
import numpy as np

# Create data
x1 = np.arange(0, 4, 0.05)
y1 = np.sin(x1*np.pi)

x2 = (1.5, 3.5)
y2 = (-1, -1)

# Create Markers
markers_on = 8
plt.plot(x1, y1, label='Markers signify lambda')
plt.plot(x2, y2)

# Set Labels
plt.title("Figure 2.5 - Visualizing Lambda")
plt.xlabel("Distance")
plt.ylabel("Frequency")
plt.savefig('/home/gary/Documents/notes/ARRL/img/2/figure-2_5.png')
