import matplotlib.pyplot as plt
import numpy as np

x = np.arange(19,486,27)
y = np.sin(1/x)*25

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('A single plot')

plt.grid(True)

plt.show()
