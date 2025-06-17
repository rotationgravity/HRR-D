
import numpy as np
import matplotlib.pyplot as plt

def z_r(r, omega0=1e-18, c=3e8):
    omega = omega0 * np.exp(-r / 1e25)
    return (1 - (omega * r / c)**2)**-0.5 - 1

r = np.linspace(1e22, 1e26, 100)
z = z_r(r)

plt.plot(r, z)
plt.xlabel("Avstånd r (m)")
plt.ylabel("Rödskift z")
plt.title("HRR-D modell: z(r)")
plt.grid()
plt.show()
