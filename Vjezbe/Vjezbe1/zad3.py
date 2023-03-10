x=input()
y=input()
z=input()
k=input()
x=int(x)
y=int(y)
z=int(z)
k=int(k)
if((k-y)/(z-x)*x+z>=0):
    print("y={}x+{}".format((k-y)/(z-x), (k-y)/(z-x)*x+z))
else:
    print("y={}x{}".format((k-y)/(z-x), (k-y)/(z-x)*x+z))
