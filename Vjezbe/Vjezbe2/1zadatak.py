import matplotlib.pyplot as plt
import numpy as np
F=int(input())
m=int(input())
a=F/m
x1points=[0, 1, 2, 3, 4, 5]
apoints=[a, a, a, a, a, a]
fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3)
ax1.plot(x1points, apoints)
ax1.set_title("a-t graf")
tpoints=[]
vpoints=[]
v=0
t=0
x=0
xpoints=[]
while (t<=5):
    tpoints.append(t)
    t=t+0.1
    dv=a*0.1
    v=v+dv
    dx=v*0.1
    x=x+dx
    vpoints.append(v)
    xpoints.append(x)
ax2.plot(tpoints, vpoints)
ax2.set_title("v-t graf")
ax3.plot(tpoints, xpoints)
ax3.set_title("x-t graf")
plt.show()