import math

def distance(x1=0,x2=0,y1=0,y2=0):
    d = math.sqrt((x2-x1)**2+(y2-y1)**2)
    return d

x = distance(0,3,0,4)
print(x)