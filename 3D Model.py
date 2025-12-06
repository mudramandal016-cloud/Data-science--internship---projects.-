import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# Define radii and distances (in arbitrary units)
planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
radii = [0.383, 0.949, 1.0, 0.532, 11.21, 9.45, 4.01, 3.88]
distances = [0.39, 0.72, 1.0, 1.52, 5.2, 9.58, 19.22, 30.05]
colors = ['gray', 'yellow', 'blue', 'red', 'orange', 'goldenrod', 'lightblue', 'blue']
# Create a figure and 3D axis
fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(111, projection='3d')

# Plot the Sun
ax.scatter(0, 0, 0, color='yellow', s=500, label='Sun')

# Plot the planets
for i in range(len(planet_names)):
    # Calculate positions
    x = distances[i] * np.cos(np.linspace(0, 2 * np.pi, 100))
    y = distances[i] * np.sin(np.linspace(0, 2 * np.pi, 100))
    z = np.zeros(100)
    
    # Plot orbit
    ax.plot(x, y, z, color='gray', linestyle='--')
    
    # Plot planet
    ax.scatter(distances[i], 0, 0, color=colors[i], s=100 * radii[i], label=planet_names[i])

# Set labels and title
ax.set_xlabel('X (AU)')
ax.set_ylabel('Y (AU)')
ax.set_zlabel('Z (AU)')
ax.set_title('3D Solar System Model')
ax.legend()

plt.show()