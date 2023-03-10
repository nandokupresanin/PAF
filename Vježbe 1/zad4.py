x=int(input())
y=int(input())
z=int(input())
k=int(input())
def funkcija(x1, y1, x2, y2):
    if((-1)*(y2-y1)/(x2-x1)*x1+y1>=0):
        print("y={}x+{}".format((y2-y1)/(x2-x1), (-1)*(y2-y1)/(x2-x1)*x1+y1))
    else:
        print("y={}x{}".format((y2-y1)/(x2-x1), (-1)*(y2-y1)/(x2-x1)*x1+y1))
funkcija(x, y, z, k)