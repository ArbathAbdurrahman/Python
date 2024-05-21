import numpy as np
import matplotlib.pyplot as plt

# Parameter sistem massa-pegas
m = 1.0  # massa (kg)
k = 1.0  # konstanta pegas (N/m)
A = 1.0  # amplitudo getaran (m)
phi = 0.0  # fase awal (rad)
t_max = 10.0  # waktu maksimum untuk simulasi (detik)
dt = 0.01  # interval waktu (detik)

# Frekuensi sudut
omega = np.sqrt(k / m)

# Waktu
t = np.arange(0, t_max, dt)

# Posisi sebagai fungsi waktu
x = A * np.cos(omega * t + phi)

# Visualisasi hasil
plt.figure(figsize=(10, 5))
plt.plot(t, x, label='x(t) = A cos(ωt + φ)')
plt.title('Gerak Harmonik Sederhana')
plt.xlabel('Waktu (s)')
plt.ylabel('Posisi (m)')
plt.legend()
plt.grid(True)
plt.show()
