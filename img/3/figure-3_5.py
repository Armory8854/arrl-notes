# Import those libs
import matplotlib.pyplot as plt
import numpy as np

# Plot those arrays
## Graph A
y1 = np.array([50, 25, 25])
myLabelsY1 = ["E", "I", "R"]

## Graph B - Specifically just the labels
y2 = np.array([50, 25, 25])
myLabelsY2 = ["P", "I", "E"]

# Plot graph
fig, axs = plt.subplots(2, layout="constrained")
axs[0].pie(y1, labels = myLabelsY1)
axs[1].pie(y2, labels = myLabelsY2)
plt.savefig('/home/gary/Documents/notes/ARRL/img/3/figure-3_5.png')
