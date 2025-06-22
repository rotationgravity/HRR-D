# hrrd_apophis_simulering.py
# Simulerar Apophis bana med HRR-D justeringar (förenklad version)

import numpy as np
import matplotlib.pyplot as plt

# HRR-D inspirerad spiralrörelse
def hrrd_spiral(t, r0=1.0, omega=1e-18):
    r = r0 * np.exp(-omega * t)
    theta = omega * t
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

t = np.linspace(0, 1e7, 1000)
x, y = hrrd_spiral(t)

plt.plot(x, y)
plt.title("HRR-D spiral trajectory (Apophis)")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis("equal")
plt.grid(True)
plt.savefig("apophis_trajectory.png")
plt.show()
