import matplotlib.pyplot as plt

# Konstante
G = 6.67408e-11
MS = 1.989e30
MZ = 5.9742e24
AU = 1.486e11
v_perpendicular = 29783
num_steps = 365  # Broj koraka simulacije (100 godina)

# Inicijalni uvjeti
x_sun = [0]  # Početna x-koordinata Sunca
y_sun = [0]  # Početna y-koordinata Sunca
x_earth = [AU]  # Početna x-koordinata Zemlje
y_earth = [0]  # Početna y-koordinata Zemlje

dt = 365.242 * 24 * 60 * 60 / num_steps  # Vremenski korak (sekunde)

# Simulacija
for _ in range(num_steps):
    # Izračunaj udaljenosti između čestica
    dx = x_earth[-1] - x_sun[-1]
    dy = y_earth[-1] - y_sun[-1]
    r = (dx ** 2 + dy ** 2) ** 0.5

    # Izračunaj ubrzanje čestica
    a_sun = G * MZ / r ** 2
    a_earth = G * MS / r ** 2

    # Izračunaj nove brzine čestica
    v_sun = 0  # Sunce je mirno
    v_earth_perpendicular = v_perpendicular
    v_earth = (v_earth_perpendicular ** 2 + (G * MS / r) ** 2) ** 0.5

    # Izračunaj nove koordinate čestica koristeći Eulerovu metodu
    x_sun.append(x_sun[-1] + v_sun * dt)
    y_sun.append(y_sun[-1] + v_sun * dt)
    x_earth.append(x_earth[-1] + v_earth * dt)
    y_earth.append(y_earth[-1] + v_earth_perpendicular * dt)

# Crtanje putanja
plt.plot(x_sun, y_sun, label="Sunce")
plt.plot(x_earth, y_earth, label="Zemlja")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Putanje Sunca i Zemlje")
plt.legend()
plt.show()