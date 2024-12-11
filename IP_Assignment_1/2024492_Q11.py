n=int(input("Enter pyramid size: "))
menu=0
breaker=True
while breaker:
    if menu%2==0:
        temp=0
        count=2*n
        for i in range(2*n+1):
            if i%2==0:
                ans=''
                track=temp
                for j in range(count):
                    if j%2!=0 and track!=0:
                        track-=1
                        ans+="  "
                    else:
                        ans+="* "
                print(ans,end="")
                print("*",end="")
                for x in range(len(ans)-1,-1,-1):
                    print(ans[x],end='')
                print()
            else:
                ans=''
                temp+=1
                track=temp
                for k in range(count):
                    if k%2==0 and track!=0:
                        ans+="* "
                        track-=1
                    else:
                        ans+="  "
                print(ans,end='')
                print(" ",end='')
                for x in range(len(ans)-1,-1,-1):
                    print(ans[x],end='')
                print()
        for i in range(2*n):
            if i%2!=0:
                ans=''
                track=temp
                for j in range(count):
                    if j%2!=0 and track!=0:
                        track-=1
                        ans+="  "
                    else:
                        ans+="* "
                print(ans,end="")
                print("*",end="")
                for x in range(len(ans)-1,-1,-1):
                    print(ans[x],end='')
                print()
            else:
                ans=''
                track=temp
                for k in range(count):
                    if k%2==0 and track!=0:
                        ans+="* "
                        track-=1
                    else:
                        ans+="  "
                print(ans,end='')
                print(" ",end='')
                for x in range(len(ans)-1,-1,-1):
                    print(ans[x],end='')
                print()
                temp-=1
    else:
        for i in range(1,n+2):
            print(" "*(2*(n+1-i)),end='')
            print("*"*(1+4*(i-1)))
    while True:
        print("A - Switch View")
        print("B - Exit")
        choice=input()
        if choice=="A":
            menu+=1
            break
        elif choice=="B":
            breaker=False
            break
        else:
            print("Choice is unavailable in menu")
            print("Please Try Again")