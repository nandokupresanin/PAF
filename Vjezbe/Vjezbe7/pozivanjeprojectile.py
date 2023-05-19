import projectile as pro
import numpy as np
x0 = 0
y0 = 0
v0 = 50
theta = np.radians(45)
dt = 0.01
mass = 0.5
ro=1.293
C=0.2
A=0.1
drag_coefficient = ro*C*A

projectile = pro.Projectile(x0, y0, v0, theta, dt, mass, drag_coefficient)
projectiler=pro.Projectile(x0, y0, v0, theta, dt, mass, drag_coefficient)
projectile.simulate()
projectiler.rungekutta()
projectile.plot_trajectory()
projectiler.plot_trajectory()