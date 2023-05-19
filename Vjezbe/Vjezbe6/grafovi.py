import  harmonic_oscillator as osc
import matplotlib.pyplot as plt
x0 = 1.0
v0 = 0.0
k = 1.0
m = 1.0
dt = 0.01
oscillator = osc.HarmonicOscillator(x0, v0, k, m, dt)
t_values = [i*dt for i in range(1000)]
x_values = [oscillator.position(t) for t in t_values]
v_values = [oscillator.velocity(t) for t in t_values]
a_values = [oscillator.acceleration(t) for t in t_values]
fig, axs = plt.subplots(3, 1)
axs[0].plot(t_values, x_values)
axs[0].set_ylabel('Position (m)')
axs[0].set_title('Position vs Time')
axs[1].plot(t_values, v_values)
axs[1].set_ylabel('Velocity (m/s)')
axs[1].set_title('Velocity vs Time')
axs[2].plot(t_values, a_values)
axs[2].set_xlabel('Time (s)')
axs[2].set_ylabel('Acceleration (m/s^2)')
axs[2].set_title('Acceleration vs Time')
plt.tight_layout()
plt.show()