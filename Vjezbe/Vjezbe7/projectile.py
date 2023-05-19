import math
import matplotlib.pyplot as plt
import numpy as np
class Projectile:
    def __init__(self, x0, y0, v0, theta, dt, mass, drag_coefficient):
        self.x = [x0]
        self.y = [y0]
        self.vx = v0 * math.cos(theta)
        self.vy = v0 * math.sin(theta)
        self.dt = dt
        self.mass = mass
        self.drag_coefficient = drag_coefficient

    def simulate(self):
        while self.y[-1] >= 0:
            vx_new = self.vx - (self.drag_coefficient * self.vx * self.dt) / self.mass
            vy_new = self.vy - (9.81 + (self.drag_coefficient * self.vy * self.dt) / self.mass) * self.dt
            x_new = self.x[-1] + vx_new * self.dt
            y_new = self.y[-1] + vy_new * self.dt

            self.vx=vx_new
            self.vy=vy_new
            self.x.append(x_new)
            self.y.append(y_new)

    def rungekutta(self):
        while self.y[-1] >= 0:
            k1_x = self.dt * self.vx
            k1_y = self.dt * self.vy

            k2_x = self.dt * (self.vx - (self.drag_coefficient / self.mass) * self.vx)
            k2_y = self.dt * (self.vy - (self.drag_coefficient / self.mass) * self.vy - 9.81)

            k3_x = self.dt * (self.vx - (self.drag_coefficient / self.mass) * self.vx)
            k3_y = self.dt * (self.vy - (self.drag_coefficient / self.mass) * self.vy - 9.81)

            k4_x = self.dt * (self.vx - (self.drag_coefficient / self.mass) * self.vx)
            k4_y = self.dt * (self.vy - (self.drag_coefficient / self.mass) * self.vy - 9.81)

            self.x.append(self.x[-1] + (k1_x + 2 * k2_x + 2 * k3_x + k4_x) / 6)
            self.y.append(self.y[-1] + (k1_y + 2 * k2_y + 2 * k3_y + k4_y) / 6)

    def plot_trajectory(self):
        plt.plot(self.x, self.y)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Kosi hitac s otporom zraka')
        plt.show()
