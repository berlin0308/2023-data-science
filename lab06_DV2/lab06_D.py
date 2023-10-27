import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Define the 2D Gaussian function
def gaussian_2d(x, y, mux, muy, sigmax, sigmay, rho):
    Z = np.exp(-((x - mux)**2 / sigmax**2 + (y - muy)**2 / sigmay**2 - 2*rho*(x - mux)*(y - muy)/(sigmax*sigmay))/(2*(1 - rho**2)))
    return Z / (2 * np.pi * sigmax * sigmay * np.sqrt(1 - rho**2))

# Parameters for the Gaussian
mux, muy = 2.5, 2.5
sigmax, sigmay = 1, 1
rho = 0

# Generate grid of x, y values
x = np.linspace(0, 5, 100)
y = np.linspace(0, 5, 100)
x, y = np.meshgrid(x, y)

# Calculate the Gaussian values
z = gaussian_2d(x, y, mux, muy, sigmax, sigmay, rho)

# Plotting
fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap=cm.viridis)

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_zlim([0, 0.16])
ax.set_zticks([x / 100.0 for x in range(2, 16, 2)])
ax.set_title('3D Gaussian Distribution')

plt.savefig("lab06_D_result.png")
plt.show()
