
import numpy as np
import matplotlib.pyplot as plt

# Konstanter
c = 3e8  # ljusets hastighet [m/s]
omega_0 = 1e-12  # grundläggande spiralrotation [rad/s]
r_c = 1e24       # dämpningsradie [m]
num_varv = 200   # antal spiralvarv
segment_r = 5e23  # längd per spiralvarv [m]

# Skapa avstånd för varje spiralvarv
r_values = np.linspace(segment_r, segment_r * num_varv, num_varv)

# Räkna ut (1 + z_i) för varje spiralsegment
z_factors = []
for r in r_values:
    omega = omega_0 * np.exp(-r / r_c)
    val = 1 - (omega * r / c)**2
    if val > 0:
        z_i = 1 / np.sqrt(val) - 1
        z_factors.append(1 + z_i)

# Total ackumulerad rödskift
z_total = np.prod(z_factors) - 1

# Tidsdilatation vid slutpunkten
omega_end = omega_0 * np.exp(-r_values[-1] / r_c)
HRRD_dilation = 1 / np.sqrt(1 - (omega_end * r_values[-1] / c)**2)

# Utskrift
print(f"Ackumulerad rödskift z_total = {z_total:.4f}")
print(f"Tidsdilatation (dτ/dt) vid slutpunkten = {HRRD_dilation:.4f}")
print(f"Motsvarar (1+z) i standardmodell: {1 + z_total:.4f}")

# Plott: z_total som funktion av antal varv
z_progress = []
running_product = 1
for zf in z_factors:
    running_product *= zf
    z_progress.append(running_product - 1)

plt.figure(figsize=(8, 5))
plt.plot(range(1, num_varv + 1), z_progress, label='Ackumulerat z i HRR-D')
plt.axhline(6.5, color='red', linestyle='--', label='z = 6.5 (observationsmål)')
plt.xlabel('Antal spiralvarv')
plt.ylabel('z_total')
plt.title('Rödskift som funktion av spiralstackning i HRR-D')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
