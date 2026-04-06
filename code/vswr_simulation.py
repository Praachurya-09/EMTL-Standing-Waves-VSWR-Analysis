import numpy as np
import matplotlib.pyplot as plt

# Distance along transmission line
z = np.linspace(0, 4*np.pi, 1000)

# Reflection coefficient
gamma = 0.6

# Incident and reflected waves
incident = np.cos(z)
reflected = gamma * np.cos(-z)

# Standing wave
standing_wave = incident + reflected

# Find Vmax and Vmin
Vmax = np.max(standing_wave)
Vmin = np.min(standing_wave)

# VSWR calculation
vswr = Vmax / abs(Vmin)

print("Vmax:", Vmax)
print("Vmin:", Vmin)
print("VSWR:", vswr)

# Plot graph
plt.figure(figsize=(10,5))
plt.plot(z, standing_wave, label="Standing Wave")

plt.axhline(Vmax, linestyle='--', label="Vmax")
plt.axhline(Vmin, linestyle='--', label="Vmin")

plt.title("Standing Wave & VSWR")
plt.xlabel("Distance")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

plt.show()
