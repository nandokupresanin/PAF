import matplotlib.pyplot as plt
import numpy as np
x=int(input())
y=int(input())
z=int(input())
k=int(input())
xpoints=np.array([x, z])
ypoints=np.array([y, k])
plt.plot(xpoints, ypoints, 'o')
def funkcija(x1, y1, x2, y2):
    x1points=[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    y1points=[]
    for element in x1points:
        y=(y2-y1)/(x2-x1)*element+(-1)*(y2-y1)/(x2-x1)*x1+y1
        y1points.append(y)
    plt.plot(x1points, y1points)
funkcija(x, y, z, k)
vrsta_grafa=input()
ime=input()
if(vrsta_grafa=='pdf'):
    plt.savefig("{}.pdf".format(ime), format="pdf", bbox_inches="tight") 
else:
    plt.title("{}".format(ime))
    plt.show()