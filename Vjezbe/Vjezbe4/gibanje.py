import particle as prt
import math
import numpy as np
p1=prt.Particle(100, 45, 0, 0, dt=0.01)
v0x=100*math.cos(np.radians(45))
v0y=100*math.sin(np.radians(45))
Dnum=2*v0x*v0y/9.81
Dan=p1.range()
razlika=abs(Dnum-Dan)
print(p1.range())
print(Dnum)
print(razlika)
#javilo se odstupanje od 0.4271201552332968