# importing packages
import matplotlib.pyplot as plt
import numpy as np

# Create data for DC plot
x1 = [0, 3, 3, 4, 5, 7, 10, 13, 13, 15, 15]
y1 = [1, 1, 0, 0, 1, 1, 0,  0,  1,  1,  0]
x1a = [0, 15]
y1a = [-1, -1]
# Create AC Plot
x2 = np.arange(0, 6, 0.001)
y2 = np.sin(x2 * np.pi * 2)

# Create graph
fig, axs = plt.subplots(2, layout="constrained")
axs[0].plot(x1, y1)
axs[0].plot(x1a, y1a)
axs[0].set_title("Direct Current, D.C.")
axs[1].plot(x2,y2)
axs[1].set_title("Alternating Current, A.C.")
#fig.tight_layout()

#axs[0].set_title('Figire 3.1 - D.C. Vs. A.C.')
plt.xlabel("Time")
plt.ylabel("Magnitude & Direction")
plt.savefig('/home/gary/Documents/notes/ARRL/img/3/figure-3_1.png')
