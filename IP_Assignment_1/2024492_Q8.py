def solve(result,h=0.1):
    y=0
    x=1
    temp=result
    dig=0
    while temp%1!=0:
        dig+=1
        temp*=10
    while x<result:
        y+=(x+y)*h
        x+=h
    return y

x=float(input("Enter x at which you want to determine value of function: "))
h=float(input("Enter value you want to increment x by for calculating (h): "))
print(solve(x,h))