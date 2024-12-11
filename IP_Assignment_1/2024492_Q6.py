def function(x):
    y=x**3 - 10.5*x**2 + 34.5*x - 35
    return y

def derivative(x):
    y=3*x**2 - 21*x + 34.5
    return y

def main(x):
    # Lowered the limits of function(x) so that rounding x to nearest value will give exact value of root
    track=0
    while function(x)>0.01 or function(x)<-0.01 or track<=100:
        x-=function(x)/derivative(x)
        track+=1
    return x

def bonus(x1,x2,n):
    print("Roots of the polynomial present in range",x1,"and",x2,"are as follows: ")
    root=0
    start=x1
    while start<=x2 and root<n:
        k=round(main(start),1)
        if k>=x1 and k<=x2:
            if root==0:
                root+=1
                lastk=k
                print(k)
            else:
                if lastk!=k:
                    print(k)
                    lastk=k
                    root+=1
        start+=0.1
while True:
    print("1 - Main Question")
    print("2 - Bonus Question")
    print("3 - Exit")
    choice=int(input("Enter what you would like to do: "))
    if choice==1:
        x0=float(input("Enter value of x0: "))
        print("Value given by program is",main(x0))
        print("Therefore we can deduce that root of the function is",round(main(x0),1))
    elif choice==2:
        x1=float(input("Enter starting value of range (x1): "))
        x2=float(input("Enter ending value of range (x2): "))
        n=int(input("Enter number of roots present in range: "))
        bonus(x1,x2,n)
    elif choice==3:
        break