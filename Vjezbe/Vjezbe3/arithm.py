import math
xsuma=0
ysuma=0
listax=[]
listay=[]
for i in range(10):
    x=int(input())
    y=int(input())
    listax.append(x)
    listay.append(y)
    xsuma=xsuma+x
    ysuma=ysuma+y   
xarit=xsuma/10
yarit=ysuma/10
for i in range(10):
    sigmax=math.sqrt((listax[i]-xarit)*(listax[i]-xarit))
    sigmay=math.sqrt((listay[i]-yarit)*(listay[i]-yarit))
sigmax=sigmax/(10*9)
sigmay=sigmay/(10*9)
print("({}, {})±({}, {})" .format(xarit, yarit, sigmax, sigmay))