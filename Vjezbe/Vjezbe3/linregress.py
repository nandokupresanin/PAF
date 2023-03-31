import numpy as np
import matplotlib.pyplot as plt
import math
M=[0.052, 0.124, 0.168, 0.236, 0.284, 0.336]
kut=[0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472]
suma_xy=0
for i in range(6):
    suma_xy=suma_xy+M[i]*kut[i] 
kut_squared=[element**2 for element in kut]
srednjikutkvadrat=np.sum(kut_squared)/6
suma_xy=suma_xy/6
a=suma_xy/srednjikutkvadrat
lista=[]
for element in kut:
    item=element*a
    lista.append(item)
M_squared=[element**2 for element in M]
srednjiMkvadrat=np.sum(M_squared)/6
dev=math.sqrt((1/6)*(srednjiMkvadrat/srednjikutkvadrat-a**2))
print("Standardna devijacija iznosi: ±{}" .format(dev))
plt.scatter(kut, M, marker="o")
plt.plot(kut, lista, color="orange")
plt.show()