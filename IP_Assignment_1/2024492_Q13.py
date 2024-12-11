import random
def test():
    n=random.randint(10,10**9-1)
    temp=n
    dig=0
    while temp!=0:
        dig+=1
        temp//=10
    limit=dig//2
    if dig%2==0:
        limit-=1
    k=random.randint(0,limit)
    k=2*k+1
    return n,k

def lucky(n,k):
    temp=n
    odd=0
    even=0
    dig=0
    while temp!=0:
        if dig%2==0:
            odd+=temp%10
        else:
            even+=temp%10
        dig+=1
        temp//=10
    if even<odd:
        for _ in range(k):
            x=n//(10**(dig-1))
            n=(n%(10**(dig-1)))*10+x
    return n

def _test():
    # Question is incorrect as shifting number to the left by some odd number k doesn't always generate a lucky number
    # But have done operations as question has required
    assert lucky(123456789,3)==456789123
    assert lucky(35,1)==53
    assert lucky(715,1)==157

_test()
n,k=test()
print(lucky(n,k))