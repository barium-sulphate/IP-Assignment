e=2.71828
def demand(p,a,b):
    return e**(a-b*p)

def supply(p,c,d):
    return e**(c+d*p)

def ans(a,b,c,d,price):
    # Increasing price by 5 percent every time and stopping when supply crosses demand
    # Although equilibrium isn't accurate, done as question has told
    while demand(price,a,b)>supply(price,c,d):
        price*=1.05
    return price

def _test():
    assert ans(10,1.05,1.0,1.06,1.0)==4.321942375150668

_test()
price=float(input("Enter minimum price: "))
a=float(input("Enter a: "))
b=float(input("Enter b: "))
c=float(input("Enter c: "))
d=float(input("Enter d: "))
chain=ans(a,b,c,d,price)
print("Equilibrium price:",chain)
print("Demand:",demand(chain,a,b))
print("Supply:",supply(chain,c,d))