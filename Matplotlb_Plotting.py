# Plotting without line
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()

# Multiple points
x = np.array([1, 2, 6, 8])
y = np.array([3, 8, 1, 10])

plt.plot(x, y)
plt.show()

# Default X-points
defaultY = np.array([3, 8, 1, 10, 5, 7])

plt.plot(defaultY)
plt.show()