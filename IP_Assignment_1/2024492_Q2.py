pi=3.14159
def sin(x):
    global pi
    x*=pi/180
    flag=1
    prod=1
    sumo=0
    # Computing taylor series for sin and cos to 50 terms to get precise value
    for i in range(1,100):
        prod*=i
        if i%2!=0:
            k=(x**i/prod)*flag
            sumo+=k
            if flag==1:
                flag=-1
            else:
                flag=1
    return sumo

def cos(x):
    global pi
    x*=pi/180
    flag=1
    prod=1
    sumo=0
    for i in range(0,100):
        if i!=0:
            prod*=i
        if i%2==0:
            k=(x**i/prod)*flag
            sumo+=k
            if flag==1:
                flag=-1
            else:
                flag=1
    return sumo

def height(l,x):
    return l*sin(x)/cos(x)

def hypotenuse(l,x):
    return l/cos(x)

def _test():
    # Haven't used round function to get precise value
    assert hypotenuse(30,45)==42.42637872565081
    assert height(30,45)==29.999960196179497
    assert hypotenuse(45,30)==51.96151095912582
    assert height(45,30)==25.980735577641997

_test()
x=int(input("Enter angle in degrees: "))
l=int(input("Enter base: "))
print("Height of the pole:",height(l,x))
print("Distance to the top of the pole:",hypotenuse(l,x))