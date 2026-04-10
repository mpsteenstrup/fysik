import numpy as np
import matplotlib.pyplot as plt

# Konstanter
R_jord = 6371  # Jordens radius i km
phi_deg = 55   # Breddegrad for Danmark/København
phi_rad = np.deg2rad(phi_deg)

# Opret 3D-figur
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 1. Lav selve Jordkuglen (transparent)
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = R_jord * np.outer(np.cos(u), np.sin(v))
y = R_jord * np.outer(np.sin(u), np.sin(v))
z = R_jord * np.outer(np.ones(np.size(u)), np.cos(v))

ax.plot_surface(x, y, z, color='cyan', alpha=0.1, linewidth=0)

# 2. Lav den 55. breddegrad (den røde cirkel)
# Radius i den lille cirkel er R * cos(phi)
r_bredde = R_jord * np.cos(phi_rad)
z_bredde = R_jord * np.sin(phi_rad)

theta = np.linspace(0, 2 * np.pi, 100)
x_cirkel = r_bredde * np.cos(theta)
y_cirkel = r_bredde * np.sin(theta)
z_cirkel = np.full_like(x_cirkel, z_bredde)

ax.plot(x_cirkel, y_cirkel, z_cirkel, color='red', linewidth=2.5, label=f'{phi_deg}° nordlig breddegrad')

# 3. Linjestykke fra centrum til et punkt på 55. breddegrad
ax.plot([0, r_bredde], [0, 0], [0, z_bredde], color='black', linewidth=2, marker='o', label='Radiusvektor (R)')
ax.plot([0, r_bredde], [0, 0], [z_bredde, z_bredde], '--', color='gray', alpha=0.5, label='Radius i cirkel (R * cos(φ))')

# Formatering af grafen
ax.set_title(f'Visualisering af Jorden og {phi_deg}. breddegrad', fontsize=14)
ax.set_xlabel('km')
ax.set_ylabel('km')
ax.set_zlabel('km')
ax.legend(loc='upper left')

# Sørg for at proportionerne er ens (så Jorden ligner en kugle)
limit = R_jord + 500
ax.set_xlim(-limit, limit)
ax.set_ylim(-limit, limit)
ax.set_zlim(-limit, limit)

plt.show()