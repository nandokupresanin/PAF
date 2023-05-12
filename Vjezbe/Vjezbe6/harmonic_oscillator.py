import math
import matplotlib.pyplot as plt
import numpy as np
class HarmonicOscillator:
    def __init__(self, x0, v0, k, m, dt):
        self.x = x0
        self.v = v0
        self.k = k
        self.m = m
        self.dt = dt

    def update(self):
        x_new = self.x + self.v*self.dt
        v_new = self.v - (self.k/self.m)*self.x*self.dt
        self.x = x_new
        self.v = v_new

    def position(self, t):
        steps = int(t/self.dt)
        for i in range(steps):
            self.update()
        return self.x

    def velocity(self, t):
        steps = int(t/self.dt)
        for i in range(steps):
            self.update()
        return self.v

    def acceleration(self, t):
        omega = math.sqrt(self.k/self.m)
        x = self.position(t)
        v = self.velocity(t)
        a = -self.k * x - self.m * omega * v
        return a
    
    def period(self):
        t = 0
        x_sign = math.copysign(1, self.x)
        while math.copysign(1, self.x) == x_sign:
            self.update()
            t += self.dt
        return 2*t
        