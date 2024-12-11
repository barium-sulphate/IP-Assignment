import math
# Importing math for computing log

def velocity(x):
    temp=140000/(140000-2100*x)
    return 2000*math.log(temp)-9.8*x

def distance(a,b):
    dist=0
    k=a
    while k<b:
        avg=(velocity(k)+velocity(k+0.25))/2
        dist+=avg*0.25
        k+=0.25
    return dist

def _test():
    # Haven't used round function to get precise value
    assert distance(1,2)==30.836050726346194
    assert distance(2,3)==51.965195597215896
    assert distance(2,4)==125.54537627743936

_test()
a=int(input("Enter starting time: "))
b=int(input("Enter ending time: "))
print("Distance covered by rocket:",distance(a,b))