import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0, 10, 1)
y = np.arange(0, 10, 1)
z = plt.plot(x, y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("X VS Y")
print(z)
