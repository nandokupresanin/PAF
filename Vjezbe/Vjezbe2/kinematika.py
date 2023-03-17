import matplotlib.pyplot as plt
import numpy as np
import math
def jednoliko_gibanje(F, m):
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
def kosi_hitac(v, kut):
    dt=0.1
    kutrad=kut*math.pi/180
    listax=[]
    listay=[]
    listat=[]
    fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3)
    vx=v*math.cos(kutrad)
    x=0
    listax.append(x)
    vy=v*math.sin(kutrad)
    y=0
    listay.append(y)
    t=0
    listat.append(t)
    while t<10:
        x=x+vx*dt
        vy=vy-9.81*dt
        y=y+vy*dt
        listax.append(x)
        listay.append(y)
        t=t+dt
        listat.append(t)
    print("{} \n {} \n {}".format(listax, listay, listat))
    ax1.plot(listax, listay)
    ax1.set_title("x-y graf")
    ax1.set(xlabel="x(m)", ylabel="y(m)")
    ax2.plot(listat, listax)
    ax2.set_title("x-t graf")
    ax2.set(xlabel="x(m)", ylabel="t(s)")
    ax3.plot(listat, listay)
    ax3.set_title("y-t graf")
    ax3.set(xlabel="y(m)", ylabel="t(s)")
    plt.show()