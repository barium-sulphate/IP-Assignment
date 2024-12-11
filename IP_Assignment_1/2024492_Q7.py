def gcd(a,b):
    for i in range(min(a,b),0,-1):
        if a%i==0 and b%i==0:
            return i
pi=3.1415926
limit=6/(pi**2)
change=float(input("Enter closeness to convergence value that satisfies (x%): "))
low=(100-change)*limit/100
high=(100+change)*limit/100
x=1
while True:
    track=0
    # Taking square N*N with points of the form {(x,y);x,y belong in range[1,n];x,y belong to natural numbers}
    for i in range(1,x+1):
        for j in range(1,x+1):
            if gcd(i,j)==1:
                track+=1
    if track/((x)**2)>=low and high>=track/((x)**2):
        print("Closeness to convergence value is achieved taking N =",x)
        break
    else:
        x+=1