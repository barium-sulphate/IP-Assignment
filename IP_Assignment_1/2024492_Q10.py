def gregorian(month,year):
    if month<=2:
        month+=12
        year-=1
        year+=(abs(year)//400+1)*400
    h=(6+((13*(month+1))//5)+(year%100)+((year%100)//4)+((year//100)//4)+(5*(year//100)))%7
    return h
def julian(month,year):
    if month<=2:
        month+=12
        year-=1
        year+=(abs(year)//28+1)*28
    h=(11+((13*(month+1))//5)+(year%100)+((year%100)//4)-(year//100))%7
    return h
print("Capitalise the first letter of the month")
print("Give month and year in the format - Month XXXX BC/AD")
month,year,bc=input("Enter month and year: ").split()
print("1 - Julian Calender")
print("2 - Gregorian Calender")
version=int(input("Enter calender type: "))
year=int(year)
if bc=="BC":
    year-=1
    year*=(-1)
time=0
if month=="January":
    month=1
elif month=="February":
    month=2
elif month=="March":
    month=3
elif month=="April":
    month=4
elif month=="May":
    month=5
elif month=="June":
    month=6
elif month=="July":
    month=7
elif month=="August":
    month=8
elif month=="September":
    month=9
elif month=="October":
    month=10
elif month=="November":
    month=11
elif month=="December":
    month=12
breaker=True
while breaker:
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        time=31
    elif month==2:
        time=28
        if year%4==0:
            time+=1
        if year%100==0:
            time-=1
        if year%400==0:
            time+=1
    else:
        time=30
    print("Mon",end=' ')
    print("Tue",end=' ')
    print("Wed",end=' ')
    print("Thu",end=' ')
    print("Fri",end=' ')
    print("Sat",end=' ')
    print("Sun")
    if version==2:
        odd=gregorian(month,year)
    else:
        odd=julian(month,year)
    print("    "*odd,end='')
    for i in range(1,time+1):
        if i//10==0:
            if (odd+i)%7!=0:
                print(' ',i,'  ',sep='',end='')
            else:
                print(' ',i,'  ',sep='')
        else:
            if (odd+i)%7!=0 and i!=time:
                print(i,'  ',sep='',end='')
            else:
                print(i,'  ',sep='')
    while True:
        print("1 - View Next Month")
        print("2 - View Previous Month")
        print("3 - Exit")
        choice=input()
        if choice=="1":
            month+=1
            if month==13:
                month=1
                year+=1
            break
        elif choice=="2":
            month-=1
            if month==0:
                month=12
                year-=1
            break
        elif choice=="3":
            breaker=False
            break
        else:
            print("Choice is unavailable in menu")
            print("Please Try Again")