import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Define the 2D Gaussian function
def gaussian_2d(x, y, mux, muy, sigmax, sigmay, rho):
    Z = np.exp(-((x - mux)**2 / sigmax**2 + (y - muy)**2 / sigmay**2 - 2*rho*(x - mux)*(y - muy)/(sigmax*sigmay))/(2*(1 - rho**2)))
    return Z / (2 * np.pi * sigmax * sigmay * np.sqrt(1 - rho**2))

# Create a checkerboard pattern
def checkerboard(x, y, size=10):
    return (np.floor(x*size) % 2 == np.floor(y*size) % 2).astype(float)

def angle_from_center(x, y, center_x, center_y):
    return np.arctan2(y - center_y, x - center_x)

def make_lighter_cmap(cmap, alpha_factor=0.5, rgb_shift=0.1):
    """Make a colormap lighter by adjusting its alpha channel and adding a constant to RGB channels."""
    colors = []
    for i in range(cmap.N):
        rgba = list(cmap(i))
        
        # Adjust the RGB channels by adding a constant
        for j in range(3):
            rgba[j] = min(1, max(0, rgba[j] + rgb_shift))  # Ensure the value is between 0 and 1
        
        rgba[3] *= alpha_factor  # Adjust the alpha channel
        colors.append(tuple(rgba))
    return ListedColormap(colors)


# Parameters for the Gaussian
mux, muy = 2.5, 2.5
sigmax, sigmay = 1, 1
rho = 0

# Generate grid of x, y values
x = np.linspace(0, 5, 100)
y = np.linspace(0, 5, 100)
X, Y = np.meshgrid(x, y)

# Calculate the Gaussian values
Z = gaussian_2d(X, Y, mux, muy, sigmax, sigmay, rho)

# Get the checkerboard pattern
pattern = checkerboard(X, Y, size=5)


# Create checkerboard pattern colormap
colors = np.zeros((X.shape[0], X.shape[1], 4))  # Initialize a RGBA array
colors[pattern == 0] = [0, 0, 0, 1]  # black with alpha=1
colors[pattern == 1] = [1, 1, 1, 1]  # white with alpha=1


# Create checkerboard pattern colormap with circular gradient
angle_map = angle_from_center(X, Y, mux, muy)
norm_angles = (angle_map + np.pi) / (2 * np.pi)  # Normalize angles between 0 and 1

# Get the colormap from matplotlib
cmap = plt.get_cmap('Spectral')  # You can use other colormaps like 'viridis', 'plasma', etc.
lighter_cmap = make_lighter_cmap(cmap, alpha_factor=0.9, rgb_shift=0.2)

colors = lighter_cmap(norm_angles)  # Convert normalized angles to colors using colormap
colors[pattern == 0, :3] = 0  # Set the RGB channels of black pattern to 0
colors[pattern == 0, 3] = 1  # Set the alpha channel of black pattern to 1


# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Adjusting the axis labels and title position
ax.set_zlabel('Z axis', labelpad=0)

ax.set_title('3D Gaussian Distribution')

# Use plot_surface to display the Gaussian with the checkerboard pattern
surf = ax.plot_surface(X, Y, Z, facecolors=colors, rstride=1, cstride=1, linewidth=0, antialiased=False, shade=False)


# Adjusting the ticks positions
ax.set_xticks(np.linspace(0, 5, 6))
ax.set_yticks(np.linspace(0, 5, 6))
ax.set_zticks([0, 0.1, 0.2])

ax.set_xlim([0,5])
ax.set_ylim([0,5])
ax.set_zlim([0,0.2])


ax.text(2.5, 5, 0.24, 'X axis', rotation=30, rotation_mode='anchor', ha='center', va='center')
ax.text(0, 2.5, 0.24, 'Y axis', rotation=30, rotation_mode='anchor', ha='center', va='center')

x_line = np.array([0, 5])
y_line = np.array([5, 5])
z_line = np.array([0.2, 0.2])
ax.plot(x_line, y_line, z_line, color='black', linewidth=2)

x_line = np.array([0, 0])
y_line = np.array([5, 0])
z_line = np.array([0.2, 0.2])
ax.plot(x_line, y_line, z_line, color='black', linewidth=2)

x_line = np.array([0, 0])
y_line = np.array([5, 5])
z_line = np.array([0.2, 0])
ax.plot(x_line, y_line, z_line, color='black', linewidth=2)

x_line = np.array([0, 0])
y_line = np.array([0, 0])
z_line = np.array([0.2, 0])
ax.plot(x_line, y_line, z_line, color='black', linewidth=2)

x_line = np.array([5, 5])
y_line = np.array([5, 5])
z_line = np.array([0.2, 0])
ax.plot(x_line, y_line, z_line, color='black', linewidth=2)

# ax.grid(False)
plt.tight_layout()
plt.savefig("lab06_D_bonus.png")
plt.show()
