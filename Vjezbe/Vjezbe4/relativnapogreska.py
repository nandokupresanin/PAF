import particle as prt
import numpy as np
import matplotlib.pyplot as plt
import math
dtlista=np.linspace(0.01, 0.1, 1000)
greske=[]
for dt in dtlista:
    p1=prt.Particle(10, 60, 0, 0, dt)
    v0x=10*math.cos(np.radians(60))
    v0y=10*math.sin(np.radians(60))
    Dan=p1.range()
    Dnum=2*v0x*v0y/9.81
    greska=abs(Dan-Dnum)/Dan*100
    greske.append(greska)
plt.plot(dtlista, greske)
plt.ylim(0, 11)
plt.show()