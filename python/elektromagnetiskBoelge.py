import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters for the electromagnetic wave
c = 3e8  # Speed of light in m/s
frequency = 1e9  # Frequency of the wave in Hz
wavelength = c / frequency  # Wavelength in meters
k = 2 * np.pi / wavelength  # Wave number
omega = 2 * np.pi * frequency  # Angular frequency

# Spatial grid
x = np.linspace(0, 2 * wavelength, 400)

# Time array for the animation
t = np.linspace(0, 2 * np.pi, 100)

# Initialize the plot
fig, ax = plt.subplots(figsize=(10, 6))
line_e, = ax.plot([], [], 'r-', label='Electric Field')
line_b, = ax.plot([], [], 'b-', label='Magnetic Field')
ax.set_xlim(0, 2 * wavelength)
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel('Distance (m)')
ax.set_ylabel('Amplitude')
ax.set_title('Electromagnetic Wave Animation')
ax.legend(loc='upper right')

# Animation function
def update(frame):
    t_val = t[frame]
    E = np.cos(k * x - omega * t_val)  # Electric field
    B = np.cos(k * x - omega * t_val + np.pi / 2)  # Magnetic field
    line_e.set_data(x, E)
    line_b.set_data(x, B)
    return line_e, line_b

# Create the animation
ani = FuncAnimation(fig, update, frames=len(t), interval=50, blit=True)

# Save the animation as a GIF file
ani.save('electromagnetic_wave_animation.gif', writer='pillow', fps=20)

plt.show()
