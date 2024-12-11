def twodig(x):
    temp=x
    dig=0
    while temp!=0:
        dig+=1
        temp//=10
    ans=''
    if dig==2:
        if x//10==9:
            ans+="ninety "
        elif x//10==8:
            ans+="eighty "
        elif x//10==7:
            ans+="seventy "
        elif x//10==6:
            ans+="sixty "
        elif x//10==5:
            ans+="fifty "
        elif x//10==4:
            ans+="forty "
        elif x//10==3:
            ans+="thirty "
        elif x//10==2:
            ans+="twenty "
        elif x//10==1:
            dig-=1
            if x%10==9:
                ans+="nineteen "
            elif x%10==8:
                ans+="eighteen "
            elif x%10==7:
                ans+="seventeen "
            elif x%10==6:
                ans+="sixteen "
            elif x%10==5:
                ans+="fifteen "
            elif x%10==4:
                ans+="fourteen "
            elif x%10==3:
                ans+="thirteen "
            elif x%10==2:
                ans+="twelve "
            elif x%10==1:
                ans+="eleven "
            elif x%10==0:
                ans+="ten "
        dig-=1
    if dig==1:
        if x%10==9:
            ans+="nine "
        elif x%10==8:
            ans+="eight "
        elif x%10==7:
            ans+="seven "
        elif x%10==6:
            ans+="six "
        elif x%10==5:
            ans+="five "
        elif x%10==4:
            ans+="four "
        elif x%10==3:
            ans+="three "
        elif x%10==2:
            ans+="two "
        elif x%10==1:
            ans+="one "
    return ans

def ans(x):
    temp=x
    dig=0
    ans=''
    while temp!=0:
        dig+=1
        temp//=10
    if x==0:
        ans="zero"
    if dig>7:
        if x//(10**7)!=0: 
            ans+=twodig(x//(10**7))
            ans+="crore "
        x%=10**7
        dig=7
    if dig>5:
        if x//(10**5)!=0: 
            ans+=twodig(x//(10**5))
            ans+="lakh "
        x%=10**5
        dig=5
    if dig>3:
        if x//(10**3)!=0:
            ans+=twodig(x//(10**3))
            ans+="thousand "
        x%=10**3
        dig=3
    if dig>2:
        if x//(10**2)!=0: 
            ans+=twodig(x//(10**2))
            ans+="hundred "
        x%=10**2
        dig=2
    if dig>0:
        if x!=0: 
            ans+=twodig(x)
        x%=10**0
        dig=0
    return ans

def _test():
    assert ans(40000002)=="four crore two "
    assert ans(0)=="zero"
    assert ans(52345)=="fifty two thousand three hundred forty five "
    assert ans(51)=="fifty one "

_test()
x=int(input("Enter number: "))
print(ans(x))