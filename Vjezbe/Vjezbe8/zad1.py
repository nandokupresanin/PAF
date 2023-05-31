import numpy as np
import matplotlib.pyplot as plt
def calculate_trajectory(q, m, v0, E, B, dt, num_steps):
    positions = np.zeros((num_steps, 3))
    velocities = np.zeros((num_steps, 3))
    positions[0] = np.array([0, 0, 0])
    velocities[0] = v0
    for i in range(1, num_steps):
        F = q * (E + np.cross(velocities[i-1], B))
        a = F / m
        velocities[i] = velocities[i-1] + a * dt
        positions[i] = positions[i-1] + velocities[i] * dt
    return positions
q = -1.6e-19 
m = 9.1e-31 
v0 = np.array([1e5, 2e5, 3e5])
E = np.array([0, 0, 0])
B = np.array([0, 0, 10]) 
dt = 1e-9  
num_steps = 1000  
positions = calculate_trajectory(q, m, v0, E, B, dt, num_steps)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(positions[:, 0], positions[:, 1], positions[:, 2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Putanja čestice')
plt.show()