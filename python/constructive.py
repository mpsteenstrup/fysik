import numpy as np
import matplotlib.pyplot as plt

# Define the time range
t = np.linspace(0, 6*2 * np.pi, 2000)

# Define two sine waves
wave1 = np.sin(t)+1
wave2 = np.sin(t)-1

# Sum of the two waves (constructive interference)
constructive_interference = wave1 + wave2

plt.plot(t,wave1)
plt.plot(t,wave2)
plt.plot(t,constructive_interference)
plt.show()

# Plot the two sine waves
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, wave1, label='Wave 1')
plt.plot(t, wave2, label='Wave 2')
plt.title('Two Sine Waves')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()

# Plot the sum of the two waves
plt.subplot(3, 1, 2)
plt.plot(t, constructive_interference, label='Constructive Interference', color='purple')
plt.title('Constructive Interference')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()

# Detailed view of the constructive interference
plt.subplot(3, 1, 3)
plt.plot(t, constructive_interference, label='Constructive Interference', color='purple')
plt.title('Detailed View of Constructive Interference')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.xlim(0, 2 * np.pi)
plt.ylim(-2, 2)
plt.legend()

plt.tight_layout()
plt.show()