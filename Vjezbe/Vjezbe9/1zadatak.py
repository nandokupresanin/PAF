import matplotlib.pyplot as plt
MS = 1.989e30
MZ = 5.9742e24
G = 6.67408e-11
AU = 1.486e11 
year = 365.242 * 24 * 3600
x0 = AU
y0 = 0 
vx0 = 0
vy0 = 29783
dt = 3600
t_start = 0
t_end =year
t_list = []
x_list = []
y_list = []
t = t_start
x = x0
y = y0
vx = vx0
vy = vy0
while t <= t_end:
    t_list.append(t)
    x_list.append(x)
    y_list.append(y)
    r = (x ** 2 + y ** 2) ** 0.5
    ax = -G * MS * x / r ** 3
    ay = -G * MS * y / r ** 3
    vx += ax * dt
    vy += ay * dt
    x += vx * dt
    y += vy * dt
    t += dt
plt.figure(figsize=(8, 6))
plt.plot(x_list, y_list)
plt.plot(0, 0, 'ro')
plt.plot(x0, y0, 'bo')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.title('Putanja Zemlje oko Sunca')
plt.axis('equal')
plt.show()
    
